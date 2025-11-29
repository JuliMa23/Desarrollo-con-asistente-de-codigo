from typing import Optional


class ContactoController:
	"""Controlador mínimo para interactuar con el servicio de contactos.

	Los métodos están definidos en español y con propósito educativo; completa
	la lógica poco a poco (por ejemplo usando GitHub Copilot).
	"""

	def __init__(self, servicio=None):
		"""Inicializa el controlador con una instancia del servicio.

		Args:
			servicio: objeto que implemente la interfaz de servicio (opcional).
		"""
		self.servicio = servicio

	def run(self):
		"""Punto de entrada para ejecutar el controlador (p. ej. un bucle CLI).

		Aquí puedes llamar a mostrar_menu(), procesar comandos, etc.
		"""
		# TODO: implementar el loop o flujo principal
		pass

	def crear_contacto(self, nombre: str, correo: Optional[str] = None, telefono: Optional[str] = None):
		"""Crear un contacto usando el servicio.

		Debe delegar en `self.servicio.agregar_contacto` o similar.
		"""
		# TODO: implementar creación
		pass

	def listar_contactos(self):
		"""Obtener y devolver la lista de contactos desde el servicio."""
		# TODO: implementar listado
		pass

	def mostrar_menu(self):
		"""Mostrar opciones (CLI) y devolver la opción seleccionada."""
		# TODO: implementar UI mínima
		pass
