from datetime import datetime
from typing import Dict, Any, Type

from pydantic import ValidationError
from pydantic.dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel, Field,PositiveInt

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
# print(MainModel.schema_json(indent=2))

# class Model(BaseModel):
#     # Here both constraints will be applied and the schema
#     # will be generated correctly
#     foo: int = Field(..., gt=0, lt=10)
#
# print(Model.schema())
class Person(BaseModel):
    name: str
    age: int

    class Config:
        # schema_extra = {
        #     'examples': [
        #         {
        #             'name': 'John Doe',
        #             'age': 25,
        #         }
        #     ]
        # }
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type['Person']) -> None:
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)


print(Person.schema_json(indent=2))