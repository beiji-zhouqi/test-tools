from fastapi import FastAPI
from routers import register_router


def create_app():
    app = FastAPI(title="fastapi-demo",
                  description="fastapi",
                  version="v1")
    register_router(app)
    return app
