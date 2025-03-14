# Sistema de Gestión de Pedidos de Cerveza

Un sistema completo para gestionar pedidos e inventario de cerveza, con backend basado en FastAPI y frontend desarrollado con Next.js.

## Descripción General

Este proyecto consta de dos componentes principales:
- **Backend**: API RESTful desarrollada con FastAPI y arquitectura hexagonal
- **Frontend**: Aplicación web moderna desarrollada con Next.js 13+ y TypeScript

## Características

- Gestión de inventario de cervezas
- Procesamiento de pedidos por rondas
- Cálculos de descuentos
- Validación de stock
- Estado de órdenes basado en pagos
- Promoción Happy Hour: descuento de 1 pinta por cada 3 pintas ordenadas
- Interfaz de usuario intuitiva y responsive

## Detalles del Diseño

El sistema fue diseñado considerando que:
- Una orden tiene un estado que depende de si está pagada o no
- Cada orden contiene un listado de rondas que representan los pedidos realizados por grupos de amigos
- Se implementa una promoción de Happy Hour donde por cada 3 pintas se descuenta 1
- El proyecto está desarrollado con arquitectura hexagonal para facilitar la escalabilidad rápida

# Backend

## Tech Stack Backend

- **FastAPI** - Framework web de alto rendimiento
- **Python 3.11+** - Lenguaje de programación
- **Pytest** - Framework de testing

## Requisitos Previos (Backend)

- Python 3.11 o superior
- pip (Instalador de paquetes de Python)

## Instalación (Backend)

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

## Ejecutar la Aplicación (Backend)

1. Iniciar el servidor de desarrollo:
```bash
uvicorn src.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Ejecutar Pruebas (Backend)

Ejecutar el conjunto de pruebas usando pytest:
```bash
python -m pytest
```

El proyecto cuenta con 27 tests unitarios que verifican el correcto funcionamiento de todas las funcionalidades.

## Documentación de la API

Una vez que el servidor esté en funcionamiento, puedes acceder a:
- Documentación de Swagger UI en: `http://localhost:8000/docs`
- Documentación de ReDoc en: `http://localhost:8000/redoc`

## Estructura del Proyecto (Backend)

```
backend/
├── src/
│   ├── application/      # Lógica de negocio de la aplicación
│   ├── domain/           # Entidades de dominio y excepciones
│   ├── infrastructure/   # Implementaciones de interfaces externas
│   └── main.py           # Punto de entrada de la aplicación
├── tests/                # Conjunto de pruebas
└── requirements.txt      # Dependencias del proyecto
```

## Desarrollo (Backend)

El proyecto sigue un patrón de arquitectura hexagonal (ports and adapters) con:
- Principios de diseño guiado por el dominio
- Lógica de negocio centrada en casos de uso
- Patrón de repositorio para acceso a datos
- Cobertura exhaustiva de pruebas (27 tests unitarios)
- Diseñado para escalar rápidamente gracias a su arquitectura desacoplada

# Frontend

## Tech Stack Frontend

- **Next.js 13+** - Framework React para producción
- **TypeScript** - Verificación de tipos estática
- **Tailwind CSS** - Framework CSS basado en utilidades
- **React Testing Library** - Utilidades para testing

## Requisitos Previos (Frontend)

Antes de comenzar, asegúrate de tener instalado:
- Node.js (se recomienda la versión LTS)
- npm o pnpm (gestor de paquetes)

## Instalación (Frontend)

1. Instalar dependencias:
   ```bash
   pnpm install
   # o
   npm install
   ```

2. Ejecutar el servidor de desarrollo:
   ```bash
   pnpm dev
   # o
   npm run dev
   ```

3. Configurar variables de entorno:
   ```bash
   cp env.local .env
   ```

4. Abrir [http://localhost:3000](http://localhost:3000) en tu navegador para ver el resultado.

## Estructura del Proyecto (Frontend)

```
frontend/
├── src/
│   ├── app/          # Páginas y layouts del App Router
│   ├── components/   # Componentes UI reutilizables
│   ├── hooks/        # Hooks personalizados de React
│   ├── services/     # Servicios API y obtención de datos
│   ├── types/        # Definiciones de tipos TypeScript
│   └── utils/        # Funciones de utilidad
├── public/           # Archivos estáticos
└── tests/            # Archivos de prueba
```

## Scripts Disponibles (Frontend)

- `pnpm dev` - Inicia el servidor de desarrollo
- `pnpm build` - Compila la aplicación para producción

## Directrices de Desarrollo (Frontend)

- Seguir las convenciones de TypeScript y mantener la seguridad de tipos
- Usar Tailwind CSS para estilizar componentes
- Escribir pruebas para nuevos componentes y funciones
- Seguir la estructura de proyecto existente para nuevas adiciones

## Testing (Frontend)

Utilizamos React Testing Library para pruebas de componentes. Ejecutar pruebas con:

```bash
pnpm test
```

## Más Información

Para aprender más sobre las tecnologías utilizadas:

- [Documentación de Next.js](https://nextjs.org/docs)
- [Documentación de TypeScript](https://www.typescriptlang.org/)
- [Documentación de Tailwind CSS](https://tailwindcss.com/)
- [Documentación de React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
