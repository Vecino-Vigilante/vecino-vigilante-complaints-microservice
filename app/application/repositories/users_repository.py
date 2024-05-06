from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.user_model import UserModel


class UsersRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: UUID) -> UserModel:
        pass