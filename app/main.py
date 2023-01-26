from fastapi import FastAPI

from app.routers import root
from app.db import engine, SQLModel


app = FastAPI()
app.include_router(root.router)
SQLModel.metadata.create_all(engine)
