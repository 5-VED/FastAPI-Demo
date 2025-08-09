"""
Schemas package for FastAPI Demo
"""

from .base import BaseDocumentSchema
from .user import (
    UserBase,
    UserCreate,
    # UserUpdate,
    UserRead
)
from .product import ProductBase

__all__ = [
    "BaseDocumentSchema",
    "UserBase",
    "UserCreate",
    # "UserUpdate",
    "UserRead",
    "ProductBase"
]
