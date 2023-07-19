from redis.asyncio.client import Redis

from src.adapters.cache.config import CacheConfig


def create_cache(config: CacheConfig) -> Redis:
    return Redis(host=config.host, port=config.port)
