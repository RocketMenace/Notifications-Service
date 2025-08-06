from pydantic import BaseModel, Field


class ServiceStatus(BaseModel):
    status: str = Field(default="Ready for accept notifications")
