from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class UserDTO(BaseModel):
    id: UUID
    name: str
    last_name: str
    email: str
    profile_image: str
    
class LocationDTO(BaseModel):
    id: UUID
    incident_id: UUID
    latitude: float
    longitude: float
    direction: str
    
class TypeDTO(BaseModel):
    id: UUID
    name: str

class ComplaintDTO(BaseModel):
    id: UUID
    type: TypeDTO
    description: str
    date: datetime
    image_url: str
    user: UserDTO | None
    # location: LocationDTO
