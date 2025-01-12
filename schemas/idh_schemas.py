from sqlalchemy import Column, Integer, String, Float
from db.db import Base

class BrazilIDH(Base):
    __tablename__ = "brazil_idh"
    year = Column(Integer, primary_key=True)
    idh = Column(Float, nullable=False)

class RegionIDH(Base):
    __tablename__ = "region_idh"
    region_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    idh = Column(Float, nullable=False)

class StateIDH(Base):
    __tablename__ = "state_idh"
    state_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    idh = Column(Float, nullable=False)

class CityIDH(Base):
    __tablename__ = "city_idh"
    city_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    idh = Column(Float, nullable=False)