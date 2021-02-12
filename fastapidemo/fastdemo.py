from typing import Optional
from fastapi import FastAPI,Form
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_home(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})


@app.post("/user/")
async def up_user_info(request: Request, username: str = Form(...), password: str = Form(...)):
    print(username)
    print(password)
    return templates.TemplateResponse("index.html",{"request": request, "username": username, "password": password})


if __name__ == '__main__':
    # 必须是模块名下的app
    uvicorn.run(app='fastdemo:app', host="127.0.0.1", port=8000, reload=True, debug=True)
