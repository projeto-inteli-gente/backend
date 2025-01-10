from fastapi import APIRouter

from api.routers import (
    places_router
)

api_router = APIRouter()

api_router.include_router(places_router)