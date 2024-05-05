from uuid import UUID
from app.application.services.complaints_service import ComplaintsService
from app.infrastructure.dto.complaint_request_dto import ComplaintRequestDTO
from app.infrastructure.mappers.complaint_mappers import (
    map_complaint_model_to_complaint_dto,
    map_complaint_req_dto_to_complaint_model,
)
from app.infrastructure.repositories.awss3_images_repository_impl import (
    AWSS3ImagesRepositoryImpl,
)
from app.infrastructure.repositories.markers_repository_impl import (
    MarkersRepositoryImpl,
)
from app.infrastructure.repositories.relational_db_complaints_repository_impl import (
    RelationalDBComplaintsRepositoryImpl,
)
from fastapi import APIRouter, status

from app.infrastructure.repositories.users_repository_impl import UsersRepositoryImpl

complaints_router = APIRouter()
complaints_service = ComplaintsService(
    complaints_repository=RelationalDBComplaintsRepositoryImpl(),
    images_repository=AWSS3ImagesRepositoryImpl(),
    users_repository=UsersRepositoryImpl(),
    markers_repository=MarkersRepositoryImpl(),
)


@complaints_router.get("")
def get_complaints():
    return [
        map_complaint_model_to_complaint_dto(complaint)
        for complaint in complaints_service.get_complaints()
    ]

@complaints_router.get("/{incident_id}")
def get_complaint_by_incident_id(incident_id: UUID):
    return map_complaint_model_to_complaint_dto(
        complaints_service.get_complaint_by_incident_id(incident_id)
    )

@complaints_router.post("", status_code=status.HTTP_201_CREATED)
def create_complaint(complaint_request: ComplaintRequestDTO):
    new_complaint = complaints_service.create_complaint(
        map_complaint_req_dto_to_complaint_model(complaint_request),
        complaint_request.resource,
    )
    return map_complaint_model_to_complaint_dto(new_complaint)
