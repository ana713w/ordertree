from fastapi import APIRouter, HTTPException, status
from models.schemas import ProductCreate, ProductResponse

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

bst_products = None
persistence = None

@router.get("/", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_list_products():
    products = bst_products.list_all()

    return {
        "total": len(products),
        "products": products
    }

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    """
    Create a new product in BST
    """
    if bst_products.search(product.id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this ID already exists"
        )
    
    bst_products.insert(product.id, product.name, product.price, product.stock)
    persistence.save_products(bst_products)
    
    return {
        "message": "Product created successfully",
        "product": product.model_dump()
    }

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_id: int):
    """
    Get product by ID - BST search O(log n)
    """
    product = bst_products.search(product_id)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    return product.to_dict()

