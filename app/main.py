from fastapi import FastAPI, APIRouter




app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}

