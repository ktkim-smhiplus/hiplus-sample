from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    time: str
