"""
Lead-related Pydantic schemas.
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LeadCreate(BaseModel):
    customer_id: Optional[int] = None
    intent: Optional[str] = None
    property_type: Optional[str] = None
    bedrooms: Optional[int] = None
    location: Optional[str] = None
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    currency: str = "NGN"
    transaction_type: Optional[str] = None
    timeline: Optional[str] = None
    additional_requirements: Optional[str] = None
    source: Optional[str] = None


class LeadUpdate(BaseModel):
    intent: Optional[str] = None
    property_type: Optional[str] = None
    bedrooms: Optional[int] = None
    location: Optional[str] = None
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    currency: Optional[str] = None
    transaction_type: Optional[str] = None
    timeline: Optional[str] = None
    additional_requirements: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    score: Optional[float] = None
    assigned_agent_id: Optional[int] = None
    notes: Optional[str] = None


class LeadOut(BaseModel):
    id: int
    customer_id: Optional[int] = None
    intent: Optional[str] = None
    property_type: Optional[str] = None
    bedrooms: Optional[int] = None
    location: Optional[str] = None
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    currency: str
    transaction_type: Optional[str] = None
    timeline: Optional[str] = None
    status: str
    priority: Optional[str] = None
    score: Optional[float] = None
    assigned_agent_id: Optional[int] = None
    source: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
