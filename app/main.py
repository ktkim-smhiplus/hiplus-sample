from fastapi import FastAPI

from app.routers import health

app = FastAPI(title="hiplus-sample")
app.include_router(health.router)
