from datetime import datetime
from uuid import UUID

from app.domain.models.location_model import LocationModel
from app.domain.models.user_model import UserModel


class ComplaintModel:
    def __init__(
        self,
        id: UUID | None,
        type_id: UUID,
        type: str | None,
        description: str,
        date: datetime,
        image_url: str | None,
        user: UserModel,
        location: LocationModel | None,
    ):
        self.id = id
        self.type_id = type_id
        self.type = type
        self.description = description
        self.date = date
        self.image_url = image_url
        self.user = user
        self.location = location