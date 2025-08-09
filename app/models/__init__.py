"""
Models package for FastAPI Demo
"""

from .base import BaseDocument
from .user import User
from .product import ProductModel
__all__ = ["BaseDocument", "User", "ProductModel"]
