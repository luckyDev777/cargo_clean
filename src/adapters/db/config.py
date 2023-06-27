from dataclasses import dataclass


@dataclass
class DBConfig:
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    db_host: str = "localhost"
    db_echo: bool = True

    @property
    def full_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
