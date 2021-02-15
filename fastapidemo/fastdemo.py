from typing import Optional
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from typing import List
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_home(request: Request):
    return templates.TemplateResponse("filepost.html", {"request": request})


# @app.post("/user/")
# async def up_user_info(request: Request, username: str = Form(...), password: str = Form(...)):
#     print(username)
#     print(password)
#     return templates.TemplateResponse("index.html", {"request": request, "username": username, "password": password})
#

@app.post("/files/")
async def files(request: Request,
                files_list: List[bytes] = File(...),
                files_name: List[UploadFile] = File(...)):
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "file_sizes": [len(file) for file in files_list],
                                       "filename": [file.filename for file in files_name]})


@app.post("/create_file/")
async def create_file(request: Request,
                      file: bytes = File(...),
                      fileb: UploadFile = File(...),
                      notes : str = Form(...)):
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "file_size": len(file),
                                       "notes": notes,
                                       "fileb_content_type": fileb.content_type})


if __name__ == '__main__':
    # 必须是模块名下的app
    uvicorn.run(app='fastdemo:app', host="127.0.0.1", port=8000, reload=True, debug=True)
