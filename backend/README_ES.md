# Sistema de Gestión de Pedidos de Cerveza Backend

Un servicio backend basado en FastAPI para gestionar pedidos e inventario de cerveza.

## Características

- Gestión de inventario de cervezas
- Procesamiento de pedidos por rondas
- Cálculos de descuentos
- Stock validation
- Estado de órdenes basado en pagos
- Promoción Happy Hour: descuento de 1 pinta por cada 3 pintas ordenadas

## Detalles del Diseño

El sistema fue diseñado considerando que:
- Una orden tiene un estado que depende de si está pagada o no
- Cada orden contiene un listado de rondas que representan los pedidos realizados por grupos de amigos
- Se implementa una promoción de Happy Hour donde por cada 3 pintas se descuenta 1
- El proyecto está desarrollado con arquitectura hexagonal para facilitar la escalabilidad rápida

## Requisitos Previos

- Python 3.11 o superior
- pip (Instalador de paquetes de Python)

## Instalación

1. Clonar el repositorio

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Unix/macOS
# o
venv\Scripts\activate  # En Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar la Aplicación

1. Iniciar el servidor de desarrollo:
```bash
uvicorn src.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Ejecutar Pruebas

Ejecutar el conjunto de pruebas usando pytest:
```bash
python -m pytest
```

El proyecto cuenta con 27 tests unitarios que verifican el correcto funcionamiento de todas las funcionalidades.

## Documentación de la API

Una vez que el servidor esté en funcionamiento, puedes acceder a:
- Documentación de Swagger UI en: `http://localhost:8000/docs`
- Documentación de ReDoc en: `http://localhost:8000/redoc`

## Estructura del Proyecto

```
backend/
├── src/
│   ├── application/      # Lógica de negocio de la aplicación
│   ├── domain/           # Entidades de dominio y excepciones
│   ├── infrastructure/   # Implementaciones de interfaces externas
│   └── main.py          # Punto de entrada de la aplicación
├── tests/               # Conjunto de pruebas
└── requirements.txt     # Dependencias del proyecto
```

## Desarrollo

El proyecto sigue un patrón de arquitectura hexagonal (ports and adapters) con:
- Principios de diseño guiado por el dominio
- Lógica de negocio centrada en casos de uso
- Patrón de repositorio para acceso a datos
- Cobertura exhaustiva de pruebas (20 tests unitarios)
- Diseñado para escalar rápidamente gracias a su arquitectura desacoplada