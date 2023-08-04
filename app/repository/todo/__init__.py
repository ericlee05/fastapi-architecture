from uuid import UUID

from app.domain.todo import Todo


class TodoRepository:
    async def findAll(self) -> list[Todo]:
        return await Todo.find_all().to_list()

    async def findById(self, id: UUID) -> Todo:
        return await Todo.find_one(Todo.id == id)

    async def save(self, todo: Todo) -> Todo:
        return await todo.insert()

    async def edit(self, id: UUID, title: str, description: str):
        found: Todo = await self.findById(id)
        await found.update({Todo.title:title, Todo.description: description})

    async def delete(self, todo_id):
        found: Todo = await self.findById(todo_id)
        await found.delete()