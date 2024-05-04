# Run this file to migrate tables to the database on development

from sqlmodel import SQLModel

from app.infrastructure.configs.sql_database import db_engine

# Import here one by one of the entities that you want to create within the database
from app.infrastructure.entities.marker_entity import Marker

if __name__ == "__main__":
    SQLModel.metadata.create_all(db_engine)
