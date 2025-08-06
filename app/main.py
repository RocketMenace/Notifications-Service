from fastapi import FastAPI
from app.config.settings import settings
from app.api.v1 import healthcheck

app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    debug=settings.debug,
    description="Scalable notifications service",
    docs_url="/docs",
    redoc_url="/redoc",
    root_path="/api",
)

app.include_router(healthcheck.router)
