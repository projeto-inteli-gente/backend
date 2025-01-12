from sqlalchemy import Column, Integer, String, Float
from db.db import Base

class Region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class State(Base):
    __tablename__ = "state"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    region_id = Column(Integer, nullable=False)

class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    state_id = Column(Integer, nullable=False)
    region_id = Column(Integer, nullable=False)