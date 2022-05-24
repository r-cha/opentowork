from fastapi import APIRouter

from app.models.job_search import JobSearch

router = APIRouter(prefix="/search")


@router.get("/", response_model=list[JobSearch])
def list_searches() -> list[JobSearch]:
    raise NotImplementedError()


@router.get("/{search_id}", response_model=JobSearch)
def get_search(search_id: int) -> JobSearch:
    raise NotImplementedError()