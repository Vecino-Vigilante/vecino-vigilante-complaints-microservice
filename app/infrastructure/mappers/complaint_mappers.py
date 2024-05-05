from app.domain.models.complaint_model import ComplaintModel
from app.domain.models.complaint_type import ComplaintTypeModel
from app.domain.models.user_model import UserModel
from app.infrastructure.dto.complaint_request_dto import ComplaintRequestDTO
from app.infrastructure.dto.complaint_response_dto import ComplaintDTO, TypeDTO
from app.infrastructure.entities.complaint_entity import Complaint
from app.infrastructure.mappers.complaint_types_mappers import map_complaint_type_model_to_complaint_type_dto
from app.infrastructure.mappers.location_mappers import (
    location_model_to_location_dto,
    location_req_dto_to_location_model,
)
from app.infrastructure.mappers.user_mappers import (
    user_model_to_user_dto,
    user_req_dto_to_user_model,
)


def map_complaint_req_dto_to_complaint_model(
    complaint_dto: ComplaintRequestDTO,
) -> ComplaintModel:
    return ComplaintModel(
        id=None,
        type = ComplaintTypeModel(id=complaint_dto.type_id, name=None),
        description=complaint_dto.description,
        date=complaint_dto.date,
        image_url=None,
        user=user_req_dto_to_user_model(complaint_dto.user),
        location=location_req_dto_to_location_model(complaint_dto.location),
    )


def map_complaint_model_to_complaint_entity(
    complaint_model: ComplaintModel,
) -> Complaint:
    return Complaint(
        id=complaint_model.id,
        type_id=complaint_model.type.id,
        user_id=complaint_model.user.id,
        description=complaint_model.description,
        date=complaint_model.date,
        image_url=complaint_model.image_url,
    )


def map_complaint_entity_to_complaint_model(complaint: Complaint) -> ComplaintModel:
    return ComplaintModel(
        id=complaint.id,
        type=ComplaintTypeModel(id=complaint.type_id, name=None),
        description=complaint.description,
        date=complaint.date,
        image_url=complaint.image_url,
        user=UserModel(
            id=complaint.user_id,
            name=None,
            last_name=None,
            email=None,
            profile_image=None,
        ),
        location=None,
    )


def map_complaint_model_to_complaint_dto(
    complaint_model: ComplaintModel,
) -> ComplaintDTO:
    return ComplaintDTO(
        id=complaint_model.id,
        type = map_complaint_type_model_to_complaint_type_dto(complaint_model.type),
        description=complaint_model.description,
        date=complaint_model.date,
        image_url=complaint_model.image_url,
        user=user_model_to_user_dto(complaint_model.user),
        location=None
    )
