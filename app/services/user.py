import bcrypt
import asyncio
from app.models import User
from app.schemas import UserCreate
from fastapi import HTTPException, status

class UserService:
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using bcrypt"""
        # Convert password to bytes
        password_bytes = password.encode('utf-8')
        # Generate salt and hash password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        # Return as string
        return hashed.decode('utf-8')
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        password_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    
    @staticmethod
    async def create_user(user_data: UserCreate) -> User:
        """Create a new user"""
        try:
            # Check if username already exists
            existing_user = await User.find_one(User.username == user_data.username)
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already exists"
                )
            
            # Check if email already exists
            existing_email = await User.find_one(User.email == user_data.email)
            if existing_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )
            
            # Hash the password
            hashed_password = UserService.hash_password(user_data.password)
            
            # Create user instance
            user = User(
                username=user_data.username,
                email=user_data.email,
                password=hashed_password,
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                phone=user_data.phone,
                bio=user_data.bio
            )
            
            # Save to database
            await user.save()
            return user
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error creating user: {str(e)}"
            )

    @staticmethod
    async def get_users(skip:int=0,limit:int=10,search:str="") -> list[User]:
        """Get all users"""
        try:
            criteria = {}
            
            if search:
                criteria = {
                    "$or": [
                        {"first_name": {"$regex": search, "$options": "i"}},
                        {"last_name": {"$regex": search, "$options": "i"}},
                        {"email": {"$regex": search, "$options": "i"}},
                        {"username": {"$regex": search, "$options": "i"}},
                    ]
                }
            
            # Create tasks for parallel execution
            data_task = User.find(criteria).skip(skip).limit(limit).to_list()
            count_task = User.find(criteria).count()

            # Execute both queries in parallel
            data, count = await asyncio.gather(data_task, count_task)

            return {
                    "data": data,
                    "count": count
                 }
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error getting user data: {str(e)}"
            )
