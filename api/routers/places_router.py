from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from db.db import get_db
import models
import schemas
from typing import List

places_router = APIRouter(prefix="/locais")

@places_router.get("/regions", response_model=List[models.Region])
async def get_regions(db: Session = Depends(get_db)):
    regions = db.execute(select(schemas.Region)).scalars().all()
    return regions


@places_router.get("/states", response_model=List[models.State])
async def get_states(db: Session = Depends(get_db)):
    states = db.execute(select(schemas.State)).scalars().all()
    return states

@places_router.get("/states/{region}", response_model=List[models.State])
async def get_states_from_regions(region: str, db: Session = Depends(get_db)):
    states = db.execute(select(schemas.State).where(schemas.State.region == region.lower())).scalars().all()
    return states