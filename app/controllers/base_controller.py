from typing import Any, Dict
from fastapi import HTTPException, status

class BaseController:
    """
    Base controller class with common controller functionality
    """
    
    def __init__(self, service: Any):
        self.service = service
    
    def _handle_not_found(self, entity_name: str = "Resource") -> None:
        """Raise HTTPException for not found resources"""
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{entity_name} not found"
        )
    
    def _handle_conflict(self, message: str) -> None:
        """Raise HTTPException for conflicts"""
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=message
        )
    
    def _handle_bad_request(self, message: str) -> None:
        """Raise HTTPException for bad requests"""
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )
    
    def _success_response(self, data: Any, message: str = "Operation successful") -> Dict[str, Any]:
        """Standard success response format"""
        return {
            "data": data,
            "message": message
        }
    
    def _error_response(self, message: str) -> Dict[str, Any]:
        """Standard error response format"""
        return {
            "data": None,
            "message": message
        } 