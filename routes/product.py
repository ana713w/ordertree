from fastapi import APIRouter, HTTPException, status
from models.schemas import ProductCreate, ProductItemOrder
from configuration.connections import db
from mysql.connector import Error

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


