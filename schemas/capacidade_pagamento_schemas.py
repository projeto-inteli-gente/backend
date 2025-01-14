from sqlalchemy import Column, Integer, String, Float
from db.db import Base

class BrazilCapag(Base):
    __tablename__ = "brazil_capacidade_pagamento"
    year = Column(Integer, primary_key=True)
    capacidade_pagamento = Column(Float, nullable=False)

class RegionCapag(Base):
    __tablename__ = "region_capacidade_pagamento"
    region_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    capacidade_pagamento = Column(Float, nullable=False)

class StateCapag(Base):
    __tablename__ = "state_capacidade_pagamento"
    state_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    capacidade_pagamento = Column(Float, nullable=False)

class CityCapag(Base):
    __tablename__ = "city_capacidade_pagamento"
    city_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    capacidade_pagamento = Column(Float, nullable=False)