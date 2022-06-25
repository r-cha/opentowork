from enum import Enum

from pydantic import BaseModel

from app.models.base import DBModel


class PositionLevel(str, Enum):
    INTERNSHIP = "INTERNSHIP"
    ENTRY_LEVEL = "ENTRY_LEVEL"
    JUNIOR = "JUNIOR"
    MID = "MID"
    SENIOR = "SENIOR"
    STAFF = "STAFF"
    EXECUTIVE = "EXECUTIVE"
    # and more


class PositionCreate(BaseModel):
    company: str  # TODO: Track companies as a model of their own
    title: str
    location: str  # or strong type?
    level: str
    expected_salary: int
    description: str


class Position(PositionCreate, DBModel):
    pass
