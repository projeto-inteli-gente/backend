from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db.db import get_db
import models
import schemas
from typing import List, Optional

sociodemography_router = APIRouter(prefix="/sociodemography")


"""
    IDH Routers
"""

@sociodemography_router.get("/idh", response_model=List[models.IDHResponse])
async def get_brazil_idh(
        db: Session = Depends(get_db)
    ):

    brazil_idh = db.execute(
        select(
            schemas.BrazilIDH.year,
            schemas.BrazilIDH.idh
        )
    ).fetchall()

    return brazil_idh

@sociodemography_router.get("/idh/region/{region_id}", response_model=List[models.IDHResponse])
async def get_region_idh(
        region_id: int,
        db: Session = Depends(get_db)
    ):

    region_idh = db.execute(
        select(
            schemas.RegionIDH.year,
            schemas.RegionIDH.idh
        ).where(
            schemas.RegionIDH.region_id == region_id
        )
    ).fetchall()

    return region_idh

@sociodemography_router.get("/idh/state/{state_id}", response_model=List[models.IDHResponse])
async def get_state_idh(
        state_id: int,
        db: Session = Depends(get_db)
    ):

    state_idh = db.execute(
        select(
            schemas.StateIDH.year,
            schemas.StateIDH.idh
        ).where(
            schemas.StateIDH.state_id == state_id
        )
    ).fetchall()

    return state_idh

@sociodemography_router.get("/idh/city/{city_id}", response_model=List[models.IDHResponse])
async def get_city_idh(
        city_id: int,
        db: Session = Depends(get_db)
    ):

    city_idh = db.execute(
        select(
            schemas.CityIDH.year,
            schemas.CityIDH.idh
        ).where(
            schemas.CityIDH.city_id == city_id
        )
    ).fetchall()

    return city_idh


"""
    Coeficiente de Gini Routers
"""


@sociodemography_router.get("/gini", response_model=List[models.GiniResponse])
async def get_brazil_gini(
        db: Session = Depends(get_db)
    ):

    brazil_gini = db.execute(
        select(
            schemas.BrazilGini.year,
            schemas.BrazilGini.gini
        )
    ).fetchall()

    return brazil_gini

@sociodemography_router.get("/gini/region/{region_id}", response_model=List[models.GiniResponse])
async def get_region_gini(
        region_id: int,
        db: Session = Depends(get_db)
    ):

    region_gini = db.execute(
        select(
            schemas.RegionGini.year,
            schemas.RegionGini.gini
        ).where(
            schemas.RegionGini.region_id == region_id
        )
    ).fetchall()

    return region_gini

@sociodemography_router.get("/gini/state/{state_id}", response_model=List[models.GiniResponse])
async def get_state_gini(
        state_id: int,
        db: Session = Depends(get_db)
    ):

    state_gini = db.execute(
        select(
            schemas.StateGini.year,
            schemas.StateGini.gini
        ).where(
            schemas.StateGini.state_id == state_id
        )
    ).fetchall()

    return state_gini

@sociodemography_router.get("/gini/city/{city_id}", response_model=List[models.GiniResponse])
async def get_city_gini(
        city_id: int,
        db: Session = Depends(get_db)
    ):

    city_gini = db.execute(
        select(
            schemas.CityGini.year,
            schemas.CityGini.gini
        ).where(
            schemas.CityGini.city_id == city_id
        )
    ).fetchall()

    return city_gini


"""
    PIB per capita Routers
"""


@sociodemography_router.get("/pib_per_capita", response_model=List[models.PIBResponse])
async def get_brazil_pib(
        db: Session = Depends(get_db)
    ):

    brazil_pib = db.execute(
        select(
            schemas.BrazilPIB.year,
            schemas.BrazilPIB.pib_per_capita
        )
    ).fetchall()

    return brazil_pib

@sociodemography_router.get("/pib_per_capita/region/{region_id}", response_model=List[models.PIBResponse])
async def get_region_pib(
        region_id: int,
        db: Session = Depends(get_db)
    ):

    region_pib = db.execute(
        select(
            schemas.RegionPIB.year,
            schemas.RegionPIB.pib_per_capita
        ).where(
            schemas.RegionPIB.region_id == region_id
        )
    ).fetchall()

    return region_pib

@sociodemography_router.get("/pib_per_capita/state/{state_id}", response_model=List[models.PIBResponse])
async def get_state_pib(
        state_id: int,
        db: Session = Depends(get_db)
    ):

    state_pib = db.execute(
        select(
            schemas.StatePIB.year,
            schemas.StatePIB.pib_per_capita
        ).where(
            schemas.StatePIB.state_id == state_id
        )
    ).fetchall()

    return state_pib

@sociodemography_router.get("/pib_per_capita/city/{city_id}", response_model=List[models.PIBResponse])
async def get_city_pib(
        city_id: int,
        db: Session = Depends(get_db)
    ):

    city_pib = db.execute(
        select(
            schemas.CityPIB.year,
            schemas.CityPIB.pib_per_capita
        ).where(
            schemas.CityPIB.city_id == city_id
        )
    ).fetchall()

    return city_pib


"""
    Vinculo Formal Routers
"""


@sociodemography_router.get("/porcentagem_vinculo_formal", response_model=List[models.VinculoFormalResponse])
async def get_brazil_vinculo_formal(
        db: Session = Depends(get_db)
    ):

    brazil_vinculo_formal = db.execute(
        select(
            schemas.BrazilVinculoFormal.year,
            schemas.BrazilVinculoFormal.porcentagem_vinculo_formal
        )
    ).fetchall()

    return brazil_vinculo_formal

@sociodemography_router.get("/porcentagem_vinculo_formal/region/{region_id}", response_model=List[models.VinculoFormalResponse])
async def get_region_vinculo_formal(
        region_id: int,
        db: Session = Depends(get_db)
    ):

    region_vinculo_formal = db.execute(
        select(
            schemas.RegionVinculoFormal.year,
            schemas.RegionVinculoFormal.porcentagem_vinculo_formal
        ).where(
            schemas.RegionVinculoFormal.region_id == region_id
        )
    ).fetchall()

    return region_vinculo_formal

@sociodemography_router.get("/porcentagem_vinculo_formal/state/{state_id}", response_model=List[models.VinculoFormalResponse])
async def get_state_vinculo_formal(
        state_id: int,
        db: Session = Depends(get_db)
    ):

    state_vinculo_formal = db.execute(
        select(
            schemas.StateVinculoFormal.year,
            schemas.StateVinculoFormal.porcentagem_vinculo_formal
        ).where(
            schemas.StateVinculoFormal.state_id == state_id
        )
    ).fetchall()

    return state_vinculo_formal

@sociodemography_router.get("/porcentagem_vinculo_formal/city/{city_id}", response_model=List[models.VinculoFormalResponse])
async def get_city_vinculo_formal(
        city_id: int,
        db: Session = Depends(get_db)
    ):

    city_vinculo_formal = db.execute(
        select(
            schemas.CityVinculoFormal.year,
            schemas.CityVinculoFormal.porcentagem_vinculo_formal
        ).where(
            schemas.CityVinculoFormal.city_id == city_id
        )
    ).fetchall()

    return city_vinculo_formal