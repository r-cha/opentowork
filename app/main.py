from fastapi import FastAPI

from app.routers import root
from app.db.base import metadata, engine


app = FastAPI()
app.include_router(root.router)
metadata.create_all(engine)
