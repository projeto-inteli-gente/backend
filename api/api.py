from fastapi import APIRouter

from api.routers import (
    names_router,
    sociodemography_router
)

api_router = APIRouter()

api_router.include_router(names_router)
api_router.include_router(sociodemography_router)