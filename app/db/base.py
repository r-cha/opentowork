import databases

import sqlalchemy as sa

# TODO: postgres >>>>
DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sa.MetaData()

engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


class TableBase:
    def __init__(self, table: sa.Table):
        self.table = table

    async def create(self, model):
        insert = self.table.insert().values(
            **model.dict()
        )  # TODO: .returning(self.table)
        id_ = await database.execute(insert)
        return await self.get(id_)

    async def list(self):
        query = self.table.select()
        return await database.fetch_all(query)

    async def get(self, id_: int):
        query = self.table.select().where(self.table.c.id == id_)
        all_ = await database.fetch_all(query)
        return all_[0]
