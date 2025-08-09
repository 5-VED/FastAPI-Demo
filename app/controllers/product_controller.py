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

    async def get_all_products(self, skip: int = 0, limit: int = 10, search: str = "") -> Dict[str, Any]:
        try:
            products = await self.service.get_all_products(skip=skip, limit=limit, search=search)
            return {
                "data": products,
                "message": "Products fetched successfully"
            }
        except Exception as e:
            return {"error": f"Failed to fetch products: {str(e)}"}

    async def delete_product(self, id: str) -> Dict[str, Any]:
        try:
            result = await self.service.product_repository.delete(id)
            if not result:
                self._handle_not_found("Product")
            return {
                "is_deleted": result,
                "message": "Product deleted successfully"
            }
        except Exception as e:
            return {"error": f"Failed to delete product: {str(e)}"}