from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel

class Marker(SQLModel, table=True):
    marker_id: UUID | None = Field(default=uuid4(), primary_key=True)
    incident_id: UUID 
    direction: str
    latitude: float
    longitude: float
    