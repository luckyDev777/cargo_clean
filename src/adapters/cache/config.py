from dataclasses import dataclass


@dataclass
class CacheConfig:
    host: str
    port: int = 6379
