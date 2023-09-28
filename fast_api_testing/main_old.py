from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from enum import Enum
import uvicorn
import os


app = FastAPI()

# 简单示例
# @app.get("/")
# async def root():
#     return {"message": "This is running..."}

# @app.get('/favicon.ico')
# async def favicon():
#     file_name = "favicon.ico"
#     file_path = os.path.join(app.root_path, "static", file_name)
#     return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

# @app.get('/items/{item_id}')
# async def items(item_id: int):
#     return {"item_id": item_id}

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# websocket 示例
# from websocket import manager

# @app.websocket("/ws/{user}")
# async def websocket_endpoint(websocket: WebSocket, user: str):

#     await manager.connect(websocket)

#     await manager.broadcast(f"用户{user}进入聊天室")

#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_personal_message(f"你说了: {data}", websocket)
#             await manager.broadcast(f"用户:{user} 说: {data}")

#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"用户-{user}-离开")


# 请求体
from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     print(item_dict)
#     print(type(item_dict))
#     return item

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

from typing import Union
from fastapi import Query

@app.get("/items6")
async def read_items6(q: Union[str, None] = Query(default=None, min_length=3, max_length=50)):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True)