from app.domain.models.location_model import LocationModel
from app.infrastructure.dto.complaint_request_dto import LocationRequestDTO
from app.infrastructure.dto.complaint_response_dto import LocationDTO



def location_req_dto_to_location_model(location_dto: LocationRequestDTO) -> LocationModel:
    return LocationModel(
        id=None,
        incident_id=None,
        latitude=location_dto.latitude,
        longitude=location_dto.longitude,
        direction=location_dto.direction
    )
    
def location_model_to_location_dto(location_model: LocationModel) -> LocationDTO:
    return LocationDTO(
        id=location_model.id,
        incident_id=location_model.incident_id,
        latitude=location_model.latitude,
        longitude=location_model.longitude,
        direction=location_model.direction
    )