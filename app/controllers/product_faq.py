from typing import Dict,Optional,Any
from app.services.product_faq import ProductFaqService
from .base_controller import BaseController


class ProductFaqController(BaseController):
    def __init__(self):        
        self.product_faq_service = ProductFaqService()


    async def create_faq(self,data:Dict[str,Any]) -> Dict[str,Any]:
        try: 
            result = await self.product_faq_service.create_faq(data)
            return {
                "data": result,
                "message": "Product FAQ created successfully"
            }
        except Exception as e:
            return {"error": f"Failed to create product faq: {str(e)}"}
    
    async def get_faqs(self,product_id:Optional[str]=None) -> Dict[str,Any]:
        try:
            faqs = await self.product_faq_service.get_all_faq(product_id)
            return {
                "data": faqs,
                "message": "Product FAQs fetched successfully"
            }
        except Exception as e:
            return {"error": f"Failed to fetch product faqs: {str(e)}"}
    
    async def delete_faq(self,id:Optional[str]="", slug:Optional[str] ="") -> Dict[str,Any]:
        try:
            result = await self.product_faq_service.delete_faq(id, slug)
            return {
                "data": result,
                "message": "Product FAQ deleted successfully"
            }
        except Exception as e:
            return {"error": f"Failed to delete product faq: {str(e)}"}
        
    async def update_faq(self,id:str,data:Dict[str,Any]) -> Dict[str,Any]:
        try:
            result = await self.product_faq_service.update_faq(id, data)
            return {
                "data": result,
                "message": "Product FAQ updated successfully"
            }
        except Exception as e:
            return {"error": f"Failed to update product faq: {str(e)}"}