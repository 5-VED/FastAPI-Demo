from beanie import Document
from datetime import datetime
from pydantic import Field
from typing import Optional
from bson import ObjectId

class BaseDocument(Document):
    """
    Base document with common fields for all collections
    """
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    is_active: bool = Field(default=True, description="Soft delete flag")
    is_deleted: bool = Field(default=False, description="Deletion flag")
    
    async def save_with_timestamp(self, **kwargs):
        """Save document with updated timestamp"""
        self.updated_at = datetime.utcnow()
        return await self.save(**kwargs)
    
    async def soft_delete(self):
        """Mark document as deleted without removing from database"""
        self.is_deleted = True
        self.is_active = False
        self.updated_at = datetime.utcnow()
        return await self.save()
    
    def to_dict(self) -> dict:
        """Convert document to dictionary"""
        return self.dict()
    
    class Settings:
        # Common settings for all documents
        use_state_management = True
