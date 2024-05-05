from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.infrastructure.entities.complaint_entity import Complaint

class ComplaintTypes(SQLModel, table=True):
    __tablename__ = "complaint_types"
    id: UUID = Field(default=uuid4(), primary_key=True)
    name: str
    complaints: list["Complaint"] = Relationship(back_populates="incident_type")