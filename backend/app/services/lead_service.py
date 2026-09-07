"""
Lead service - core business logic for leads.
"""

from typing import Optional, List
from sqlalchemy.orm import Session

from app.models.lead import Lead
from app.schemas.lead import LeadCreate, LeadUpdate


class LeadService:
    def __init__(self, db: Session):
        self.db = db

    def create_lead(self, data: LeadCreate) -> Lead:
        lead = Lead(**data.model_dump(exclude_unset=True))
        self.db.add(lead)
        self.db.commit()
        self.db.refresh(lead)
        return lead

    def get_lead(self, lead_id: int) -> Optional[Lead]:
        return self.db.query(Lead).filter(Lead.id == lead_id).first()

    def list_leads(
        self,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> List[Lead]:
        query = self.db.query(Lead)
        if status:
            query = query.filter(Lead.status == status)
        if priority:
            query = query.filter(Lead.priority == priority)
        return query.order_by(Lead.created_at.desc()).offset(offset).limit(limit).all()

    def update_lead(self, lead_id: int, data: LeadUpdate) -> Optional[Lead]:
        lead = self.get_lead(lead_id)
        if not lead:
            return None
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(lead, field, value)
        self.db.commit()
        self.db.refresh(lead)
        return lead
