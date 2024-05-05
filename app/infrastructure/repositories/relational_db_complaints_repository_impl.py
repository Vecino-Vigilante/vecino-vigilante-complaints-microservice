from uuid import UUID
from sqlmodel import Session, select
from app.infrastructure.configs.sql_database import db_engine
from app.application.repositories.complaints_repository import ComplaintsRepository
from app.domain.models.complaint_model import ComplaintModel
from app.infrastructure.entities.complaint_entity import Complaint
from app.infrastructure.entities.complaint_types import ComplaintTypes
from app.infrastructure.mappers.complaint_mappers import (
    map_complaint_entity_to_complaint_model,
    map_complaint_model_to_complaint_entity,
)
from app.infrastructure.mappers.complaint_types_mappers import map_complaint_type_entity_to_complaint_type_model


class RelationalDBComplaintsRepositoryImpl(ComplaintsRepository):
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        with Session(db_engine) as session:
            complaint_entity = map_complaint_model_to_complaint_entity(complaint)
            session.add(complaint_entity)
            session.commit()
            session.refresh(complaint_entity)
        return self.get_complaint(complaint_entity.id)
    
    def get_complaints(self) -> list[ComplaintModel]:
        with Session(db_engine) as session:
            complaints = []
            result = session.exec(select(Complaint, ComplaintTypes).join(ComplaintTypes, isouter=True))
            for complaint, complaint_type in result:
                complaint_model = map_complaint_entity_to_complaint_model(complaint)
                complaint_model.type = map_complaint_type_entity_to_complaint_type_model(complaint_type)
                complaints.append(complaint_model)
            return complaints

    def get_complaint(self, incident_id: UUID) -> ComplaintModel:
        with Session(db_engine) as session:
            complaint = session.get(Complaint, incident_id)
            complaint_model = map_complaint_entity_to_complaint_model(complaint)
            complaint_model.type = map_complaint_type_entity_to_complaint_type_model(complaint.incident_type)
        return complaint_model