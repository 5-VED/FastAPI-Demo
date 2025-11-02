from typing import Dict, Any
from app.schemas import UserCreate, UserUpdate
from app.services.user import UserService
from app.repositories import UserRepository
from .base_controller import BaseController

class UserController(BaseController):
    """
    User controller class handling user-related HTTP requests
    """
    
    def __init__(self):
        user_repository = UserRepository()
        user_service = UserService(user_repository)
        super().__init__(user_service)
    
    async def create_user(self, user_data: UserCreate) -> Dict[str, Any]:
        """Handle user creation""" 
        try:
            result = await self.service.create_user(user_data)
            return self._success_response(
                result["data"], 
                result["message"]
            )
        except Exception as e:
            return self._error_response(f"Failed to create user: {str(e)}")
    
    async def get_user(self, user_id: str) -> Dict[str, Any]:
        """Handle get user by ID"""
        try:
            result = await self.service.get_user(user_id)
            
            if result["data"] is None:
                return self._error_response(result["message"])
            
            return self._success_response(
                result["data"], 
                result["message"]
            )
        except Exception as e:
            return self._error_response(f"Failed to get user: {str(e)}")
    
    async def get_users(self, skip: int = 0, limit: int = 10, search: str = "") -> Dict[str, Any]:
        """Handle get all users with pagination and search"""
        try:
            result = await self.service.get_users(skip, limit, search)
            return self._success_response(result, "Users fetched successfully")
        except Exception as e:
            return self._error_response(f"Failed to get users: {str(e)}")
    
    async def update_user(self, user_id: str, user_data: UserUpdate) -> Dict[str, Any]:
        """Handle user update"""
        try:
            result = await self.service.update_user(user_id, user_data)
            
            if result["data"] is None:
                return self._error_response(result["message"])
            
            return self._success_response(
                result["data"], 
                result["message"]
            )
        except Exception as e:
            return self._error_response(f"Failed to update user: {str(e)}")
    
    async def delete_user(self, user_id: str) -> Dict[str, Any]:
        """Handle user deletion"""
        try:
            result = await self.service.delete_user(user_id)
            
            if result["data"] is None:
                return self._error_response(result["message"])
            
            return self._success_response(
                result["data"], 
                result["message"]
            )
        except Exception as e:
            return self._error_response(f"Failed to delete user: {str(e)}")
