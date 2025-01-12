from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db.db import get_db
import models
import schemas
from typing import List, Optional

sociodemography_router = APIRouter(prefix="/sociodemography")

@sociodemography_router.get("/region/{region_id}", response_model=models.Region)
async def get_region_sociodemography(
        region_id: int,
        db: Session = Depends(get_db)
    ):

    region_sociodemography = db.execute(
        select(
            schemas.Region
        ).where(
            schemas.Region.id == region_id
        )
    ).scalars().first()

    return region_sociodemography

@sociodemography_router.get("/state/{state_id}", response_model=models.State)
async def get_state_sociodemography(
        state_id: int,
        db: Session = Depends(get_db)
    ):

    state_sociodemography = db.execute(
        select(
            schemas.State
        ).where(
            schemas.State.id == state_id
        )
    ).scalars().first()

    return state_sociodemography

@sociodemography_router.get("/city/{city_id}", response_model=models.City)
async def get_city_sociodemography(
        city_id: int,
        db: Session = Depends(get_db)
    ):

    city_sociodemography = db.execute(
        select(
            schemas.City
        ).where(
            schemas.City.id == city_id
        )
    ).scalars().first()

    return city_sociodemography