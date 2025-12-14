from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class ProductFaq(BaseModel):
    product_id: str = Field(...,description="Product Id")
    question: str = Field(...,description="Question for the product.")
    answer : str = Field(...,description="Answer of the question.")