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

    async def get_all_products(self, skip: int = 0, limit: int = 10, search: str = "") -> Dict[str, Any]:
        try:
            products = await self.product_repository.get_all(skip=skip, limit=limit, search=search)
            return {"products": products}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to fetch products: {str(e)}"
            )

    async def delete_product(self, id: str) -> Dict[str, Any]:
        try:
            result = await self.product_repository.delete(id)
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Product not found"
                )
            return {"message": "Product deleted successfully"}
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to delete product: {str(e)}"
            )