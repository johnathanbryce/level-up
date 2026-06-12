"""Database connection setup (psycopg3 + a connection pool).

You fill in the two TODOs below. Everything else (imports, the pool object) is
scaffolded for you — that part is psycopg_pool API trivia, not the concept.

The two things worth writing cold:
  1. DSN     — the connection string that points the app at the Postgres container.
  2. get_db  — the FastAPI dependency that hands a pooled connection to a route.
"""

from psycopg_pool import ConnectionPool

DSN = "postgresql://user:postgres@localhost:5432/pgdb"

# The connection pool.
#   - open=False: build the pool now, but don't open connections yet. We open it
#     explicitly in main.py's lifespan on startup (and close it on shutdown).
#   - min_size/max_size: how many connections the pool keeps ready / allows max.
pool = ConnectionPool(conninfo=DSN, min_size=1, max_size=10, open=False)


def get_db():
    with pool.connection() as conn:
        yield conn
