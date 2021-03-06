import uvicorn
from fastapi import FastAPI, Query
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class Name(str, Enum):
    a = "z0"
    b = "z1"
    c = "z2"


# 查询参数和字符串校验&添加正则表达式, 必需值则 None->...
@app.get("/items1/")
async def items1(q: Optional[str] = Query(None, min_length=3, max_length=50, regex=r"^a")):
    res = {"message": fake_items_db}
    if q:
        res.update({"q": q})
    return res


# 查询参数列表 / 多个值, 别名：alias Query(None, alias="qq")
@app.get("/items2/")
async def items2(q: Optional[List[str]] = Query(["foo", "bar"])):
    query = {"message": q}
    return query


# 弃用参数
@app.get("/items3/")
async def read_items(
        q: Optional[str] = Query(
            None,
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            regex="^fixedquery$",
            deprecated=True,  # 弃用参数标识
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/")
async def read():
    return {
        "message": 123
    }


# BaseModel参数
@app.post("/item/")
async def create_item(item: Item):
    print(item.dict())
    return item


# BaseModel参数
@app.put("/items/{item_id}")
async def read_user_item(
        item_id: int, item: Item, q: Optional[str] = None
):
    item = {"item_id": item_id, **item.dict()}
    if q:
        item.update({"q": q})
    print(item)
    return item


# 查询参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# 查询参数含默认参数
@app.get("/ab/")
async def ab(A: int = 0, B: int = 20):
    return {
        "message": B + A
    }


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/a/{name}")
async def get_name(name: Name):
    if name == Name.a:
        return {"name": name, "message": name + " no!"}
    if name == Name.b:
        return {"name": name, "message": name + " no no!"}
    return {"name": name, "message": name + " yes!"}


if __name__ == '__main__':
    # 必须是模块名下的app
    uvicorn.run(app='fastdemo1:app', host="127.0.0.1", port=8000, reload=True, debug=True)
