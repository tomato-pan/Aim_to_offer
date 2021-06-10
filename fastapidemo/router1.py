from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates
api_router = APIRouter()
templates = Jinja2Templates(directory="templates")
@api_router.get("/aaa")
async def main(request: Request):
    return templates.TemplateResponse("filepost.html", {"request": request})
