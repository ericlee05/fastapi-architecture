from uuid import UUID

from fastapi import APIRouter, Body
from h11 import Response

from app.dto.todo import TodoResponse, TodoModifyRequest
from app.service.todo import TodoService

router = APIRouter()


@router.get("/")
async def getAllTodo() -> list[TodoResponse]:
    return await TodoService().getAll()


@router.post("/")
async def createTodo(todo_request: TodoModifyRequest = Body()) -> TodoResponse:
    return await TodoService().create(todo_request)


@router.patch("/{todo_id}",
              response_model=TodoResponse)
async def editTodo(todo_id: UUID, todo_request: TodoModifyRequest = Body()) -> TodoResponse:
    return await TodoService().edit(todo_id, todo_request)


@router.delete("/{todo_id}")
async def deleteTodo(todo_id: UUID):
    await TodoService().delete(todo_id)
    return Response(status_code=204)