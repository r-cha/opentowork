from datetime import datetime
from fastapi import APIRouter

from app.models.job_search import JobSearch, JobSearchCreate

router = APIRouter(prefix="/search", tags=["Job Searches"])


@router.post("/", response_model=JobSearch)
def create_search(new_search: JobSearchCreate) -> JobSearch:
    # TODO: Add to datastore
    now = datetime.now()
    faked = JobSearch(**new_search.dict(), id=1, created_on=now, updated_on=now)
    return faked


@router.get("/", response_model=list[JobSearch])
def list_searches() -> list[JobSearch]:
    raise NotImplementedError()


@router.get("/{search_id}", response_model=JobSearch)
def get_search(search_id: int) -> JobSearch:
    raise NotImplementedError()
