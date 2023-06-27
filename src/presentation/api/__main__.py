import asyncio

from .main import build_app, run_api
from .settings.config import load_config


async def main() -> None:
    config = load_config()

    app = build_app(config=config)

    await run_api(app=app, api_config=config.api)


if __name__ == "__main__":
    asyncio.run(main())
