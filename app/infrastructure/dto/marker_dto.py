from uuid import UUID
from pydantic import BaseModel


class MarkerDTO(BaseModel):
    marker_id: UUID
    incident_id: UUID
    direction: str
    latitude: float
    longitude: float 