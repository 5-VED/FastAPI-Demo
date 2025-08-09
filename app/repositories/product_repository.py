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
            print("Creating product with data:", data)
            instance = self.model(**data)
            await instance.save()
            return instance
        except Exception as e:
            print(f"Error creating product: {str(e)}")
            raise
