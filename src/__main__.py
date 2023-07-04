import uvicorn

from src.presentation.api.settings.config import load_config

if __name__ == "__main__":
    config = load_config()

    uvicorn.run(
        app="src.presentation.api.__main__:main",
        host=config.api.host,
        port=config.api.port,
        reload=True,
        factory=True,
    )
