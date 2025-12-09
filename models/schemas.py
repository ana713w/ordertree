from pydantic import BaseModel
from typing import List

class ProductCreate(BaseModel):
    """
    Model to create a product
    """
    id: int
    name: str
    price: float
    stock: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Laptop Dell XPS",
                "price": 1299.99,
                "stock": 10
            }
        }

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int


class ProductItemOrder(BaseModel):
    """
    Product inside an order
    """
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    """
    Model to create an order
    """
    client: str
    products: List[ProductItemOrder]
    
    class Config:
        json_schema_extra = {
            "example": {
                "client": "Juan Pérez",
                "products": [
                    {"product_id": 1, "quantity": 2},
                    {"product_id": 2, "quantity": 1}
                ]
            }
        }


class OrderUpdate(BaseModel):
    """
    Model to update an order
    """
    products: List[ProductItemOrder]


class OrderResponse(BaseModel):
    """
    Order response model
    """
    id: int
    client: str
    products: List[dict]
    date: str
    total: float