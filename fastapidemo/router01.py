from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
app01 = APIRouter()

class loginData(BaseModel):
    username:str
    password:str

@app01.get("/username/{name}")
async def get_name(name:Optional[str]):
    if name == "panj":
        return JSONResponse(content={"name":"panj","password":"panj"})
    else:
        return JSONResponse(content="Not Found!!")

