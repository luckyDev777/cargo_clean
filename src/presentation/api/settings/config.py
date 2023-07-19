from dataclasses import dataclass

from src.adapters.cache.config import CacheConfig
from src.adapters.db.config import DBConfig
from src.adapters.sentry.config import SentryConfig
from .extractor import ConfigExtractor


@dataclass
class APIConfig:
    host: str = "0.0.0.0"
    port: int = 8001


@dataclass
class Config:
    api: APIConfig
    db: DBConfig
    sentry: SentryConfig
    cache: CacheConfig


def load_config() -> Config:
    extractor = ConfigExtractor()

    return Config(
        api=APIConfig(),
        db=DBConfig(
            db_port=extractor.db_port,
            db_password=extractor.db_password,
            db_user=extractor.db_user,
            db_name=extractor.db_name
        ),
        sentry=SentryConfig(
            host=extractor.sentry_host
        ),
        cache=CacheConfig(
            host=extractor.cache_host
        )
    )
