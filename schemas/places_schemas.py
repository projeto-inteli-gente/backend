from sqlalchemy import Column, Integer, String
from db.db import Base

class Region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class State(Base):
    __tablename__ = "state"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)

class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    region = Column(String, nullable=False)