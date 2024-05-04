from uuid import UUID
from app.application.repositories.marker_repository import MarkerRepository
from app.domain.exceptions.conflict_with_existing_resource_exception import ConflictWithExistingResourceException
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.domain.models.marker_model import MarkerModel


class MarkerService:
    def __init__(
        self, 
        marker_repository: MarkerRepository
    ) -> None: self.marker_repository = marker_repository

    def get_marker_by_incident_id(self, incident_id: UUID) -> MarkerModel:
        marker = self.marker_repository.get_marker_by_incident_id(incident_id)
        if not marker:
            raise ResourceNotFoundException
        return marker
    
    def get_all_markers(self) -> MarkerModel:
        return self.marker_repository.get_all_markers()

    def create_marker(self, marker: MarkerModel) -> MarkerModel:
        if self.marker_repository.get_marker_by_incident_id(marker.incident_id):
            raise ConflictWithExistingResourceException
        return self.marker_repository.save_marker(marker)

    def update_marker(self, marker: MarkerModel) -> MarkerModel:
        if not self.marker_repository.get_marker_by_incident_id(marker.incident_id):
            raise ResourceNotFoundException
        return self.marker_repository.save_marker(marker)

    def delete_marker_by_incident_id(self, incident_id: UUID):
        if not self.get_marker_by_incident_id(incident_id):
            raise ResourceNotFoundException
        return self.marker_repository.delete_marker_by_incident_id(incident_id)