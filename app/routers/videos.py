from fastapi import APIRouter

from app.schemas.video import VideoCreateRequest, VideoCreateResponse
from app.services.video_title import normalize_title

router = APIRouter(prefix="/videos", tags=["videos"])


@router.post("", response_model=VideoCreateResponse)
def create_video(request: VideoCreateRequest) -> VideoCreateResponse:
    return VideoCreateResponse(title=normalize_title(request.title))
