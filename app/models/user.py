from typing import Optional, List
from pydantic import Field, EmailStr
from beanie import Indexed
from .base import BaseDocument

class User(BaseDocument):
    """
    User document model for MongoDB
    """
    # Required fields
    username: Indexed(str, unique=True) = Field(..., description="Unique username")
    email: Indexed(EmailStr, unique=True) = Field(..., description="User email address")
    
    password: str = Field(..., description="Hashed password")    
    first_name: str = Field(None, description="User's first name")
    last_name: str = Field(None, description="User's last name")
    phone: str = Field(None, description="Phone number")
    
    is_verified: bool = Field(default=False, description="Email verification status")
    
    # Additional fields
    profile_picture: Optional[str] = Field(None, description="URL to profile picture")
    bio: Optional[str] = Field(None, max_length=500, description="User biography")
    
    # Methods
    def get_full_name(self) -> str:
        """Get user's full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    class Settings:
        name = "users_collection"  # MongoDB collection name
        indexes = [
            "username",
            "email", 
            "created_at",
            "is_active"
        ]
