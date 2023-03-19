from functools import lru_cache

from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    class Config:
        env_file = ".env"


class Environment(ApiSettings):
    db_main_uri: str = "mysql+pymysql://root:1234@127.0.0.1/projeto_teste"
    environment: str = "LOCAL"
    redis_uri: str = "redis://localhost:6379"


@lru_cache
def get_environment() -> Environment:
    return Environment()
