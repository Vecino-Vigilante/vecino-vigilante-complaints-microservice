from uuid import UUID
from fastapi import APIRouter, HTTPException, status

from app.application.services.marker_service import MarkerService
from app.domain.exceptions.conflict_with_existing_resource_exception import ConflictWithExistingResourceException
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.infrastructure.dto.marker_dto import MarkerDTO
from app.infrastructure.dto.marker_request_dto import MarkerRequestDTO
from app.infrastructure.mappers.marker_mappers import map_marker_dto_to_marker_model, map_marker_model_to_marker_dto, map_marker_request_dto_to_marker_model
from app.infrastructure.repositories.relational_database_marker_repository_impl import RelationalDatabaseMarkerRepositoryImpl


marker_router = APIRouter()
marker_service = MarkerService(
    marker_repository= RelationalDatabaseMarkerRepositoryImpl()
)

@marker_router.get("/{incident_id}", status_code=status.HTTP_200_OK)
def get_marker_by_incident_id(incident_id: UUID) -> MarkerDTO:
    try:
        return map_marker_model_to_marker_dto(
            marker_service.get_marker_by_incident_id(incident_id)
        )
    except ResourceNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Marker not found",
        ) 

@marker_router.get("", status_code=status.HTTP_200_OK)
def get_all_markers() -> list[MarkerDTO]:
    return [
        map_marker_model_to_marker_dto(marker)
        for marker in marker_service.get_all_markers()
    ]
    
@marker_router.post("", status_code=status.HTTP_201_CREATED)
def create_marker(marker_request_dto: MarkerRequestDTO) -> MarkerDTO:
    try:
        return map_marker_model_to_marker_dto(
            marker_service.create_marker(
                marker=map_marker_request_dto_to_marker_model(marker_request_dto)
            )
        )
    except ConflictWithExistingResourceException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Incident marker already exists",
        )

@marker_router.put("", status_code=status.HTTP_200_OK)
def edit_marker_information(marker_dto: MarkerDTO) -> MarkerDTO:
    try:
        return map_marker_model_to_marker_dto(
            marker_service.update_marker(
                marker=map_marker_dto_to_marker_model(marker_dto),
            )
        )
    except ResourceNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Marker not found",
        )
    
@marker_router.delete("/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_marker(incident_id: UUID) -> None:
    try:
        marker_service.delete_marker_by_incident_id(incident_id)
    except ResourceNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Marker not found",
        )