"""FastAPI app for the drillhole CRUD rep.

The pool lifecycle (open on startup, close on shutdown) is wired for you via
`lifespan` — that's psycopg_pool trivia and ties to db.py. Everything below the
marker is yours to write. See README.md for the full spec.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from db import pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.open()          # open the connection pool on startup
    yield
    pool.close()         # close it on shutdown


app = FastAPI(lifespan=lifespan, title="Drillhole CRUD")


# ===========================================================================
# YOUR WORK STARTS HERE (see README.md for the full spec):
#
#   - CORS middleware (recall it cold — no hand-holding this time)
#
#   - GET    /drillholes        list, with query params:
#                                 status (filter), sort, order, limit, offset
#   - GET    /drillholes/{id}   single record, 404 if not found
#   - POST   /drillholes        create, return 201 + the created record
#   - PUT    /drillholes/{id}   update, 404 if not found
#   - DELETE /drillholes/{id}   delete, return 204
#
# Use raw psycopg: db.cursor() -> cur.execute(sql, params) -> fetch -> commit.
# Parameterize with %s placeholders (NEVER f-strings — SQL injection).
# ===========================================================================
