import motor.motor_asyncio
from beanie import init_beanie
from .settings import settings
from app.models import User, ProductModel  # Import all your document models here

async def init_database():
    """
    Initialize MongoDB database connection with Beanie
    """
    # Create Motor client
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)    
    # Initialize beanie with the Product document class and a database
    print(f"🔗 Connecting to MongoDB at {settings.mongodb_url}...")
    await init_beanie(
        database=client[settings.mongodb_db_name],
        document_models=[
            User,  # Add all your document models here
            ProductModel,  # Add when you create Product model
        ]
    )
    
    print(f"✅ Connected to MongoDB database: {settings.mongodb_db_name}")
    
async def close_database():
    """
    Close database connection
    """
    # Beanie automatically handles connection cleanup
    print("🔌 Database connection closed")
    pass
