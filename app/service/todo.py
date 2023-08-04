import datetime
from uuid import UUID

from pythondi import inject

from app.domain.todo import Todo
from app.dto.todo import TodoResponse, TodoModifyRequest
from app.repository.todo import TodoRepository


class TodoService:
    @inject()
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def getAll(self) -> list[TodoResponse]:
        todo_list: list[Todo] = await self.todo_repository.findAll()
        return list(map(lambda x: TodoResponse.from_orm(x), todo_list))

    async def create(self, todo_request: TodoModifyRequest):
        todo: Todo = Todo(title=todo_request.title, description=todo_request.description, created_at=datetime.datetime.now())
        return TodoResponse.from_orm(await self.todo_repository.save(todo))

    async def edit(self, id: UUID, todo_request: TodoModifyRequest):
        todo: Todo = await self.todo_repository.findById(id)
        await todo.set({Todo.title: todo_request.title, Todo.description: todo_request.description})

        return TodoResponse.from_orm(todo)

    async def delete(self, todo_id: UUID):
        await self.todo_repository.delete(todo_id)
