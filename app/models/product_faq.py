from .base import BaseDocument
from pydantic import  Field


class ProductFaqModel(BaseDocument):
    """
    Product FAQ document model for MongoDB
    """
    product_id: str = Field(..., description="ID of the associated product")
    question: str = Field(..., description="Frequently asked question")
    answer: str = Field(..., description="Answer to the frequently asked question")

    class Settings:
        name = "product_faqs_collection"
        indexes = [
            "product_id",
            "created_at"
        ]

