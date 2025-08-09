from typing import Dict, Any
from fastapi import APIRouter, Query
from app.schemas.product import ProductBase
from app.controllers.product_controller import ProductController

router = APIRouter(prefix="/products", tags=["products"])

# Initialize controller
product_controller = ProductController()

@router.post("/add_product")
async def create_product(product_data: ProductBase):
    try:
        print("Adding product with data:", product_data)
        return await product_controller.create_product(product_data.dict())
    except Exception as e:
        return {"error": f"Failed to add product: {str(e)}"}