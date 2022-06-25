import sqlalchemy as sa

from app.db.base import TableBase, metadata


position_table = sa.Table(
    "position",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("created_on", sa.DateTime, default=sa.func.now()),
    sa.Column("updated_on", sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),
    # Actual Columns
    sa.Column("company", sa.String),
    sa.Column("title", sa.String),
    sa.Column("location", sa.String),
    sa.Column("level", sa.String),
    sa.Column("expected_salary", sa.Integer),
    sa.Column("description", sa.String),
)


_position = TableBase(position_table)
