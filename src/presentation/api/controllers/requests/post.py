from pydantic import BaseModel


class UpdatePostRequest(BaseModel):
    name: str | None = None
