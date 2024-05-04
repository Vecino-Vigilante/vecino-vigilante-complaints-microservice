from uuid import UUID
from fastapi import APIRouter, HTTPException, status

from app.application.services.marker_service import MarkerService
from app.infrastructure.dto.marker_dto import MarkerDTO
from app.infrastructure.dto.marker_request_dto import MarkerRequestDTO
from app.infrastructure.mappers.marker_mappers import map_marker_model_to_marker_dto
from app.infrastructure.repositories.relational_database_marker_repository_impl import RelationalDatabaseMarkerRepositoryImpl


marker_router = APIRouter()
marker_service = MarkerService(
    marker_repository= RelationalDatabaseMarkerRepositoryImpl()
)

@marker_router.get("/{incident_id}", status_code=status.HTTP_200_OK)
def get_marker_by_incident_id(incident_id: UUID) -> MarkerDTO:

    return map_marker_model_to_marker_dto(
        marker_service.get_marker_by_incident_id(incident_id)
    )
   
