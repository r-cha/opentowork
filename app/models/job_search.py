from datetime import datetime
from enum import Enum

from pydantic import BaseModel, root_validator

from app.models.base import DBModel


class Salary(BaseModel):
    lower_bound: int | None
    upper_bound: int | None
    absolute: int | None

    @root_validator
    def validate_salary(cls, values):
        # TODO: If a single arg int is provided instead of kwargs, treat it as `absolute`
        if all(v is None for v in values.values()):
            raise ValueError("At least one salary value must be provided")
        return values


class Position(BaseModel):
    company: str  # TODO: Track companies as a model of their own
    title: str
    location: str  # or strong type
    level: str  # or enum
    expected_salary: Salary | None
    description: str


class EventKind(str, Enum):
    # TODO: Figure out what I intend for these sort of hierarchical Enums
    INTERVIEW = "INTERVIEW"  # [technical, phone screen, executive, culture]
    ASSESSMENT = "ASSESSMENT"
    EMAIL = "EMAIL"


class InterviewEvent(BaseModel):
    kind: EventKind
    position: Position
    date: datetime
    contact: str  # phone number, zoom link, etc


class ApplicationMaterials(BaseModel):
    resume: str  # or file
    cover_letter: str  # or file
    notes: str


class ApplicationProcess(BaseModel):
    position: Position
    status: str  # enum
    updated_on: datetime
    events: list[InterviewEvent]
    materials: ApplicationMaterials


class JobSearchCreate(BaseModel):
    desired_title: str
    desired_salary: int | None  # TODO: Allow to be Salary Model
    # TODO: What else to include when starting a new search? e.g. location...
    # Actually may end up similar to Position model


class JobSearch(JobSearchCreate, DBModel):
    pass


class CompletedJobSearch(BaseModel):
    search: JobSearch
    position: Position
    completed_on: datetime
