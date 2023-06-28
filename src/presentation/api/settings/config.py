from dataclasses import dataclass

from src.adapters.db.config import DBConfig

from .extractor import ConfigExtractor


@dataclass
class APIConfig:
    host: str = "0.0.0.0"
    port: int = 8000


@dataclass
class Config:
    api: APIConfig
    db: DBConfig


def load_config() -> Config:
    extractor = ConfigExtractor()

    return Config(
        api=APIConfig(),
        db=DBConfig(
            db_port=extractor.db_port,
            db_password=extractor.db_password,
            db_user=extractor.db_user,
            db_name=extractor.db_name,
        ),
    )
