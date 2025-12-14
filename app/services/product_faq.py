from typing import Optional, Dict
from app.repositories.product_faq import ProductFaqRepository
from fastapi import HTTPException, status

class ProductFaqService:
    def __init__(self, product_faq_repository: ProductFaqRepository = None):
        self.product_faq_repository = product_faq_repository        

    async def create_faq(self,data):
        try:
            faq = await self.product_faq_repository.create(data)
            return {"faq": faq}
        except Exception as e:
            print(f"Error occured while creating Product faq : -> {e}")
            raise HTTPException (
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  
                detail=f"Error creating Product FAQ: {str(e)}",
            )
    
    async def get_all_faq(self,skip:int = 0 , limit:int=10, search:str ="",sort:Dict={}):
        try:
            result = await self.product_faq_repository.get_all_faq(skip, limit, search, sort)
            return {"faqs": result}
        except Exception as e:
            print(f"Error occured while fetching Product faq : -> {e}")
            raise HTTPException (
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                details = f"Error fetching Product FAQs: {str(e)}",
            )
    
    async def delete_faq(self,id:Optional[str]="", slug:Optional[str] =""):
        try:
            result = await self.product_faq_repository.delete_faq(id, slug)
            if result == False:
                return {"message": "FAQ not found" }
            
            return {"message": "FAQ deleted successfully"}
              
        except Exception as e:
            print(f"Error occured while deleting Product faq : -> {e}")
            raise HTTPException(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                details = f"Error deleting Product FAQ: {str(e)}",
            )

    async def update_faq(self,id:str,data:Dict[str,str]):
        try:
            faq = await self.product_faq_repository.update_faq(id, **data)
            return {"faq": faq}
        except Exception as e:
            print(f"Error occured while updating Product faq : -> {e}")            
            raise HTTPException(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,    
                details = f"Error updating Product FAQ: {str(e)}",
            )