from dataclasses import dataclass


@dataclass
class DBConfig:
    port: int
    user: str
    password: str
    name: str
    host: str
    echo: bool = False

    @property
    def full_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
