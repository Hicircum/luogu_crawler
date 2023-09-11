import uvicorn

from module.api import router


if __name__ == "__main__":
    host = "0.0.0.0"
    uvicorn.run(
        router,
        host=host,
    )
