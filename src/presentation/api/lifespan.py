from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.asd = "HELLOWEASDASDASD"

    yield

    del app.state.asd
