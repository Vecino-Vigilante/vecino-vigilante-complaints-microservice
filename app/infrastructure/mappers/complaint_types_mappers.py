from app.domain.models.complaint_type import ComplaintTypeModel
from app.infrastructure.dto.complaint_response_dto import TypeDTO
from app.infrastructure.entities.complaint_types import ComplaintTypes


def map_complaint_type_entity_to_complaint_type_model(complaint_type: ComplaintTypes) -> ComplaintTypeModel:
    return ComplaintTypeModel(
        id=complaint_type.id,
        name=complaint_type.name,
    )
    
def map_complaint_type_model_to_complaint_type_dto(complaint_type: ComplaintTypeModel) -> TypeDTO:
    return TypeDTO(
        id=complaint_type.id,
        name=complaint_type.name,
    )