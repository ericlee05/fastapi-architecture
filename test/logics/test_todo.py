import pytest
from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
from pythondi import Provider, configure

from app.domain.todo import Todo
from app.dto.todo import TodoModifyRequest
from app.repository.todo import TodoRepository
from app.service.todo import TodoService

provider = Provider()
configure(provider=provider)

def UseMockDatabase(func):
    async def wrapper():
        client = AsyncMongoMockClient()
        await init_beanie(document_models=[Todo], database=client.get_database(name="db"))
        await func()

    return wrapper


@pytest.mark.asyncio
@UseMockDatabase
async def test_create():
    expected = {"title": "TEST TITLE", "description": "TEST DESCRIPTION"}

    mock_repo: TodoRepository = TodoRepository()
    todo_service = TodoService(todo_repository=mock_repo)

    response = await todo_service.create(TodoModifyRequest(**expected))

    assert response.title == expected['title']
    assert response.description == expected['description']


@pytest.mark.asyncio
@UseMockDatabase
async def test_edit():
    expected_origin = {"title": "TEST TITLE", "description": "TEST DESCRIPTION"}
    expected_changed = {"title": "TEST TITLE", "description": "CHANGED"}

    mock_repo: TodoRepository = TodoRepository()
    todo_service = TodoService(todo_repository=mock_repo)

    created_id = (await todo_service.create(TodoModifyRequest(**expected_origin))).id

    change_request = TodoModifyRequest(**expected_changed)
    response = await todo_service.edit(created_id, change_request)

    assert response.title == expected_changed['title']
    assert response.description == expected_changed['description']