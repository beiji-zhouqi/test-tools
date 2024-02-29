from apps import create_app
from config.env import FASTAPI_APP, FASTAPI_HOST, FASTAPI_PORT

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=FASTAPI_APP, host=FASTAPI_HOST, port=int(FASTAPI_PORT), reload=True)
