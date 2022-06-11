import sys
from datetime import datetime
from typing import Type, Callable
from random import random, randint
from uuid import uuid4

from pydantic import BaseModel


def get_uuid() -> str:
    return str(uuid4())


type_default_map: dict[type, Callable] = {
    str: get_uuid,
    int: lambda: randint(0, sys.maxsize),
    float: random,
    datetime: datetime.now,
}


def generate_random(model_class: Type[BaseModel]) -> dict:
    fields = model_class.__fields__

    random_model = {
        name: type_default_map.get(field.type_, lambda: generate_random(field.type_))()
        for name, field in fields.items()
    }

    return random_model
