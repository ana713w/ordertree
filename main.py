from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from contextlib import asynccontextmanager


# Import routers modules (to inject dependencies)
from routers import product, order

# Import data structures
from bst_products import BST_Products
from list_orders import LinkedList_Orders
from persistencia import PersistenceJSON

# Load environment variables
load_dotenv()

bst_products = BST_Products()
linked_list_orders = LinkedList_Orders()
persistence = PersistenceJSON()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP - Load data
    persistence.load_products(bst_products)
    persistence.load_orders(linked_list_orders, bst_products)
    print("🚀 API started successfully")
    
    yield 
    
    # SHUTDOWN - Save data
    persistence.save_products(bst_products)
    persistence.save_orders(linked_list_orders)
    print("💾 Data saved successfully")


app = FastAPI(
    lifespan=lifespan  
)

product.bst_products = bst_products
product.persistence = persistence

order.linked_list_orders = linked_list_orders
order.bst_products = bst_products
order.persistence = persistence

app.include_router(product)
app.include_router(order)


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