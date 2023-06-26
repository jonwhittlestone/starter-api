

from fastapi import APIRouter, status
from fastapi.responses import Response, JSONResponse
from ..config.dyna import settings

routers = APIRouter()


@routers.get(
    "/health",
    response_model=str,
    description="health check",
    name="health",
)
async def health() -> JSONResponse:
    return JSONResponse(content={"current_env": settings.current_env}, 
                    status_code=status.HTTP_200_OK
    )
