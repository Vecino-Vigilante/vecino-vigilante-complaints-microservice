from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4

from app.infrastructure.entities.complaint_types import ComplaintTypes


class Complaint(SQLModel, table=True):
    id: UUID = Field(default=uuid4(), primary_key=True)
    type_id: UUID = Field(foreign_key="complaint_types.id")
    user_id: UUID
    description: str
    date: datetime
    image_url: str
    incident_type: "ComplaintTypes" = Relationship(back_populates="complaints")