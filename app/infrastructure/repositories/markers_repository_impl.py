from os import getenv
from uuid import UUID, uuid4

import httpx
from app.application.repositories.markers_repository import MarkersRepository
from app.domain.models.location_model import LocationModel


class MarkersRepositoryImpl(MarkersRepository):
    MARKERS_SERVICE_URL = getenv("MARKERS_SERVICE_URL")
    def add_marker(self, marker: LocationModel) -> LocationModel:
        # TODO: Implement the code to request the markers service when it is ready
        pass
    
    def get_marker_by_incident_id(self, incident_id: UUID) -> LocationModel:
        with httpx.Client() as client:
            response = client.get(f"{self.MARKERS_SERVICE_URL}/markers/{incident_id}")
            return LocationModel(**response.json())
        
    def update_marker(self, marker: LocationModel) -> LocationModel:
        # TODO: Request through rabbitmq to update the marker
        pass
        
    def delete_marker(self, incident_id: UUID) -> None:
        # TODO: Request through rabbitmq to delete the marker
        pass