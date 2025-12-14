from typing import List, Optional
from pydantic import Field
from beanie import Indexed
from .base import BaseDocument

class ProductModel(BaseDocument):
    """
    Product document model for MongoDB
    """
    product_name: Indexed(str, unique = True) = Field(..., description="Unique product name")
    price: float = Field(..., description="Product price")
    image_url: Optional[str] = Field(None, description="URL to product image")
    video_url: Optional[str] = Field(None, description="URL to product video")
    description: Optional[str] = Field(None, max_length=1000, description="Product description")

    class Settings:
        name = "products_collection"
        indexes = [
            "product_name",
            "price",
            "created_at"
        ]