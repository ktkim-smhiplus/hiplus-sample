from fastapi import FastAPI

from app.routers import videos

app = FastAPI(title="hiplus-sample")
app.include_router(videos.router)
