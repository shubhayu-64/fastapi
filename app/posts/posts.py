from fastapi import APIRouter
from ..models import Post



@app.get("/posts")
async def get_posts():
    return {"data": "Post data"}


@app.post("/posts")
async def create_posts(post: Post):
    return {"data": post.dict()}