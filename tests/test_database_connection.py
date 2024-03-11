from sqlalchemy import text
from app.database import ENGINE


def test_db_connection():
    with ENGINE.begin() as conn:
        query = text("SELECT 1 AS result")
        row = conn.execute(query).mappings().fetchone()
        assert row.result == 1
