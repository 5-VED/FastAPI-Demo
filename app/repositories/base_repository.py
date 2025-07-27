from typing import Optional, List, Dict, Any
from beanie import Document, PydanticObjectId

class BaseRepository:
    """
    Base repository class with common CRUD operations
    """
    
    def __init__(self, model: Document):
        self.model = model
    
    async def create(self, data: Dict[str, Any]) -> Document:
        """Create a new document"""
        instance = self.model(**data)
        await instance.save()
        return instance
    
    async def find_by_id(self, id: str) -> Optional[Document]:
        """Find document by ID"""
        return await self.model.find_one({"_id": PydanticObjectId(id)})
    
    async def find_all(self, skip: int = 0, limit: int = 10) -> List[Document]:
        """Get all documents with pagination"""
        return await self.model.find().skip(skip).limit(limit).to_list()
    
    async def update_by_id(self, id: str, update_data: Dict[str, Any]) -> Optional[Document]:
        """Update document by ID"""
        instance = await self.find_by_id(id)
        if instance:
            for field, value in update_data.items():
                if hasattr(instance, field):
                    setattr(instance, field, value)
            await instance.save()
        return instance
    
    async def delete_by_id(self, id: str) -> bool:
        """Delete document by ID"""
        instance = await self.find_by_id(id)
        if instance:
            await instance.delete()
            return True
        return False
    
    async def count(self, criteria: Dict[str, Any] = None) -> int:
        """Count documents matching criteria"""
        if criteria:
            return await self.model.find(criteria).count()
        return await self.model.find().count()
    
    async def find_with_criteria(self, criteria: Dict[str, Any], skip: int = 0, limit: int = 10) -> List[Document]:
        """Find documents matching criteria"""
        return await self.model.find(criteria).skip(skip).limit(limit).to_list() 