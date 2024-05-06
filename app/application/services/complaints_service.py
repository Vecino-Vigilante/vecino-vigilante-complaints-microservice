import base64
import imghdr
from uuid import UUID, uuid4
from app.application.repositories.complaints_repository import ComplaintsRepository
from app.application.repositories.images_repository import ImagesRepository
from app.application.repositories.markers_repository import MarkersRepository
from app.application.repositories.users_repository import UsersRepository
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.domain.models.complaint_model import ComplaintModel
from app.domain.models.location_model import LocationModel


class ComplaintsService:
    def __init__(
        self,
        complaints_repository: ComplaintsRepository,
        images_repository: ImagesRepository,
        users_repository: UsersRepository,
        markers_repository: MarkersRepository,
    ):
        self.complaints_repository = complaints_repository
        self.images_repository = images_repository
        self.users_repository = users_repository
        self.markers_repository = markers_repository
        
    def get_complaints(self, start_date: str | None = None, end_date: str | None = None, type_id: UUID | None = None):
        complaints = self.complaints_repository.get_complaints(start_date, end_date, type_id)
        for complaint in complaints:
            complaint.user = self.get_complaint_user(complaint.user.id)
        return complaints
    
    def get_complaint(self, incident_id: UUID):
        if complaint := self.complaints_repository.get_complaint(incident_id):
            return complaint
        
        raise ResourceNotFoundException
    
    def get_complaint_by_incident_id(self, incident_id: UUID):
        complaint = self.get_complaint(incident_id)
        complaint.user = self.get_complaint_user(complaint.user.id)
        return complaint

    def get_filepath(self, path: str, file_bytes: bytes):
        extension = imghdr.what(None, h=file_bytes)
        return f"{path}.{extension}" if extension else path

    def upload_complaint_image(self, base64_image: str, complaint_id: UUID):
        file_bytes = base64.b64decode(base64_image)
        filename = str(complaint_id).replace("-", "")
        relative_path = self.get_filepath(filename, file_bytes)
        return self.images_repository.upload_object(file_bytes, relative_path)
    
    def create_complaint(self, complaint: ComplaintModel, base64_image: str | None = None):
        if base64_image:
            complaint.id = uuid4()
            complaint.image_url = self.upload_complaint_image(base64_image, complaint.id)
        new_complaint = self.complaints_repository.add_complaint(complaint)
        complaint.location.incident_id = new_complaint.id
        new_complaint.user = self.get_complaint_user(new_complaint.user.id)
        self.create_marker(complaint.location)
        return new_complaint
    
    def create_marker(self, marker: LocationModel):
        return self.markers_repository.add_marker(marker)
    
    def get_marker_by_incident_id(self, incident_id: UUID):
        return self.markers_repository.get_marker_by_incident_id(incident_id)
    
    def get_complaint_user(self, user_id: UUID):
        return self.users_repository.get_user(user_id)
    
    def update_complaint(self, complaint: ComplaintModel, base64_image: str | None = None):
        if base64_image:
            complaint.image_url = self.upload_complaint_image(base64_image, complaint.id)
        updated_complaint = self.complaints_repository.update_complaint(complaint)
        updated_complaint.user = self.get_complaint_user(updated_complaint.user.id)
        self.markers_repository.update_marker(complaint.location)
        return updated_complaint
    
    def delete_complaint(self, incident_id: UUID):
        if self.get_complaint(incident_id):
            self.complaints_repository.delete_complaint(incident_id)
            self.markers_repository.delete_marker(incident_id)
            return