from typing import Any, Dict
# from app.services.product import ProductService
from fastapi import HTTPException, status
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository = None):
        self.product_repository = product_repository or ProductRepository()

    async def create_product(self, product_data: dict) -> dict:
        try:
            product = await self.product_repository.create(product_data)
            return product
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create product: {str(e)}"
            )