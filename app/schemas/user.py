from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
from .base import BaseDocumentSchema

# Base User schema with common fields
class UserBase(BaseModel):
    """
    Base User schema with common fields
    """
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: EmailStr = Field(..., description="Email address")
    first_name: str = Field(None, max_length=50, description="First name")
    last_name: str = Field(None, max_length=50, description="Last name")
    phone: str = Field(None, description="Phone number")
    bio: Optional[str] = Field(None, max_length=500, description="User biography")

# Schema for creating a new user
class UserCreate(UserBase):
    """
    Schema for user creation
    """
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")
    confirm_password: str = Field(..., description="Password confirmation")
    
    @field_validator('confirm_password')
    @classmethod
    def passwords_match(cls, v, info):
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v
    
    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v):
        if not v.replace('_', '').replace('-', '').isalnum():
            raise ValueError('Username must be alphanumeric (underscores and hyphens allowed)')
        return v

# Schema for updating user information
class UserUpdate(BaseModel):
    """
    Schema for updating user information
    """
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    phone: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=500)

# Schema for reading user data (response)
class UserRead(BaseDocumentSchema):
    """
    Schema for user data in API responses
    Used when returning user information to clients
    """
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    is_verified: bool
    
    # Add computed field for full name
    @property
    def full_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
