from fastapi import Depends

from src.business_logic.test import SomeDAO, SomeService
from src.presentation.api.di.main import some_dao_provider


def service_test_provider(dao: SomeDAO = Depends(some_dao_provider)) -> SomeService:
    return SomeService(dao)
