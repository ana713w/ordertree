from fastapi import APIRouter, HTTPException, status
from models.schemas import ProductCreate, ProductItemOrder

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

