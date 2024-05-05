from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from decimal import Decimal

class UserRequestDTO(BaseModel):
    id: UUID
    
class LocationRequestDTO(BaseModel):
    latitude: Decimal
    longitude: Decimal
    direction: str
        
        
class ComplaintRequestDTO(BaseModel):
    type_id: UUID
    description: str
    date: datetime
    resource: str
    user: UserRequestDTO
    location: LocationRequestDTO