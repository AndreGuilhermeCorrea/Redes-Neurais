# api/v1/api.py
from fastapi import APIRouter

from api.v1.endpoints import zoo

api_router = APIRouter()
api_router.include_router(zoo.router)
