from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class UserRequestDTO(BaseModel):
    id: UUID
    
class LocationRequestDTO(BaseModel):
    latitude: float
    longitude: float
    direction: str
        
        
class ComplaintRequestDTO(BaseModel):
    type_id: UUID
    description: str
    date: datetime
    resource: str | None
    user: UserRequestDTO
    location: LocationRequestDTO
    
class ComplaintUpdateDTO(BaseModel):
    id: UUID
    type_id: UUID
    description: str
    date: datetime
    resource: str | None