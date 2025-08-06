from fastapi import APIRouter
from app.schemas.healthcheck import ServiceStatus
from app.config.logging import logger

router = APIRouter()


@router.get(path="/ping", response_model=ServiceStatus)
async def get_status() -> ServiceStatus:
    logger.info(msg="Service healthy and ready to accept notifications.")
    return ServiceStatus()
