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
├── requirements.txt
├── pytest.ini
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── contacto.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── contacto_controller.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── contacto_service.py
│   └── data/
│       ├── __init__.py
│       └── contactos.json
└── tests/
		├── __init__.py
		├── conftest.py
		├── test_contacto.py
		└── test_contacto_controller.py
```

## Explicación de cada parte

- `README.md`: Documentación del proyecto, cómo arrancar y notas de arquitectura.
- `requirements.txt`: Dependencias (aquí `pytest` para ejecutar las pruebas).
- `pytest.ini`: Configuración mínima de `pytest` (patrón de nombres de tests).

- `src/`: Código fuente principal.

  - `main.py`: Punto de entrada (vacío por ahora; útil para CLI o launcher).
  - `models/contacto.py`: Modelos del dominio. `Contacto` es la entidad principal con helpers de serialización.
  - `controllers/contacto_controller.py`: Adaptadores / funciones que exponen operaciones (crear, listar) y orquestan llamadas a `services`.
  - `services/contacto_service.py`: Lógica de negocio y acceso a datos (en este scaffold persiste en JSON). Aquí deben ir reglas, validaciones y coordinación entre repositorios.
  - `data/contactos.json`: Fichero JSON que actúa como almacenamiento local para pruebas y prototipos.

- `tests/`: Pruebas con `pytest`.
  - `conftest.py`: Fixtures compartidas para tests (si se necesitan más adelante).
  - `test_contacto.py`: Test unitario del modelo (serialización).
  - `test_contacto_controller.py`: Test de integración ligero que verifica la creación y lectura de contactos usando un archivo temporal.

## Notas de diseño y recomendaciones

- Separación de capas: modelos <-> services <-> controllers permite cambiar la persistencia (por ejemplo a una base de datos) sin tocar la lógica de negocio.
- Repositorio/Adapter: cuando escales, crea una interfaz `Repository` en `src/services` o `src/repositories` y un adaptador JSON; luego agrega adaptadores para SQLite/Postgres.
- Tests: usa `tmp_path` para que los tests de integración no modifiquen ficheros reales. Añade tests unitarios que mockeen I/O cuando pruebes la lógica aislada.
- CI: añade un workflow de GitHub Actions que cree el venv, instale dependencias y ejecute `pytest` en cada push/PR.

Si quieres, puedo ahora:

- Crear la interfaz `Repository` y un adaptador JSON (opción recomendada para escalar).
- Añadir validaciones en `models/contacto.py` y tests unitarios adicionales.
- Generar un `README` más extenso con ejemplos de uso y comandos.

Dime qué prefieres y lo implemento.

## Pasos que seguí al preparar este repositorio

1. Creé la estructura de carpetas requerida (`src`, `src/models`, `src/controllers`, `src/services`, `src/data`, `tests`).
2. Añadí archivos plantilla mínimos (vacíos o con pequeñas implementaciones):
   - `src/models/contacto.py`: `Contacto` (dataclass) con helpers `to_dict`/`from_dict`.
   - `src/services/contacto_service.py`: servicio mínimo que persiste en JSON.
   - `src/controllers/contacto_controller.py`: funciones para crear y listar contactos.
   - `tests/test_contacto.py` y `tests/test_contacto_controller.py`: tests básicos (serialización e integración usando `tmp_path`).
3. Creé un entorno virtual local en `./.venv`, instalé `pytest` y ejecuté la suite de tests.
   - Resultado: `2 passed` (los tests añadidos pasan correctamente).

## Cómo están pensadas las capas (resumen)

- Modelos: representan datos y suelen incluir validaciones y serialización.
- Services: contienen la lógica de negocio; en producción tendrían validaciones, reglas y llamadas a repositorios.
- Controllers: adaptadores entre la capa de entrada (CLI/API) y los servicios.

## Testing

- Ejecuta `pytest -q` en el entorno virtual para correr todos los tests.
- Usa `tmp_path` en `pytest` para crear ficheros temporales en tests de integración y no tocar los datos reales.

## Siguientes pasos recomendados

- Separar la abstracción de almacenamiento (Repository) y crear adaptadores para JSON y, si lo deseas, para SQLite/Postgres.
- Añadir validaciones y manejo de errores (clases de excepción en `services` o `models`).
- Preparar CI (GitHub Actions) que ejecute `pytest` automáticamente.
