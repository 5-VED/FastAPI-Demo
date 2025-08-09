from typing import Dict, Any
from app.schemas import ProductBase
from app.services.product import ProductService
from app.repositories import ProductRepository
from .base_controller import BaseController

class ProductController(BaseController):
    """
    Product controller class handling product-related HTTP requests
    """
    def __init__(self):
        product_repository = ProductRepository()
        product_service = ProductService(product_repository)
        self.product_service = product_service
        super().__init__(product_service)

    async def create_product(self, product_data: dict) -> dict:
        try:
            result = await self.service.create_product(product_data)
            return {
                "data": result,
                "message": "Product created successfully"
            }
        except Exception as e:
            return {"error": f"Failed to create product: {str(e)}"}
