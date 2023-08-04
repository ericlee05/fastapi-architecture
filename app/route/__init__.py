from fastapi import APIRouter
from app.route.todo import router as todo_router

root_router = APIRouter()

root_router.include_router(todo_router, prefix="/todos", tags=["Todo"])