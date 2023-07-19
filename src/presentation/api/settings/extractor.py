from pydantic_settings import BaseSettings


class ConfigExtractor(BaseSettings):
    db_name: str
    db_port: int
    db_user: str
    db_password: str

    sentry_host: str

    cache_host: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
