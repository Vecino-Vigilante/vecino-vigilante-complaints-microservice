from uuid import UUID
from app.domain.models.marker_model import MarkerModel


class MarkerRepository:
    def get_marker_by_incident_id(self, incident_id: UUID) -> MarkerModel:
        raise NotImplementedError(
            "get_marker_by_incident_id hasn't been implemented yet."
        )
    
    def get_all_markers(self) -> MarkerModel:
        raise NotImplementedError(
            "get_markers_by_incident_id hasn't been implemented yet."
        )
        
    def save_marker(self, marker: MarkerModel) -> MarkerModel:
        raise NotImplementedError(
            "save_marker hasn't been implemented yet."
        )
    
    def delete_marker_by_incident_id(self, incident_id: UUID):
        raise NotImplementedError(
            "delete_marker_by_incident_id hasn't been implemented yet."
        )