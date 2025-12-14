from typing import List, Optional,Dict ,Any
from pydantic import Field
from beanie import Indexed , Document, PydanticObjectId 
from app.models.product import ProductModel
from .base_repository import BaseRepository


class ProductRepository(BaseRepository):
    """
    Product document model for MongoDB
    """
    def __init__(self):
        super().__init__(ProductModel)

    async def create(self, data: Dict[str, Any]) -> Document:
        """ Create a new Document """
        try:
            instance = self.model(**data)
            await instance.save()
            return instance
        except Exception as e:
            print(f"Error creating product: {str(e)}")
            raise

    async def get_all(self, skip: int = 0, limit: int = 10, search: str = "") -> List[Document]:
        """ Get all products with optional search, skip and limit """
        try:
            query = {}
            if search:
                query["product_name"] = {"$regex": search, "$options": "i"}
            products = await self.model.find(query).skip(skip).limit(limit).to_list()
            return products
        except Exception as e:
            print(f"Error fetching products: {str(e)}")
            raise

    async def delete(self, id: str) -> bool:
        """ Delete a product by ID """
        try:
            product_id = PydanticObjectId(id)
            result = await self.model.get(product_id)
            if not result:
                return False
            await result.delete()
            return True
        except Exception as e:
            print(f"Error deleting product: {str(e)}")
            raise       