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
from app.infrastructure.mappers.complaint_types_mappers import (
    map_complaint_type_entity_to_complaint_type_model,
)


class RelationalDBComplaintsRepositoryImpl(ComplaintsRepository):
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        with Session(db_engine) as session:
            complaint_entity = map_complaint_model_to_complaint_entity(complaint)
            session.add(complaint_entity)
            session.commit()
            session.refresh(complaint_entity)
        return self.get_complaint(complaint_entity.id)

    def get_complaints(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        type_id: UUID | None = None,
    ) -> list[ComplaintModel]:
        with Session(db_engine) as session:
            complaints = []
            query = select(Complaint, ComplaintTypes).join(ComplaintTypes, isouter=True)
            if start_date:
                query = query.where(Complaint.date >= start_date)
            if end_date:
                query = query.where(Complaint.date <= end_date)
            if type_id:
                query = query.where(Complaint.type_id == type_id)
            result = session.exec(query)
            for complaint, complaint_type in result:
                complaint_model = map_complaint_entity_to_complaint_model(complaint)
                complaint_model.type = (
                    map_complaint_type_entity_to_complaint_type_model(complaint_type)
                )
                complaints.append(complaint_model)
            return complaints

    def get_complaint(self, incident_id: UUID) -> ComplaintModel:
        with Session(db_engine) as session:
            complaint = session.get(Complaint, incident_id)
            if not complaint:
                return None
            complaint_model = map_complaint_entity_to_complaint_model(complaint)
            complaint_model.type = map_complaint_type_entity_to_complaint_type_model(
                complaint.incident_type
            )
        return complaint_model

    def update_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        with Session(db_engine) as session:
            with Session(db_engine) as session:
                complaint_entity = session.get(Complaint, complaint.id)
                complaint_entity.type_id = complaint.type.id
                complaint_entity.description = complaint.description
                complaint_entity.date = complaint.date
                complaint_entity.image_url = (
                    complaint.image_url
                    if complaint.image_url
                    else complaint_entity.image_url
                )
                session.add(complaint_entity)
                session.commit()
                session.refresh(complaint_entity)
                return self.get_complaint(complaint_entity.id)

    def delete_complaint(self, incident_id: UUID) -> None:
        with Session(db_engine) as session:
            complaint = session.exec(
                select(Complaint).where(Complaint.id == incident_id)
            ).one()
            session.delete(complaint)
            session.commit()
