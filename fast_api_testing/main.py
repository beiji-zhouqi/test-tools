from apps import create_app
from config.env import FASTAPI_HOST, FASTAPI_PORT
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return ("Hello, FASTAPI")


# app = create_app()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host=FASTAPI_HOST, port=int(FASTAPI_PORT), reload=True)
