from fastapi import APIRouter, Query
from app.schemas import UserCreate
from app.controllers import UserController
from typing import Dict, Any

router = APIRouter(prefix="/users", tags=["Users"])

# Initialize controller
user_controller = UserController()

@router.post("/")
async def create_user(user_data: UserCreate):
    """
    Create a new user
    
    - **username**: Must be unique and alphanumeric (3-50 characters)
    - **email**: Must be a valid email address and unique
    - **password**: Minimum 8 characters
    - **confirm_password**: Must match the password
    - **first_name**: User's first name
    - **last_name**: User's last name
    - **phone**: Phone number (optional)
    - **bio**: User biography (optional, max 500 characters)
    """
    return await user_controller.create_user(user_data)

@router.get("/")
async def get_users(
    skip: int = Query(0, ge=0, description="Number of records to skip for pagination"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of users to return"),
    search: str = Query("", description="Optional search query to filter users")
):
    """
    Retrieve a list of users with pagination and search.

    - **skip**: Number of records to skip for pagination (default: 0)
    - **limit**: Maximum number of users to return (default: 10, max: 100)
    - **search**: Optional search query to filter users by username, email, first name, or last name
    """
    return await user_controller.get_users(skip, limit, search)

@router.get("/{user_id}")
async def get_user(user_id: str):
    """
    Get a user by their ID
    
    - **user_id**: The unique identifier of the user
    """
    return await user_controller.get_user(user_id)

@router.put("/{user_id}")
async def update_user(user_id: str, payload: Any):
    """
    Update a user by their ID
    
    - **user_id**: The unique identifier of the user to update
    - **payload**: User data to update (all fields optional)
    """
    return await user_controller.update_user(user_id, payload)

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    """
    Delete a user by their unique ID.

    - **user_id**: The unique identifier of the user to delete
    """
    return await user_controller.delete_user(user_id)
