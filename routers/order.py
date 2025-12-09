from fastapi import APIRouter, HTTPException, status
from schemas import OrderCreate, OrderUpdate, OrderResponse

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# Will be injected from main.py
linked_list_orders = None
bst_products = None
persistence = None


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    """
    Create new order in Linked List
    """
    # Validate products exist in BST
    for item in order.products:
        product = bst_products.search(item.product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {item.product_id} not found"
            )
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product.name}"
            )
    
    products_list = [
        {"product_id": p.product_id, "quantity": p.quantity}
        for p in order.products
    ]
    
    new_order = linked_list_orders.add_order(
        order.client,
        products_list,
        bst_products
    )
    
    persistence.save_orders(linked_list_orders)
    
    return {
        "message": "Order created successfully",
        "order": new_order.to_dict()
    }


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int):
    """
    Get order by ID
    """
    order = linked_list_orders.search_order(order_id)
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    return order.to_dict()


@router.put("/{order_id}")
async def update_order(order_id: int, data: OrderUpdate):
    """
    Update order products
    """
    order = linked_list_orders.search_order(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    for item in data.products:
        product = bst_products.search(item.product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {item.product_id} not found"
            )
    
    products_list = [
        {"product_id": p.product_id, "quantity": p.quantity}
        for p in data.products
    ]
    
    updated = linked_list_orders.update_order(
        order_id,
        products_list,
        bst_products
    )
    
    persistence.save_orders(linked_list_orders)
    
    return {
        "message": "Order updated successfully",
        "order": updated.to_dict()
    }


@router.delete("/{order_id}")
async def delete_order(order_id: int):
    """
    Delete order from linked list
    """
    deleted = linked_list_orders.delete_order(order_id)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    persistence.save_orders(linked_list_orders)
    
    return {
        "message": f"Order {order_id} deleted successfully"
    }


@router.get("/")
async def list_orders():
    """
    List all orders
    """
    orders = linked_list_orders.list_all()
    return {
        "total": len(orders),
        "orders": orders
    }