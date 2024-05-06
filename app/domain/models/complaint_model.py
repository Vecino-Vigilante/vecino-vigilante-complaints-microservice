from datetime import datetime
from uuid import UUID

from app.domain.models.complaint_type import ComplaintTypeModel
from app.domain.models.location_model import LocationModel
from app.domain.models.user_model import UserModel


class ComplaintModel:
    def __init__(
        self,
        id: UUID | None,
        type: ComplaintTypeModel,
        description: str,
        date: datetime,
        image_url: str | None,
        user: UserModel | None,
        location: LocationModel | None,
    ):
        self.id = id
        self.type = type
        self.description = description
        self.date = date
        self.image_url = image_url
        self.user = user
        self.location = location
