"""Database connection setup (psycopg3 + a connection pool).

You fill in the two TODOs below. Everything else (imports, the pool object) is
scaffolded for you — that part is psycopg_pool API trivia, not the concept.

The two things worth writing cold:
  1. DSN     — the connection string that points the app at the Postgres container.
  2. get_db  — the FastAPI dependency that hands a pooled connection to a route.
"""

from psycopg_pool import ConnectionPool

# ---------------------------------------------------------------------------
# TODO (John) #1 — build the DSN / conninfo string.
#
# Format:  postgresql://<user>:<password>@<host>:<port>/<dbname>
#
#   - user / password / dbname must match the env vars you set in
#     docker-compose.yml (POSTGRES_USER / POSTGRES_PASSWORD / POSTGRES_DB).
#   - host is `localhost` (FastAPI runs on your host, Postgres is in a container
#     with its port published — so from the app's POV it's just localhost).
#   - port is whatever you publish in compose (default Postgres port is 5432).
# ---------------------------------------------------------------------------
DSN = ""  # <-- replace

# The connection pool. Scaffolded for you.
#   - open=False: build the pool now, but don't open connections yet. We open it
#     explicitly in main.py's lifespan on startup (and close it on shutdown).
#   - min_size/max_size: how many connections the pool keeps ready / allows max.
pool = ConnectionPool(conninfo=DSN, min_size=1, max_size=10, open=False)


# ---------------------------------------------------------------------------
# TODO (John) #2 — write the get_db dependency (a *generator* dependency).
#
# Steps:
#   - grab a connection from the pool. psycopg_pool gives you `pool.connection()`,
#     which is a context manager (use a `with` block) that automatically returns
#     the connection to the pool when the block exits.
#   - `yield` that connection to the route (NOT `return`).
#       Why yield? So FastAPI can run the code *after* the yield (the `with`
#       block's cleanup) once the request finishes. A return would close the
#       connection before the route ever uses it.
#
# Your routes consume this with:  def route(..., db = Depends(get_db)):
# ---------------------------------------------------------------------------
def get_db():
    ...  # <-- replace
