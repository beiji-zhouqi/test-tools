from fastapi import FastAPI
from routers import register_router


def create_app():
    app = FastAPI(
        debug=True,
        title="FastAPI",
        version="v1",
    )
    # 注册路由
    register_router(app)
    return app