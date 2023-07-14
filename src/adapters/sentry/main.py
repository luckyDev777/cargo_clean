import sentry_sdk

from src.adapters.sentry.config import SentryConfig


def setup_sentry(config: SentryConfig) -> None:
    sentry_sdk.init(
        dsn=config.host,
        traces_sample_rate=config.traces_sample_rate,
    )
