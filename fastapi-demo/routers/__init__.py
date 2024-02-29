from fastapi import FastAPI, Depends
from routers.v1 import v1


# 注册路由
def register_router(app: FastAPI):
    # 路由集合
    app.include_router(
        # 版本
        v1,
        # # 路由前缀,版本
        # prefix="/v1",
        # 标签
        # tags=["敏捷开发框架"],
        # 依赖
        # dependencies=[Depends(login_required)],
    )