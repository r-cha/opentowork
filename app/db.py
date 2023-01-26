import databases

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio.engine import create_async_engine

from sqlmodel import SQLModel  # noqa
from app import models  # noqa

# TODO: postgres >>>>
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
# DATABASE_URL = "postgresql+asyncpg://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})

async def get_session():
    async with AsyncSession(engine) as session:
        yield session
        await session.commit()
