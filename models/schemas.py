from pydantic import BaseModel
from typing import List

class ProductCreate(BaseModel):
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
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
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
    products: List[ProductItemOrder]


class OrderResponse(BaseModel):
    id: int
    client: str
    products: List[dict]
    date: str
    total: float