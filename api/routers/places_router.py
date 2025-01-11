from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db.db import get_db
import models
import schemas
from typing import List, Optional

places_router = APIRouter(prefix="/places")

@places_router.get("/regions", response_model=List[models.Region])
async def get_regions(db: Session = Depends(get_db)):
    regions = db.execute(select(schemas.Region)).scalars().all()
    return regions

@places_router.get("/states", response_model=List[models.State])
async def get_states_from_regions(region: Optional[str] = None, db: Session = Depends(get_db)):
    
    if region:
        states = db.execute(
            select(schemas.State).where(
                schemas.State.region == region.lower()
            )
        ).scalars().all()
    else:
        states = db.execute(
            select(schemas.State)
        ).scalars().all()
    
    return states

@places_router.get("/cities", response_model=List[models.City])
async def get_cities(state: Optional[str] = None, region: Optional[str] = None, db: Session = Depends(get_db)):

    if state:
        cities = db.execute(
            select(schemas.City).where(
                schemas.City.state == state.upper()
            )
        ).scalars().all()
    elif region:
        cities = db.execute(
            select(schemas.City).where(
                schemas.City.region == region.lower()
            )
        ).scalars().all()
    else:
        cities = db.execute(
            select(schemas.City)
        ).scalars().all()

    return cities