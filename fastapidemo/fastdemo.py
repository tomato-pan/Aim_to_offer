from typing import Optional
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from typing import List
import uvicorn
from fastapidemo.router01 import app01
from fastapidemo.router1 import api_router
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/user/")
async def up_user_info(request: Request,
                       username: str = Form(...),
                       password: str = Form(...)
                       ):
    print(username)
    print(password)
    return templates.TemplateResponse("index.html",
                                      {
                                          "request": request,
                                          "username": username
                                      })


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


# @app.post("/files/")
# async def files(request: Request,
#                 files_list: List[bytes] = File(...),
#                 files_name: List[UploadFile] = File(...), ):
#     return templates.TemplateResponse("index1.html",
#                                       {"request": request,
#                                        "file_sizes": [len(file) for file in files_list],
#                                        "filenames": [file.filename for file in files_name]
#                                        }
#                                       )
#
#
# @app.post("/create_file/")
# async def create_file(request: Request,
#                       file: bytes = File(...),
#                       fileb: UploadFile = File(...),
#                       notes: str = Form(...)):
#     return templates.TemplateResponse("index1.html",
#                                       {"request": request,
#                                        "file_size": len(file),
#                                        "notes": notes,
#                                        "fileb_content_type": fileb.content_type
#                                        }
#                                       )


# @app.get("/")
# async def main(request: Request):
#     return templates.TemplateResponse("filepost.html", {"request": request})
app.include_router(api_router)

if __name__ == '__main__':
    # 必须是模块名下的app
    uvicorn.run(app='fastdemo:app', host="127.0.0.1", port=8000, reload=True, debug=True)
