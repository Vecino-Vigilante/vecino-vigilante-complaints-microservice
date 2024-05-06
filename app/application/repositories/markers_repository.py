
from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.location_model import LocationModel


class MarkersRepository(ABC):
    @abstractmethod
    def add_marker(self, marker: LocationModel) -> LocationModel:
        pass
    
    @abstractmethod
    def get_marker_by_incident_id(self, incident_id: UUID) -> LocationModel:
        pass
    
    @abstractmethod
    def delete_marker(self, incident_id: UUID) -> None:
        pass