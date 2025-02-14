from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db.db import get_db
import models
import schemas
from typing import List, Optional
from intelligentedb.indicators import read_data as dbrd
import pandas as pd

names_router = APIRouter(prefix="/names")

@names_router.get("/regions",response_model=List[models.RegionResponse])
async def get_regions_names():
    response = dbrd.get_city_dimension_values()
    regions = response[['nome_regiao_nacional']].drop_duplicates().reset_index(drop=True)

    return [models.RegionResponse(name=region_name) for region_name in regions['nome_regiao_nacional']]

@names_router.get("/states",response_model=List[models.StateResponse])
async def get_states_names(
        nome_regiao: Optional[str] = None
    ):
    
    response = dbrd.get_city_dimension_values()

    if nome_regiao:
        states = response.loc[response['nome_regiao_nacional'] == nome_regiao][['nome_uf','sigla_uf']].drop_duplicates().reset_index(drop=True)
    else:
        states = response[['nome_uf','sigla_uf']].drop_duplicates().reset_index(drop=True)

    return [models.StateResponse(nome_uf=item['nome_uf'],sigla_uf=item['sigla_uf']) for item in states.to_dict(orient='records')]

@names_router.get("/cities")
async def get_cities_names(
        sigla_uf: Optional[str] = None, 
        nome_regiao: Optional[str] = None, 
    ):

    response = dbrd.get_city_dimension_values()

    if sigla_uf:
        cities = response.loc[response['sigla_uf'] == sigla_uf]\
            [['nome_municipio','municipio_id']].reset_index()
    elif nome_regiao:
        cities = response.loc[response['nome_regiao_nacional'] == nome_regiao]\
            [['nome_municipio','municipio_id']].reset_index(drop=True)
    else:
        cities = response[['nome_municipio','municipio_id']].reset_index(drop=True)

    return [models.CityResponse(nome_municipio=item['nome_municipio'],municipio_id=item['municipio_id']) for item in cities.to_dict(orient='records')]