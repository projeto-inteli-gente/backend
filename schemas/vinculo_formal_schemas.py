from sqlalchemy import Column, Integer, String, Float
from db.db import Base

class BrazilVinculoFormal(Base):
    __tablename__ = "brazil_porcentagem_vinculo_formal"
    year = Column(Integer, primary_key=True)
    porcentagem_vinculo_formal = Column(Float, nullable=False)

class RegionVinculoFormal(Base):
    __tablename__ = "region_porcentagem_vinculo_formal"
    region_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    porcentagem_vinculo_formal = Column(Float, nullable=False)

class StateVinculoFormal(Base):
    __tablename__ = "state_porcentagem_vinculo_formal"
    state_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    porcentagem_vinculo_formal = Column(Float, nullable=False)

class CityVinculoFormal(Base):
    __tablename__ = "city_porcentagem_vinculo_formal"
    city_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    porcentagem_vinculo_formal = Column(Float, nullable=False)