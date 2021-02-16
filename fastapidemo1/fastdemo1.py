import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read():
    return {
        "message": 123
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == '__main__':
    # 必须是模块名下的app
    uvicorn.run(app='fastdemo1:app', host="127.0.0.1", port=8000, reload=True, debug=True)
