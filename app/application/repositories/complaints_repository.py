from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.complaint_model import ComplaintModel


class ComplaintsRepository(ABC):
    @abstractmethod
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        pass
    
    @abstractmethod
    def get_complaints(self) -> list[ComplaintModel]:
        pass

    @abstractmethod
    def get_complaint(self, incident_id: UUID) -> ComplaintModel:
        pass
    
    @abstractmethod
    def delete_complaint(self, incident_id: UUID) -> None:
        pass