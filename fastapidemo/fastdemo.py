from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_home():
    return {"message": "Welcome to tomato's home!"}


if __name__ == '__main__':
    # 必须是模块名下的app
    uvicorn.run(app='fastdemo:app', host="127.0.0.1", port=8000, reload=True, debug=True)
