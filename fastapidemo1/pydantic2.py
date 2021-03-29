from datetime import datetime
from pydantic import ValidationError
from pydantic.dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel, Field


class MyConfig:
    max_anystr_length = 10
    validate_assignment = True
    error_msg_templates = {
        'value_error.any_str.max_length': 'max_length:{limit_value}',
    }


@dataclass(config=MyConfig)
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None


user = User(id='42111111111', signup_ts='2032-06-21T12:00')  # 初始化不会报错？初始化时并没有设置超长
try:
    user.name = 'x' * 11
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    name
      max_length:10 (type=value_error.any_str.max_length; limit_value=10)
   """


class FooBar(BaseModel):
    count: int
    size: float = None


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class MainModel(BaseModel):
    foobar: FooBar = Field(...)
    gender: Gender = Field(None, alias="Gender")
    snap: int = Field(
        42, title="The Snap!", description="this is the value of snap", gt=30, lt=50
    )

    class Config:
        title = "main"
print(MainModel.schema_json(indent=2))