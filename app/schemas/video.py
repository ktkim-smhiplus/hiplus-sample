from pydantic import BaseModel


class VideoCreateRequest(BaseModel):
    title: str


class VideoCreateResponse(BaseModel):
    title: str
