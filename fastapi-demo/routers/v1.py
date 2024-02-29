from fastapi import APIRouter
from apps.views import root

# 创建路由
v1 = APIRouter
# 系统主页
v1.include_router(root.router, prefix="", tags=["系统主页"])