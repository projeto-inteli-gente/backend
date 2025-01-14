from sqlalchemy import Column, Integer, String, Float
from db.db import Base

class BrazilPIB(Base):
    __tablename__ = "brazil_pib_per_capita"
    year = Column(Integer, primary_key=True)
    pib_per_capita = Column(Float, nullable=False)

class RegionPIB(Base):
    __tablename__ = "region_pib_per_capita"
    region_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    pib_per_capita = Column(Float, nullable=False)

class StatePIB(Base):
    __tablename__ = "state_pib_per_capita"
    state_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    pib_per_capita = Column(Float, nullable=False)

class CityPIB(Base):
    __tablename__ = "city_pib_per_capita"
    city_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    pib_per_capita = Column(Float, nullable=False)