from fastapi import FastAPI

from app.api.routes import router
from app.database.database import Base,engine
from app.models import user_model
from app.models import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NeuroFocus",
    description="AI Powered Interview Platform Based on Trust Score",
    version="1.0.0",
)

app.include_router(router, prefix="/api/v1")