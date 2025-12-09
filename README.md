# Order Tree - Sistema de Gestión de Pedidos

API REST desarrollada con FastAPI que implementa un sistema de gestión de pedidos para una tienda en línea, utilizando estructuras de datos avanzadas: **Árbol Binario de Búsqueda (BST)** para productos y **Lista Enlazada** para pedidos.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/ana713w/ordertree
cd ordertree
```

### 2. Crear y activar entorno virtual

**En Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install pydantic
pip install python-dotenv
```

### 4. Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

La API estará disponible en: **http://127.0.0.1:8000**

## Documentación de la API

Una vez que la aplicación esté corriendo, puedes acceder a la documentación interactiva:

- **Swagger UI**: http://127.0.0.1:8000/docs

## Endpoints Disponibles

### Endpoint Principal

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de bienvenida y versión de la API |

### Productos (`/products`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/products/` | Crear un nuevo producto en el BST |
| GET | `/products/` | Listar todos los productos |
| GET | `/products/{product_id}` | Obtener un producto específico por ID (búsqueda O(log n)) |

### Pedidos (`/orders`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/orders/` | Crear un nuevo pedido en la lista enlazada |
| GET | `/orders/` | Listar todos los pedidos |
| GET | `/orders/{order_id}` | Obtener un pedido específico por ID |
| PUT | `/orders/{order_id}` | Actualizar un pedido existente |
| DELETE | `/orders/{order_id}` | Eliminar un pedido de la lista enlazada |

## Estructura del Proyecto

```
ordertree/
│
├── main.py                     # Punto de entrada de la aplicación
├── .gitignore                  # Archivos ignorados por git
│
├── bst_products.py             # Implementación del BST para productos
├── list_orders.py              # Implementación de Lista Enlazada 
├── persistencia.py             # Sistema de persistencia con JSON
│
├── models/
│   └── schemas.py              # Esquemas Pydantic para validación
│
├── routers/
│   ├── products.py             # Endpoints relacionados con productos
│   └── orders.py               # Endpoints relacionados con pedidos
│
├── products.json               # Persistencia de productos
├── orders.json                 # Persistencia de pedidos
│
└── postman_collection/
    └── ordertree.postman_collection.json
```

## Estructuras de Datos Implementadas

### 1. Árbol Binario de Búsqueda (BST) - Productos

Los productos se almacenan en un **BST** que permite:
- Búsqueda eficiente: **O(log n)** en promedio
- Inserción ordenada por ID de producto
- Recorrido in-order para listar productos ordenados

**Ejemplo de producto:**
```json
{
  "id": 1,
  "name": "Laptop Dell XPS",
  "price": 1200.50,
  "stock": 10
}
```

### 2. Lista Enlazada - Pedidos

Los pedidos se almacenan en una **Lista Enlazada** donde:
- Cada nodo representa un pedido completo
- Permite inserción, actualización y eliminación eficiente
- Cada pedido contiene múltiples productos

**Ejemplo de pedido:**
```json
{
  "order_id": 1,
  "client": "Juan Pérez",
  "products": [
    {
      "product_id": 1,
      "quantity": 2,
      "name": "Laptop Dell XPS",
      "price": 1200.50,
      "subtotal": 2401.00
    }
  ],
  "total": 2401.00,
  "created_at": "2025-12-09T20:15:30"
}
```

## Persistencia de Datos

El sistema utiliza **serialización/deserialización JSON** para:
- Guardar automáticamente productos y pedidos al crear/modificar/eliminar
- Cargar datos al iniciar la aplicación
- Mantener la integridad de las estructuras de datos entre reinicios

Los archivos de persistencia son:
- `products.json`: Almacena todos los productos del BST
- `orders.json`: Almacena todos los pedidos de la lista enlazada

## Testing con Postman

El proyecto incluye una colección de Postman con todos los endpoints configurados:

1. Importa la colección: `postman_collection/ordertree.postman_collection.json`
2. Ejecuta las peticiones en orden para probar el flujo completo

### Flujo de prueba recomendado:

1. **Crear productos** (POST `/products/`)
2. **Consultar productos** (GET `/products/` o GET `/products/{id}`)
3. **Crear pedidos** (POST `/orders/`) - Valida que los productos existan
4. **Consultar pedidos** (GET `/orders/` o GET `/orders/{id}`)
5. **Actualizar pedido** (PUT `/orders/{id}`)
6. **Eliminar pedido** (DELETE `/orders/{id}`)

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para Python
- **Pydantic**: Validación de datos y configuración
- **Uvicorn**: Servidor ASGI para FastAPI
- **JSON**: Serialización y deserialización de datos


## Notas Importantes

- Los datos se guardan automáticamente al realizar cambios
- Al crear un pedido, se valida que los productos existan en el BST
- Se verifica el stock disponible antes de crear pedidos
- El entorno virtual debe estar activado antes de ejecutar `uvicorn`
- Los archivos `products.json` y `orders.json` se crean automáticamente


