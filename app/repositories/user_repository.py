from typing import Optional, List, Dict, Any
from app.models import User
from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    """
    User repository class with user-specific database operations
    """
    
    def __init__(self):
        super().__init__(User)
    
    async def find_by_username(self, username: str) -> Optional[User]:
        """Find user by username"""
        return await self.model.find_one({"username": username})
    
    async def find_by_email(self, email: str) -> Optional[User]:
        """Find user by email"""
        return await self.model.find_one({"email": email})
    
    async def username_exists(self, username: str) -> bool:
        """Check if username already exists"""
        user = await self.find_by_username(username)
        return user is not None
    
    async def email_exists(self, email: str) -> bool:
        """Check if email already exists"""
        user = await self.find_by_email(email)
        return user is not None
    
    async def search_users(self, search_term: str, skip: int = 0, limit: int = 10) -> List[User]:
        """Search users by multiple fields"""
        criteria = {
            "$or": [
                {"first_name": {"$regex": search_term, "$options": "i"}},
                {"last_name": {"$regex": search_term, "$options": "i"}},
                {"email": {"$regex": search_term, "$options": "i"}},
                {"username": {"$regex": search_term, "$options": "i"}},
            ]
        }
        return await self.find_with_criteria(criteria, skip, limit)
    
    async def get_users_with_pagination(self, skip: int = 0, limit: int = 10, search: str = "") -> Dict[str, Any]:
        """Get users with pagination and optional search"""
        if search:
            users = await self.search_users(search, skip, limit)
            total_count = await self.model.find({
                "$or": [
                    {"first_name": {"$regex": search, "$options": "i"}},
                    {"last_name": {"$regex": search, "$options": "i"}},
                    {"email": {"$regex": search, "$options": "i"}},
                    {"username": {"$regex": search, "$options": "i"}},
                ]
            }).count()
        else:
            users = await self.find_all(skip, limit)
            total_count = await self.count()
        
        return {
            "data": users,
            "count": total_count,
            "skip": skip,
            "limit": limit
        } 