"""
Lead model - core entity of the system.
"""

from datetime import datetime
from typing import Optional
from enum import Enum

from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, Text, func, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.connection import Base


class LeadStatus(str, Enum):
    NEW = "NEW"
    CONTACTED = "CONTACTED"
    QUALIFIED = "QUALIFIED"
    FOLLOW_UP = "FOLLOW_UP"
    CONVERTED = "CONVERTED"
    LOST = "LOST"
    CLOSED = "CLOSED"


class LeadPriority(str, Enum):
    HOT = "HOT"
    WARM = "WARM"
    COLD = "COLD"


class TransactionType(str, Enum):
    BUY = "BUY"
    RENT = "RENT"
    SELL = "SELL"
    INQUIRE = "INQUIRE"


class Intent(str, Enum):
    BUY_PROPERTY = "BUY_PROPERTY"
    RENT_PROPERTY = "RENT_PROPERTY"
    BUY_LAND = "BUY_LAND"
    SELL_PROPERTY = "SELL_PROPERTY"
    GENERAL_ENQUIRY = "GENERAL_ENQUIRY"


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[Optional[int]] = mapped_column(ForeignKey("customers.id"), nullable=True, index=True)

    # Requirements
    intent: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    property_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    bedrooms: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    budget_min: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    budget_max: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    currency: Mapped[str] = mapped_column(String(10), default="NGN")
    transaction_type: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    timeline: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    additional_requirements: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Qualification
    status: Mapped[str] = mapped_column(String(30), default=LeadStatus.NEW.value, index=True)
    priority: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, index=True)
    score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    # Assignment
    assigned_agent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("sales_agents.id"), nullable=True)

    # Metadata
    source: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self) -> str:
        return f"<Lead id={self.id} status={self.status} priority={self.priority} score={self.score}>"
