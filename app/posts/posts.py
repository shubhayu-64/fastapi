from fastapi import APIRouter
from ..models import Post

router = APIRouter()

@router.get("/posts")
async def get_posts():
    return {"data": "Post data"}


@router.post("/posts")
async def create_posts(post: Post):
    return {"data": post.dict()}