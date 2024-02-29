# =============================================== 基础配置 =================================================

import os

# 应用名称
FASTAPI_NAME = os.getenv('FASTAPI_NAME', 'FastAPI+EleVue旗舰版')
# 应用版本
FASTAPI_VERSION = os.getenv('FASTAPI_VERSION', 'v2.2.0')
# 应用秘钥
FASTAPI_SECRET_KEY = os.getenv('FASTAPI_SECRET_KEY', 'd67beaf46fbf4f048d2eeb26fd62ea49')
# 应用运行地址
FASTAPI_HOST = os.getenv('FASTAPI_HOST', '127.0.0.1')
# 应用运行端口
FASTAPI_PORT = os.getenv('FASTAPI_PORT', 8000)
# 应用启动文件
FASTAPI_APP = os.getenv('FASTAPI_APP', 'main.py')
# 应用环境变量
FASTAPI_ENV = os.getenv('FASTAPI_ENV', 'development')
# 是否调试模式：是-True,否-False
FASTAPI_DEBUG = (os.getenv('FASTAPI_DEBUG', 'True') == 'True')
# 是否演示模式：是-True,否-False
FASTAPI_DEMO = (os.getenv('FASTAPI_DEMO', 'True') == 'True')