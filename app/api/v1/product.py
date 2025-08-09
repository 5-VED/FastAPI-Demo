from typing import Dict, Any
from fastapi import APIRouter, Query
from app.schemas.product import ProductBase
from app.controllers.product_controller import ProductController

router = APIRouter(prefix="/products", tags=["Products"])

# Initialize controller
product_controller = ProductController()

@router.post(
    "/add_product")
async def create_product(product_data: ProductBase):
    """
    Create a new product.

    **Request Body**:
    - **name** (str): Name of the product. Must be unique and 3–100 characters long.
    - **description** (str, optional): Detailed description of the product.
    - **price** (float): Price of the product. Must be a positive value.
    - **stock** (int): Quantity available in stock. Must be a non-negative integer.
    - **category** (str, optional): Category to which the product belongs.
    - **tags** (list[str], optional): List of tags/keywords for search optimization.

    **Returns**:
    - **201**: Product created successfully.
    - **400**: Invalid input data.
    - **500**: Internal server error.
    """
    try:
        print("Adding product with data:", product_data)
        return await product_controller.create_product(product_data.dict())
    except Exception as e:
        return {"error": f"Failed to add product: {str(e)}"}


@router.get(
    "/"
)
async def get_all_products(
    skip: int = Query(0, description="Number of products to skip for pagination."),
    limit: int = Query(10, description="Maximum number of products to return."),
    search: str = Query("", description="Search term to filter products by name.")
):
    """
    Get all products.

    **Query Parameters**:
    - **skip** (int): Number of products to skip (default: 0).
    - **limit** (int): Maximum number of products to return (default: 10).
    - **search** (str, optional): Search term to filter by product name.

    **Returns**:
    - **200**: List of matching products.
    - **500**: Internal server error.
    """
    try:
        return await product_controller.get_all_products(skip, limit, search)
    except Exception as e:
        return {"error": f"Failed to fetch products: {str(e)}"}


@router.delete(
    "/{id}")
async def delete_products(id: str):
    """
    Delete a product.

    **Path Parameter**:
    - **id** (str): Unique ID of the product to delete.

    **Returns**:
    - **200**: Product deleted successfully.
    - **404**: Product not found.
    - **500**: Internal server error.
    """
    try:
        return await product_controller.delete_product(id)
    except Exception as e:
        return {"error": f"Failed to delete product: {str(e)}"}
