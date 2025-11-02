from fastapi import APIRouter
from .user import router as user_router
from .product import router as product_router

# Main API router for version 1
api_router = APIRouter()

# Include user routes
api_router.include_router(user_router)
# api_router.include_router(product_router)
