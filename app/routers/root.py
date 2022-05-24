from fastapi import APIRouter

from app.routers import job_search

router = APIRouter()


@router.get("/")
def get_info():
    return {"message": "Hello"}

router.include_router(job_search.router)