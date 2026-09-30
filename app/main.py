from fastapi import FastAPI
from .routes import router

app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")

app.include_router(router)
