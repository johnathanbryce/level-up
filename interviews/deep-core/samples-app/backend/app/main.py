from fastapi import FastAPI, APIRouter, HTTPException
from contextlib import asynccontextmanager
from app.db import init_db, get_connection
from typing import Literal, Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # runs once, before app serves requests
    yield  # anything after yield runs on shutdown


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
router = APIRouter()


class SampleCreate(BaseModel):
    name: str
    rock_type: Literal["granite", "basalt", "shale", "limestone", "sandstone"]
    grade: float
    depth_m: float


class Sample(SampleCreate):
    id: int


@router.get("/")
def init():
    return {"message": "hello world"}


@router.get("/samples", response_model=list[Sample])
def list_samples(rock_type: Optional[str] = None):
    conn = get_connection()
    cursor = conn.cursor()

    if rock_type:
        # Prefix match: "sha" -> "sha%" matches "shale". The `?` placeholder is
        # injection-safe (the driver escapes the value). SQLite LIKE is
        # case-insensitive for ASCII, so "Sha" matches "shale" too.
        cursor.execute(
            "SELECT * FROM samples WHERE rock_type LIKE ?", (rock_type + "%",)
        )
    else:
        cursor.execute("SELECT * FROM samples")

    rows = cursor.fetchall()
    conn.close()

    # rows are sqlite3.Row (dict-like); response_model wants plain dicts.
    return [dict(row) for row in rows]


@router.get("/samples/{id}", response_model=Sample)
def get_sample(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM samples WHERE id = ?", (id,))
    row = cursor.fetchone()  # returns one row or None
    conn.close()
    if row is None:
        raise HTTPException(
            status_code=404, detail="Sample with this ID does not exist"
        )
    return dict(row)


@router.post("/samples", response_model=Sample, status_code=201)
def create_sample(sample: SampleCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO samples (name, rock_type, grade, depth_m) VALUES (?,?,?,?)",
        (sample.name, sample.rock_type, sample.grade, sample.depth_m),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, **sample.model_dump()}


@router.delete("/samples/{id}", status_code=204)
def delete_sample(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM samples WHERE id = ?", (id,))
    conn.commit()
    row_count = cursor.rowcount
    conn.close()

    if row_count == 0:
        raise HTTPException(status_code=404, detail="Unable to find this sample")

    return None


# must come after defined routes as it takes a snapshot the instant it's called
app.include_router(router)
