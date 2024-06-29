import psycopg
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:567234@localhost:5432/hw03"


@contextmanager
def create_connection():
    conn = psycopg.connect(SQLALCHEMY_DATABASE_URL)
    yield conn
    # conn.rollback()
    conn.close()
