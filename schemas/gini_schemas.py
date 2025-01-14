from sqlalchemy import Column, Integer, String, Float
from db.db import Base

class BrazilGini(Base):
    __tablename__ = "brazil_gini"
    year = Column(Integer, primary_key=True)
    gini = Column(Float, nullable=False)

class RegionGini(Base):
    __tablename__ = "region_gini"
    region_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    gini = Column(Float, nullable=False)

class StateGini(Base):
    __tablename__ = "state_gini"
    state_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    gini = Column(Float, nullable=False)

class CityGini(Base):
    __tablename__ = "city_gini"
    city_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    gini = Column(Float, nullable=False)