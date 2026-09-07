"""
Chat-related Pydantic schemas.
"""

from typing import Optional, List
from pydantic import BaseModel, Field


class ChatMessageRequest(BaseModel):
    conversation_id: Optional[str] = Field(None, description="Existing conversation ID")
    message: str = Field(..., min_length=1, max_length=4000)
    customer_id: Optional[int] = None


class ChatMessageResponse(BaseModel):
    conversation_id: str
    message_id: Optional[str] = None
    response: str
    lead_id: Optional[int] = None
    status: str = "ok"


class MessageOut(BaseModel):
    id: int
    role: str  # user | assistant | system
    content: str
    created_at: str

    class Config:
        from_attributes = True
