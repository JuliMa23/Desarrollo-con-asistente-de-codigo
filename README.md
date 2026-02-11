# Contact Management System

A clean and scalable contact management application built with Python, demonstrating solid software engineering principles through a Model-View-Controller (MVC) architecture and comprehensive test coverage.

## Overview

This project implements a contact management system with CRUD operations, showcasing object-oriented programming principles, separation of concerns, and maintainable code structure. The application uses JSON-based persistence and follows industry-standard architectural patterns.

## Key Features

- **Complete CRUD Operations**: Create, read, update, and delete contacts with ease
- **MVC Architecture**: Clean separation between models, services, and controllers
- **Data Persistence**: JSON-based storage with automatic file handling
- **Extensible Design**: Service layer abstraction enables easy database migration
- **Test Coverage**: Pytest framework integration for unit and integration testing
- **Type Hints**: Enhanced code readability and IDE support with Python type annotations

## Tech Stack

- **Language**: Python 3.x
- **Testing Framework**: pytest 7.0+
- **Data Storage**: JSON (file-based persistence)
- **Architecture Pattern**: MVC (Model-View-Controller)
- **Development Practices**: Object-Oriented Programming, SOLID principles

## Project Structure

```
.
├── src/
│   ├── main.py                          # Application entry point
│   ├── models/
│   │   └── contacto.py                  # Contact entity with serialization
│   ├── services/
│   │   └── contacto_service.py          # Business logic and data access layer
│   ├── controllers/
│   │   └── contacto_controller.py       # Request handling and orchestration
│   └── data/
│       └── contactos.json               # JSON data storage
├── tests/
│   ├── test_contacto.py                 # Unit tests for Contact model
│   └── test_contacto_controller.py      # Integration tests for controller
├── requirements.txt                      # Python dependencies
├── pytest.ini                           # Pytest configuration
└── README.md                            # Project documentation
```

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/JuliMa23/Desarrollo-con-asistente-de-codigo.git
cd Desarrollo-con-asistente-de-codigo
```

2. Create and activate a virtual environment:

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

3. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## How to Run the Project

### Running the Application

Execute the main application:
```bash
python -m src.main
```

### Running Tests

Run the test suite:
```bash
pytest -q
```

For verbose output with detailed test information:
```bash
pytest -v
```

For test coverage report:
```bash
pytest --cov=src tests/
```

## Usage Example

The application provides a service layer for managing contacts programmatically:

```python
from src.services.contacto_service import ContactoService
from src.models.contacto import Contacto

# Initialize the service with a data file
service = ContactoService('src/data/contactos.json')

# Create a new contact
new_contact = Contacto(
    id='1',
    nombre='John Doe',
    telefono='+1234567890',
    correo='john.doe@example.com'
)

# Add contact to the system
service.agregar_contacto(new_contact.to_dict())

# Retrieve all contacts
contacts = service.cargar_contactos()

# Get a specific contact
contact = service.obtener_contacto('1')

# Delete a contact
service.eliminar_contacto('1')
```

## Architecture Highlights

### Model Layer
The `Contacto` class encapsulates contact data with serialization methods (`to_dict`, `from_dict`) for easy persistence and retrieval.

### Service Layer
`ContactoService` implements the business logic and handles data persistence, abstracting storage implementation details from the rest of the application.

### Controller Layer
`ContactoController` orchestrates user interactions and delegates operations to the service layer, following the single responsibility principle.

## Development Best Practices

- **Virtual Environment**: All dependencies are isolated in a virtual environment
- **Type Hints**: Functions include type annotations for better code documentation
- **Error Handling**: Defensive programming with proper exception handling
- **Clean Code**: Follows PEP 8 style guidelines for Python code
- **Modular Design**: Clear separation of concerns enables easy testing and maintenance

## Future Improvements

- Implement a Repository pattern interface to enable multiple storage backends (PostgreSQL, MongoDB, SQLite)
- Add input validation and custom exception handling for improved error messaging
- Develop a command-line interface (CLI) with argparse or Click for better user interaction
- Integrate a web framework (Flask/FastAPI) to provide RESTful API endpoints
- Add comprehensive integration tests with fixtures and mocking
- Implement logging functionality for debugging and monitoring
- Add data validation using Pydantic models
- Create a CI/CD pipeline with GitHub Actions for automated testing and deployment
- Add database migrations support using Alembic
- Implement authentication and authorization for multi-user support

## Contributing

Contributions are welcome. Please ensure that all tests pass before submitting a pull request.

## License

This project is available for educational and portfolio purposes.

---

**Note**: This project was developed as a demonstration of software engineering fundamentals and is suitable for inclusion in a technical portfolio.
