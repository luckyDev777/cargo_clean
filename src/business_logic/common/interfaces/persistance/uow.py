from typing import Protocol


class UoW(Protocol):

    async def commit(self) -> None:
        ...

    async def rollback(self) -> None:
        ...
