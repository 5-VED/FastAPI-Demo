from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from .base import BaseDocumentSchema

class ProductBase(BaseModel):
    """
    Base Product schema with common fields
    """
    product_name: str = Field(..., min_length=3, max_length=100, description="Product name")
    price: float = Field(..., gt=0, description="Product price")
    image_url: Optional[str] = Field(None, description="URL to product image")
    video_url: Optional[str] = Field(None, description="URL to product video")
    description: Optional[str] = Field(None, max_length=1000, description="Product description")
