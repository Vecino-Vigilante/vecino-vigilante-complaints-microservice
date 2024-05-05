from app.domain.models.user_model import UserModel
from app.infrastructure.dto.complaint_request_dto import UserRequestDTO
from app.infrastructure.dto.complaint_response_dto import UserDTO


def user_req_dto_to_user_model(user_dto: UserRequestDTO) -> UserModel:
    return UserModel(
        id=user_dto.id,
        name=None,
        last_name=None,
        email=None,
        profile_image=None
    )
    
def user_model_to_user_dto(user_model: UserModel) -> UserDTO:
    return UserDTO(
        id=user_model.id,
        name=user_model.name,
        last_name=user_model.last_name,
        email=user_model.email,
        profile_image=user_model.profile_image
    )