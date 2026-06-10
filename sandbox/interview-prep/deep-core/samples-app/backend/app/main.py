from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()


@router.get("/")
def init():
    return {"message": "hello world"}

# must come after defined routes as it takes a snapshot the instant it's called
app.include_router(router)
