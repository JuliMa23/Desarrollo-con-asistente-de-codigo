import json
import os
from pathlib import Path
from typing import List, Optional


class ContactoService:
    """Servicio para gestionar contactos (interfaz mínima).

    Implementa la estructura de métodos en español para que puedas
    completarlos poco a poco: cargar, guardar, agregar, obtener,
    actualizar y eliminar.
    """

    def __init__(self, archivo_json: Optional[str] = None):
        """Inicializa el servicio con la ruta al archivo JSON.

        Args:
            archivo_json: ruta al fichero JSON de persistencia (opcional).
        """
        self.archivo_json = archivo_json

    def cargar_contactos(self) -> List[dict]:
        """Leer contactos desde el archivo JSON y devolver lista de diccionarios."""

        # Si no se ha indicado archivo o no existe, devolver lista vacía
        if not self.archivo_json or not os.path.exists(self.archivo_json):
            return []

        with open(self.archivo_json, 'r', encoding='utf-8') as file:
            try:
                contactos = json.load(file)
            except json.JSONDecodeError:
                contactos = []

        return contactos

    def guardar_contactos(self, contactos: List[dict]) -> None:
        """Guardar lista de contactos (diccionarios) en el archivo JSON."""

        if not self.archivo_json:
            return

        archivo_path = Path(self.archivo_json)
        if not archivo_path.exists():
            archivo_path.parent.mkdir(parents=True, exist_ok=True)
            archivo_path.touch()

        with open(self.archivo_json, 'w', encoding='utf-8') as file:
            json.dump(contactos, file, ensure_ascii=False, indent=4)

    def agregar_contacto(self, contacto: dict) -> dict:
        """Agregar un nuevo contacto al almacenamiento y devolverlo."""
        contactos = self.cargar_contactos()
        contactos.append(contacto)
        self.guardar_contactos(contactos)
        return contacto

    def obtener_contacto(self, contacto_id: str) -> Optional[dict]:
        """Obtener un contacto por su id."""
        contactos = self.cargar_contactos()
        for contacto in contactos:
            if contacto.get('id') == contacto_id:
                return contacto
        print("Contacto no encontrado.")
        return None

    def actualizar_contacto(self, contacto: dict) -> dict:
        """Actualizar un contacto existente y devolverlo."""
        pass

    def eliminar_contacto(self, contacto_id: str) -> None:
        """Eliminar un contacto por su id."""
        contactos = self.cargar_contactos()
        contactos = [contacto for contacto in contactos if contacto.get('id') != contacto_id]
        self.guardar_contactos(contactos)


