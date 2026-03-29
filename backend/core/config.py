from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api" 
    DEBUG: bool = False

    DATABASE_URL: str

    ALLOWED_ORIGIN: str = ""

    OPENAI_API_KEY: str

    @field_validator('ALLOWED_ORIGIN')
    # convert comma-separated string to list of strings
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

    class Config: 
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()