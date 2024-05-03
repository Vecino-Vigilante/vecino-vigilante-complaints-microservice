from os import getenv
from uuid import UUID
import httpx
from app.application.repositories.users_repository import UsersRepository
from app.domain.models.user_model import UserModel


class UsersRepositoryImpl(UsersRepository):
    USERS_SERVICE_URL = getenv("USERS_SERVICE_URL")
    def get_user(self, user_id: UUID):
        return UserModel(id=user_id, name="John", last_name="Doe", email="johndoe@gmail.com", profile_image="https://example.com/image.jpg")
        # TODO: Uncomment the code below when the users service is ready
        # with httpx.Client() as client:
        #     response = client.get(f"{self.USERS_SERVICE_URL}/users/{user_id}")
        #     return UserModel(**response.json())