from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from pydantic import ValidationError
from sqlalchemy import Column
import pickle
from pathlib import Path

class User(BaseModel):
    name: str
    id: int
    password: str
    time: Optional[datetime] = None
    friends: List[str] = []


# pydantic基础用法
user_data = {"name": "panj", "id": 123123, "password": "panjie", "time": datetime.today(), "friends": ["pp", "aa"]}
user = User(**user_data)

# print(user.dict())
# print(user.json())
# print(user.friends)
# print(repr(user.time))

# pydantic错误码&错误信息
# try:
#     User(time="asd", friends=["not", []],name= "panj", id= 123123, password="panjie")
# except ValidationError as e:
#     print(e.json()) # 为什么无法识别time/friends字段的错误(如果为数字的字符串类型时)

assert user.__fields_set__ == {"name", "id", "password", "time", "friends"}
print(user.parse_obj(user))
try:
    print(User.parse_raw('{"name": "panj", "id": 123123, "password": "panjie"}'))
except ValidationError as e:
    print(e.json())
aa = pickle.dumps({"name": "panj", "id": 123123, "password": "panjie","time":datetime(2020,1,22)})
m = User.parse_raw(aa,content_type="application/pickle",allow_pickle=True)
print(m)
path = Path("data.json")
path.write_text('{"name": "panj", "id": 123123, "password": "panjie"}')
mm = User.parse_file(path)
print(mm)
print(user.__fields_set__)
fields=user.__fields_set__
# 一般construst一般使用在非法数据里
new_user = User.construct(_fields_set = fields,**user_data)
print(repr(new_user))
bad_user = User.construct(id="123dd")
print(repr(bad_user))