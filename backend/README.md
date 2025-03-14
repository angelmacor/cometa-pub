# Beer Ordering System Backend

A FastAPI-based backend service for managing beer orders and inventory.

## Features

- Beer inventory management
- Order processing with rounds
- Discount calculations
- Stock validation

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation

1. Clone the repository

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the development server:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## Running Tests

Execute the test suite using pytest:
```bash
python -m pytest
```

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation at: `http://localhost:8000/docs`
- ReDoc documentation at: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── src/
│   ├── application/      # Application business logic
│   ├── domain/           # Domain entities and exceptions
│   ├── infrastructure/   # External interfaces implementations
│   └── main.py          # Application entry point
├── tests/               # Test suite
└── requirements.txt     # Project dependencies
```

## Development

The project follows a clean architecture pattern with:
- Domain-driven design principles
- Use case-centered business logic
- Repository pattern for data access
- Comprehensive test coverage