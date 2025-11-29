# Gestión de Contactos

Proyecto de ejemplo pensado para aprender programación orientada a objetos (POO) y testing con `pytest`.

## Quickstart (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

## Arquitectura y organización

Este proyecto está organizado de forma simple y escalable para una pequeña aplicación de gestión de contactos:

- `models/` - Clases del dominio (p. ej. `contacto.py` con la entidad `Contacto`).
- `controllers/` - Capas de orquestación o adaptadores que exponen operaciones (crear, listar, etc.).
- `services/` - Lógica de negocio y acceso simple a datos (en este scaffold se persiste en JSON).
- `data/` - Ficheros de datos (por ejemplo `contactos.json`).

## Arquitectura (árbol)

La estructura del proyecto se organiza de forma clara para separar responsabilidades. A continuación tienes la visualización en árbol exactamente como está creada:

```
Modulo_2/
├── README.md
# Desarrollo con asistente de código

Proyecto educativo en Python para gestionar contactos. Está pensado como scaffold para practicar Programación Orientada a Objetos (POO), pruebas con `pytest` y trabajo guiado con asistentes de código.

**Repositorio remoto:** https://github.com/JuliMa23/Desarrollo-con-asistente-de-codigo

## Descripción

Ejemplo didáctico que separa responsabilidades en `models`, `services` y `controllers`, y utiliza un fichero JSON para persistencia en fase de prototipo.

## Quickstart (PowerShell)

```powershell
# Crear entorno virtual
python -m venv .venv

# Activar (PowerShell)
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Ejecutar tests
pytest -q

# Ejecutar la aplicación (entrypoint mínimo)
python -m src.main
```

Si borras la carpeta `.venv` en tu máquina, recrea el entorno con los pasos anteriores. Antes de borrarla, exporta dependencias:

```powershell
pip freeze > requirements.txt
```

## Estructura del proyecto

- `README.md` — documentación y comandos básicos.
- `requirements.txt` — dependencias (por ejemplo `pytest`).
- `pytest.ini` — configuración de `pytest`.
- `src/` — código fuente:
  - `main.py` — punto de entrada (launcher/CLI).
  - `models/contacto.py` — entidad `Contacto` con serialización.
  - `services/contacto_service.py` — lógica y persistencia (JSON adapter en este scaffold).
  - `controllers/contacto_controller.py` — orquestador / adaptador de entrada.
  - `data/contactos.json` — almacenamiento JSON de ejemplo.
- `tests/` — pruebas con `pytest`.

## Comandos útiles

- Ver estado Git y remotos:
```powershell
git remote -v
git log --oneline -n 5
git status
```

## Testing

- Ejecuta `pytest -q` para correr la suite.
- Usa `tmp_path` en tests que necesiten filesystem temporal.

## Buenas prácticas y recomendaciones

- No subas la carpeta `.venv` al repositorio; ya está en `.gitignore`.
- Mantén `requirements.txt` actualizado con `pip freeze` para poder recrear entornos reproducibles.
- Abstrae la persistencia detrás de una interfaz `Repository` cuando quieras cambiar JSON por una base de datos.

## Próximos pasos que puedo implementar

- Añadir una interfaz `Repository` y un adaptador JSON.
- Añadir validaciones y excepciones en `models` y `services`.
- Crear un workflow de GitHub Actions que ejecute `pytest` en cada push.

---

Si quieres que agregue un `LICENSE` (MIT) o ejemplos de uso más detallados, dímelo y lo añado.
