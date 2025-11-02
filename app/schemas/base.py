from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BaseDocumentSchema(BaseModel):
    """
    Base schema for all document responses
    """
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_deleted: bool

    class Config:
        from_attributes = True

