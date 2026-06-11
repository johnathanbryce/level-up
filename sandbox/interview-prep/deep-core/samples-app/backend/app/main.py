from fastapi import FastAPI, APIRouter, HTTPException
from typing import Literal, Optional
from pydantic import BaseModel
from app.seed_data import SAMPLES

app = FastAPI()
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
    if rock_type:
        return [s for s in SAMPLES if s["rock_type"] == rock_type]
    return SAMPLES


@router.get("/samples/{id}", response_model=Sample)
def get_sample(id: int):
    target_sample = next((s for s in SAMPLES if s["id"] == id), None)
    if target_sample is None:
        raise HTTPException(
            status_code=404, detail="Sample with this ID does not exist"
        )
    return target_sample


@router.post("/samples", response_model=Sample, status_code=201)
def create_sample(sample: SampleCreate):

    sample_id = (
        max((s["id"] for s in SAMPLES), default=0) + 1
    )  # normally, would come from server
    sample_obj = {"id": sample_id, **sample.model_dump()}
    SAMPLES.append(sample_obj)
    return sample_obj


@router.delete("/samples/{id}", status_code=204)
def delete_sample(id: int):
    target_sample = next((s for s in SAMPLES if s["id"] == id), None)
    if target_sample is None:
        raise HTTPException(status_code=404, detail="Unable to find this sample")
    SAMPLES.remove(target_sample)
    return None


# must come after defined routes as it takes a snapshot the instant it's called
app.include_router(router)
