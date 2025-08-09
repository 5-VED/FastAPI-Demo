import bcrypt
import asyncio
from typing import Dict, Any

from app.repositories import UserRepository
from app.schemas import UserCreate
from fastapi import HTTPException, status


class UserService:

    def __init__(self, user_repository: UserRepository = None):
        self.user_repo = user_repository or UserRepository()

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using bcrypt"""
        # Convert password to bytes
        password_bytes = password.encode("utf-8")
        # Generate salt and hash password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        # Return as string
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        password_bytes = plain_password.encode("utf-8")
        hashed_bytes = hashed_password.encode("utf-8")
        return bcrypt.checkpw(password_bytes, hashed_bytes)

    async def create_user(self, user_data: UserCreate) -> Dict[str, Any]:
        """Create a new user"""
        try:
            # Check if username already exists
            if await self.user_repo.username_exists(user_data.username):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already exists"
                )

            # Check if email already exists  
            if await self.user_repo.email_exists(user_data.email):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )

            # Hash the password
            hashed_password = self.hash_password(user_data.password)

            # Create user data
            user_dict = {
                "username": user_data.username,
                "email": user_data.email,
                "hashed_password": hashed_password,
                "first_name": user_data.first_name,
                "last_name": user_data.last_name,
                "phone": user_data.phone,
                "bio": user_data.bio
            }

            # Create user via repository
            user = await self.user_repo.create(user_dict)
            return {"data": user, "message": "User created successfully"}

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error creating user: {str(e)}",
            )

    async def get_users(self, skip: int = 0, limit: int = 10, search: str = "") -> Dict[str, Any]:
        """Get all users with pagination and search"""
        try:
            result = await self.user_repo.get_users_with_pagination(skip, limit, search)
            return result
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error getting users data: {str(e)}",
            )

    async def get_user(self, user_id: str) -> Dict[str, Any]:
        """Get a user by their ID"""
        try:
            user = await self.user_repo.find_by_id(user_id)
            if user is None:
                return {"data": None, "message": "User not found"}

            return {"data": user, "message": "User fetched successfully"}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error getting user data: {str(e)}",
            )

    async def delete_user(self, user_id: str) -> Dict[str, Any]:
        """
        Delete a user by their ID.

        This method attempts to find and delete a user from the database using the provided user_id.
        If the user is found, it is deleted and a success message is returned.
        If the user does not exist, an HTTP 404 error is raised.
        Any unexpected errors during the process will result in an HTTP 500 error.

        Args:
            user_id (str): The unique identifier of the user to be deleted.

        Returns:
            dict: A dictionary containing the deleted user's data and a success message.

        Raises:
            HTTPException: If the user is not found (404) or if an internal server error occurs (500).
        """
        try:
            # Find the user first
            user = await self.user_repo.find_by_id(user_id)

            if user is None:
                return {"data": None, "message": "User not found"}

            # Delete user via repository
            deleted = await self.user_repo.delete_by_id(user_id)
            
            if deleted:
                return {"data": user, "message": "User deleted successfully"}
            else:
                return {"data": None, "message": "Failed to delete user"}

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error getting user data: {str(e)}",
            )

    async def update_user(self, user_id: str, payload: Any) -> Dict[str, Any]:
        """Update a user by their ID"""
        try:
            update_data = payload.model_dump(exclude_unset=True, exclude_none=True)
            
            if not update_data:
                return {"data": None, "message": "No fields to update"}
            
            # Update user via repository
            updated_user = await self.user_repo.update_by_id(user_id, update_data)
            
            if updated_user:
                return {"data": updated_user, "message": "User updated successfully"}
            else:
                return {"data": None, "message": "User not found"}

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error updating user data: {str(e)}"
            )
