from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

# Import routers
from app.api.v1.router import api_router
from app.config.database import init_database, close_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting up FastAPI application...")
    await init_database()
    yield
    # Shutdown
    print("🛑 Shutting down FastAPI application...")
    await close_database()

# Create FastAPI instance
app = FastAPI(
    title="FastApi Demo App",
    description="A FastAPI project with MongoDB and Redis",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Demo!", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "Server is running",
        "version": "1.0.0"
    }

# Include API routers
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
