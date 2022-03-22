from fastapi import FastAPI, APIRouter
import posts

app = FastAPI()

app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "hello world"}

