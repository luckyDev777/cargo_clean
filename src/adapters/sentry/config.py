from dataclasses import dataclass


@dataclass
class SentryConfig:
    host: str
    traces_sample_rate: float = 1.0
