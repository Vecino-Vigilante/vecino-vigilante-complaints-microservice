from sqlmodel import Session, select
from app.application.repositories.marker_repository import MarkerRepository
from app.domain.models.marker_model import MarkerModel
from app.infrastructure.configs.sql_database import db_engine
from app.infrastructure.entities.marker_entity import Marker
from app.infrastructure.mappers.marker_mappers import map_marker_entity_to_marker_model, map_marker_model_to_marker_entity


class RelationalDatabaseMarkerRepositoryImpl(MarkerRepository):
    def get_marker_by_incident_id(self, incident_id: str) -> MarkerModel | None:
        with Session(db_engine) as session:
            marker_entity = session.exec(
                select(Marker).where(Marker.incident_id == incident_id)
            ).first()

            if marker_entity:
                return map_marker_entity_to_marker_model(marker_entity)
            
    def get_all_markers(self) -> list[MarkerModel]:
        with Session(db_engine) as session:
            marker_entities = session.exec( select(Marker) ).all()

            return [map_marker_entity_to_marker_model(marker) for marker in marker_entities]

    def save_marker(self, marker: MarkerModel) -> MarkerModel:
        with Session(db_engine) as session:
            marker_entity = None

            if marker.marker_id:
                marker_entity = session.exec(
                    select(Marker).where(Marker.marker_id == marker.marker_id)
                ).one()

                marker_entity.incident_id = marker.incident_id
                marker_entity.latitude = marker.latitude
                marker_entity.longitude = marker.longitude
                marker_entity.direction = marker.direction
            else:
                marker_entity = map_marker_model_to_marker_entity(marker)
    
            session.add(marker_entity)
            session.commit()
            session.refresh(marker_entity)

            return map_marker_entity_to_marker_model(marker_entity)
        
    def delete_marker_by_incident_id(self, incident_id: str):
        with Session(db_engine) as session:
            marker_entity = session.exec(
                select(Marker).where(Marker.incident_id == incident_id)
            ).one()

            session.delete(marker_entity)
            session.commit()