from fastapi import FastAPI, APIRouter
from typing import Literal, Optional
from pydantic import BaseModel
from app.seed_data import SAMPLES

app = FastAPI()
router = APIRouter()


class Sample(BaseModel):
    id: int
    name: str
    rock_type: Literal["granite", "basalt", "shale", "limestone", "sandstone"]
    grade: float
    depth_m: float


@router.get("/")
def init():
    return {"message": "hello world"}


@router.get("/samples", response_model=Sample)
def list_samples(options: Optional[str] = None):
    return {"samples": SAMPLES}


# must come after defined routes as it takes a snapshot the instant it's called
app.include_router(router)
