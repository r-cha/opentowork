from fastapi import APIRouter

from app.routers import jobsearch, position

router = APIRouter()


@router.get("/")
def get_info():
    return {"message": "Hello"}


# router.include_router(jobsearch.router)
router.include_router(position.router)
