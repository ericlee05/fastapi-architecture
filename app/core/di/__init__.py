from pythondi import Provider, configure

from app.repository.todo import TodoRepository


def init_di():
    provider = Provider()

    provider.bind(TodoRepository, TodoRepository)

    configure(provider=provider)