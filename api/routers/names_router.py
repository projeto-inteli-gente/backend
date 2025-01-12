from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db.db import get_db
import models
import schemas
from typing import List, Optional

names_router = APIRouter(prefix="/names")

@names_router.get("/regions", response_model=List[models.NameResponse])
async def get_regions_names(
        db: Session = Depends(get_db)
    ):

    regions = db.execute(
        select(
            schemas.Region.id, 
            schemas.Region.name
        )
    ).fetchall()

    return regions

@names_router.get("/states", response_model=List[models.NameResponse])
async def get_states_names(
        region_id: Optional[int] = None, 
        db: Session = Depends(get_db)
    ):
    
    if region_id:
        states = db.execute(
            select(
                schemas.State.id, 
                schemas.State.name
            ).where(
                schemas.State.region_id == region_id
            )
        ).fetchall()
    else:
        states = db.execute(
            select(
                schemas.State.id, 
                schemas.State.name
            )
        ).fetchall()
    
    return states

@names_router.get("/cities", response_model=List[models.NameResponse])
async def get_cities_names(
        state_id: Optional[int] = None, 
        region_id: Optional[int] = None, 
        db: Session = Depends(get_db)
    ):

    if state_id:
        cities = db.execute(
            select(
                schemas.City.id, 
                schemas.City.name
            ).where(
                schemas.City.state_id == state_id
            )
        ).fetchall()
    elif region_id:
        cities = db.execute(
            select(
                schemas.City.id, 
                schemas.City.name)
            .where(
                schemas.City.region_id == region_id
            )
        ).fetchall()
    else:
        cities = db.execute(
            select(
                schemas.City.id, 
                schemas.City.name
            )
        ).fetchall()

    return cities