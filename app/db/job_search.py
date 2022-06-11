import sqlalchemy as sa

from app.db.base import TableBase, metadata


job_search_table = sa.Table(
    "job_search",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("created_on", sa.DateTime, default=sa.func.now()),
    sa.Column("updated_on", sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),
    # Actual Columns
    sa.Column("desired_title", sa.String),
    sa.Column("desired_salary", sa.Integer),
)


_job_search = TableBase(job_search_table)
