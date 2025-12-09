from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# Import our data structures
from bst_products import BST_Products
from list_orders import LinkedList_Orders
from persistencia import PersistenceJSON

# Cargar variables de entorno
load_dotenv()

# Crear instancia de FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Bienvenido a Order Tree",
            "version": "1.0.0",
            "docs": "/docs"
        }
    )

bst_products = BST_Products()
linked_list_orders = LinkedList_Orders()
persistence = PersistenceJSON()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc),
            "path": str(request.url)
        }
    )