from fastapi import APIRouter, Depends, HTTPException
from app.controllers.product_faq import ProductFaqController
from app.schemas.product_faq import ProductFaq

product_faq_controller = ProductFaqController()
router = APIRouter(prefix="/product-faq", tags=["Products FAQ's"])


@router.post("/")
async def create_product_faq(data: ProductFaq):
    try:
        return await product_faq_controller.create_faq(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create product FAQ: {str(e)}")
