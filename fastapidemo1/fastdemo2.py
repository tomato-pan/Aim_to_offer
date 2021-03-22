from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from sqlalchemy import Column

class User(BaseModel):
    name: str
    id: int
    password: str
    time: datetime


user_data = {"name": "panj", "id": 123123, "password": "panjie", "time": datetime.today()}
user = User(**user_data)

print(user.dict())
print(user.json())
print(user.parse_obj(user))
