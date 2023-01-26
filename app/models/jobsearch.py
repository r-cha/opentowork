from datetime import datetime

from pydantic import BaseModel, Field

from app.models.base import DBModel
from app.models.position import Position


class JobSearchCreate(BaseModel):
    desired_title: str = Field(
        ..., description="The applicant's dream job title for this search."
    )
    desired_salary: int | None = Field(
        None, description="An estimate of the desired salary of this applicant."
    )


class JobSearch(JobSearchCreate, DBModel):
    pass


class CompletedJobSearch(BaseModel):
    search: JobSearch
    position: Position = Field(
        ..., description="The position accepted at the end of this job search"
    )
    completed_on: datetime
