from fastapi import APIRouter, HTTPException, status
from app.schemas import UserCreate, UserRead
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/signup", response_model=UserRead, status_code=status.HTTP_201_CREATED)
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
    response = await UserService.create_user(user_data)
    return UserRead.model_validate(response)

@router.get("/", status_code=status.HTTP_201_CREATED)
async def get_users(skip:int=0,limit:int=10,search:str=""):
    """
    Retrieve a list of users.

    - **skip**: Number of records to skip for pagination (default: 0)
    - **limit**: Maximum number of users to return (default: 10)
    - **search**: Optional search query to filter users by username or email
    """
    response = await UserService.get_users(skip,limit,search)
    return response
