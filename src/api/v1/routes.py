from fastapi import APIRouter

from src.api.v1.healthcheck.handlers import router as healthcheck_router

api_router = APIRouter()
api_router.include_router(healthcheck_router, prefix="/healthcheck")
