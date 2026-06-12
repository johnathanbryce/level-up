"""FastAPI app for the drillhole CRUD rep.

The pool lifecycle (open on startup, close on shutdown) is wired for you via
`lifespan` — that's psycopg_pool trivia and ties to db.py.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from psycopg.rows import dict_row
from db import pool, get_db
from models import Drillhole, DrillholeCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.open()  # open the connection pool on startup
    yield
    pool.close()  # close it on shutdown


app = FastAPI(lifespan=lifespan, title="Drillhole CRUD")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()


@router.get("/drillholes", response_model=list[Drillhole], status_code=200)
def list_drillholes(
    status: str | None = None,  # optional filter
    sort: str = "logged_at",  # default sort column
    order: str = "desc",  # default direction
    limit: int = 20,
    offset: int = 0,
    db=Depends(get_db),
):
    with db.cursor(row_factory=dict_row) as cur:
        query = "SELECT * FROM drillholes"
        params = []
        if status:
            query += " WHERE status = %s"
            params.append(status)

        ALLOWED_SORT = {"logged_at", "grade", "depth_m", "hole_id", "id"}
        if sort not in ALLOWED_SORT:
            sort = "logged_at"
        order = "asc" if order.lower() == "asc" else "desc"

        query += f" ORDER BY {sort} {order}"
        query += " LIMIT %s OFFSET %s"
        params.extend([limit, offset])
        cur.execute(query, params)

        rows = cur.fetchall()

    return rows


@router.get("/drillholes/{id}", response_model=Drillhole, status_code=200)
def get_drillhole(id: int, db=Depends(get_db)):
    with db.cursor(row_factory=dict_row) as cur:
        query = "SELECT * FROM drillholes WHERE id = %s"
        cur.execute(query, (id,))
        row = cur.fetchone()

        if not row:
            raise HTTPException(
                status_code=404, detail="Drillhole with this ID does not exist"
            )
    return row


@router.post("/drillholes", response_model=Drillhole, status_code=201)
def create_drillhole(drillhole: DrillholeCreate, db=Depends(get_db)):
    with db.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """INSERT INTO drillholes (hole_id, status, rock_type, grade, depth_m)
               VALUES (%s, %s, %s, %s, %s)
               RETURNING *""",
            (
                drillhole.hole_id,
                drillhole.status,
                drillhole.rock_type,
                drillhole.grade,
                drillhole.depth_m,
            ),
        )
        row = cur.fetchone()
        db.commit()
    return row


@router.put("/drillholes/{id}", response_model=Drillhole, status_code=200)
def update_drillhole(id: int, drillhole: DrillholeCreate, db=Depends(get_db)):
    with db.cursor(row_factory=dict_row) as cur:
        query = """UPDATE drillholes 
               SET hole_id = %s, status = %s, rock_type = %s, grade = %s, depth_m = %s
               WHERE id = %s
               RETURNING *"""
        cur.execute(
            query,
            (
                drillhole.hole_id,
                drillhole.status,
                drillhole.rock_type,
                drillhole.grade,
                drillhole.depth_m,
                id,
            ),
        )
        row = cur.fetchone()
        db.commit()
        if row is None:
            raise HTTPException(status_code=404, detail="Couldn't update drillhole")
    return row


@router.delete("/drillholes/{id}", status_code=204)
def delete_drillhole(id: int, db=Depends(get_db)):
    with db.cursor(row_factory=dict_row) as cur:
        cur.execute("DELETE FROM drillholes WHERE id = %s", (id,))
        affected_rows = cur.rowcount
        db.commit()

        if affected_rows == 0:
            raise HTTPException(
                status_code=404, detail="Drillhole does not exist with that ID"
            )
    return None


# must come after defined routes as it takes a snapshot the instant it's called
app.include_router(router)
