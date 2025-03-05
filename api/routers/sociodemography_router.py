from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db.db import get_db
import db.utils as dbutils
import models
from typing import List, Optional
from intelligentedb.indicators import read_data  as dbrd
import pandas as pd

sociodemography_router = APIRouter(prefix="/sociodemography")


"""
    IDH Routers
"""

@sociodemography_router.get("/idh", response_model=List[models.IndicatorResponse])
async def get_brazil_idh():

    df = dbutils.get_brazil_mean_indicator('índice de desenvolvimento humano do município (idh-m)')

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]



@sociodemography_router.get("/idh/region/{nome_regiao}", response_model=List[models.IndicatorResponse])
async def get_region_idh(
        nome_regiao: str,
    ):

    df = dbutils.get_region_mean_indicator('índice de desenvolvimento humano do município (idh-m)',nome_regiao)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/idh/state/{sigla_uf}", response_model=List[models.IndicatorResponse])
async def get_state_idh(
        sigla_uf: str
    ):

    df = dbutils.get_state_mean_indicator('índice de desenvolvimento humano do município (idh-m)',sigla_uf)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/idh/city/{id_municipio}", response_model=List[models.IndicatorResponse])
async def get_city_idh(
        id_municipio: int,
    ):

    df = dbutils.get_city_indicator('índice de desenvolvimento humano do município (idh-m)',id_municipio)
    return [models.IndicatorResponse(year=item['ano'],value=item['valor']) for item in df.to_dict(orient='records')]


"""
    Coeficiente de Gini Routers
"""


@sociodemography_router.get("/gini", response_model=List[models.IndicatorResponse])
async def get_brazil_gini():

    df = dbutils.get_brazil_mean_indicator('índice de gini da renda domiciliar per capita')

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]


@sociodemography_router.get("/gini/region/{nome_regiao}", response_model=List[models.IndicatorResponse])
async def get_region_gini(
        nome_regiao: str
    ):

    df = dbutils.get_region_mean_indicator('índice de gini da renda domiciliar per capita',nome_regiao)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]


@sociodemography_router.get("/gini/state/{sigla_uf}", response_model=List[models.IndicatorResponse])
async def get_state_gini(
        sigla_uf: str,
    ):

    df = dbutils.get_state_mean_indicator('índice de gini da renda domiciliar per capita',sigla_uf)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]



@sociodemography_router.get("/gini/city/{municipio_id}", response_model=List[models.IndicatorResponse])
async def get_city_gini(
        municipio_id: int
    ):

    df = dbutils.get_city_indicator('índice de gini da renda domiciliar per capita',municipio_id)
    return [models.IndicatorResponse(year=item['ano'],value=item['valor']) for item in df.to_dict(orient='records')]

"""
    PIB per capita Routers
"""


@sociodemography_router.get("/pib_per_capita", response_model=List[models.IndicatorResponse])
async def get_brazil_pib():

    df = dbutils.get_brazil_mean_indicator('pib per capita')

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/pib_per_capita/region/{nome_regiao}", response_model=List[models.IndicatorResponse])
async def get_region_pib(
        nome_regiao: str,
    ):

    df = dbutils.get_region_mean_indicator('pib per capita',nome_regiao)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/pib_per_capita/state/{sigla_uf}", response_model=List[models.IndicatorResponse])
async def get_state_pib(
        sigla_uf: str,
    ):

    df = dbutils.get_state_mean_indicator('pib per capita',sigla_uf)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/pib_per_capita/city/{municipio_id}", response_model=List[models.IndicatorResponse])
async def get_city_pib(
        municipio_id: int,
    ):

    df = dbutils.get_city_indicator('pib per capita',municipio_id)
    return [models.IndicatorResponse(year=item['ano'],value=item['valor']) for item in df.to_dict(orient='records')]


"""
    Vinculo Formal Routers
"""


@sociodemography_router.get("/porcentagem_vinculo_formal", response_model=List[models.IndicatorResponse])
async def get_brazil_vinculo_formal(
        db: Session = Depends(get_db)
    ):

    df = dbutils.get_brazil_mean_indicator('população ocupada com vínculo formal')
    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/porcentagem_vinculo_formal/region/{nome_regiao}", response_model=List[models.IndicatorResponse])
async def get_region_vinculo_formal(
        nome_regiao: str,
    ):

    df = dbutils.get_region_mean_indicator('população ocupada com vínculo formal',nome_regiao)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/porcentagem_vinculo_formal/state/{sigla_uf}", response_model=List[models.IndicatorResponse])
async def get_state_vinculo_formal(
        sigla_uf: str,
    ):

    df = dbutils.get_state_mean_indicator('população ocupada com vínculo formal',sigla_uf)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/porcentagem_vinculo_formal/city/{municipio_id}", response_model=List[models.IndicatorResponse])
async def get_city_vinculo_formal(
        municipio_id: int,
    ):

    df = dbutils.get_city_indicator('população ocupada com vínculo formal',municipio_id)
    return [models.IndicatorResponse(year=item['ano'],value=item['valor']) for item in df.to_dict(orient='records')]

"""
    Capacidade de Pagamento Routers
"""


@sociodemography_router.get("/capacidade_pagamento", response_model=List[models.IndicatorResponse])
async def get_brazil_capacidade_pagamento():

    
    df = dbutils.get_brazil_mean_indicator('capacidade de pagamento dos municípios (capag)')
    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/capacidade_pagamento/region/{nome_regiao}", response_model=List[models.IndicatorResponse])
async def get_region_capacidade_pagamento(
        nome_regiao: str,
    ):

    df = dbutils.get_region_mean_indicator('capacidade de pagamento dos municípios (capag)',nome_regiao)
    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/capacidade_pagamento/state/{sigla_uf}", response_model=List[models.IndicatorResponse])
async def get_state_capacidade_pagamento(
        sigla_uf: str
    ):

    df = dbutils.get_state_mean_indicator('capacidade de pagamento dos municípios (capag)',sigla_uf)

    return [models.IndicatorResponse(year=ano,value=valor) for ano,valor in df.itertuples()]

@sociodemography_router.get("/capacidade_pagamento/city/{municipio_id}", response_model=List[models.IndicatorResponse])
async def get_city_capacidade_pagamento(
        municipio_id: int,
    ):

    df = dbutils.get_city_indicator('capacidade de pagamento dos municípios (capag)',municipio_id)
    return [models.IndicatorResponse(year=item['ano'],value=item['valor']) for item in df.to_dict(orient='records')]