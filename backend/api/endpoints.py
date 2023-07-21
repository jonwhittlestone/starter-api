
from fastapi import APIRouter

from .health import routers as health_router
from .album import routers as album_router

routers = APIRouter()
routers.include_router(health_router, tags=["health"])
routers.include_router(album_router, tags=["album"])