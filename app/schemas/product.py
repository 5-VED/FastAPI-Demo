# from typing import List, Optional
# from pydantic import BaseModel,Field

# class ProductSchema(BaseModel):
#     product_name:str = Field(..., min_length=3,description="Product Name")
#     description:str = Field(...,min_length=10,description="Product details.")
#     category:Optional[str] = Field(None,max_length=10,description="Category of the product.")
#     subcategory: Optional[str] = Field(None,max_length=10,description="Product Sub Category.")

#     # Cost Information 
#     price:float = Field(...,description="Price of one unit.")
#     currency:str = Field(default="USD",description="Currency Code.")
#     discount_percentage:float = Field(default=0,ge=0,le=100) 
#     tax_rate:float = Field(0,ge=0,le=100)

#     # Inventory Information
#     stock_quantity: int = Field(..., ge=0)
#     min_stock_level: int = Field(10, ge=0)
#     max_stock_level: int = Field(1000, ge=0)
#     reorder_point: int = Field(20, ge=0)
    
#     # Physical Informatin 
#     stock_quantity: int = Field(..., ge=0)
#     min_stock_level: int = Field(10, ge=0)
#     max_stock_level: int = Field(1000, ge=0)
#     reorder_point: int = Field(20, ge=0)

#     # Additional Information (Fields 19-23)
#     manufacturer: Optional[str] = Field(None, max_length=100)
#     brand: Optional[str] = Field(None, max_length=100)
#     tags: List[str] = Field(default_factory=list, max_length=20)
#     image_urls: List[str] = Field(default_factory=list, max_length=10)
#     status: Optional[str] = Field(default="Draft")

# # class ProductCreate(ProductSchema):
