# from fastapi import APIRouter, status

# from app.models.jobsearch import JobSearch, JobSearchCreate

# router = APIRouter(prefix="/search", tags=["Job Searches"])


# @router.post("/", response_model=JobSearch)
# async def create_search(new_search: JobSearchCreate) -> JobSearch:
#     return await searches.create(new_search)


# @router.get("/", response_model=list[JobSearch])
# async def list_searches() -> list[JobSearch]:
#     return await searches.list()


# @router.get("/{search_id}", response_model=JobSearch)
# async def get_search(search_id: int) -> JobSearch:
#     return await searches.get(search_id)


# @router.delete("/{search_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_search(search_id: int):
#     await searches.delete(search_id)
