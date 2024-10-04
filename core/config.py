# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Configurações gerais
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:026373@localhost:5432/zoo'


    class Config:
        case_sesitive = True

settings: Settings = Settings()