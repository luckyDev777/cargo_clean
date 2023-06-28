from fastapi import APIRouter, Depends

from src.business_logic.test import SomeDAO, SomeService
from src.presentation.api.di.providers.services.service_test import (
    service_test_provider,
)

router = APIRouter(tags=["test"])


@router.get(path="/")
async def test_get(
    service: SomeService = Depends(service_test_provider),
) -> dict[str, str]:
    return {"1": service.get()}


# Controller -> SomeService(service_test_provider) ->  some_dao_provider(SomeDAO("hello world"))
