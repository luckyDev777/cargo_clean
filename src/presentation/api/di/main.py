from fastapi import FastAPI

from src.business_logic.test import SomeDAO

from ..settings.config import Config


def some_dao_provider() -> SomeDAO:
    raise NotImplementedError


def setup_di(app: FastAPI, config: Config) -> None:
    some_dao = SomeDAO("hello world", 5)

    app.dependency_overrides[some_dao_provider] = lambda: some_dao
