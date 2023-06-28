from pydantic import BaseSettings


class ConfigExtractor(BaseSettings):
    db_name: str
    db_port: int
    db_user: str
    db_password: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
