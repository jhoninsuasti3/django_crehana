import strawberry
from typing import List
from tasks.application.task_service import TaskService
from tasks.domain.models import Task

@strawberry.type
class TaskType:
    id: int
    title: str
    description: str
    completed: bool

task_service = TaskService()

@strawberry.type
class Query:
    @strawberry.field
    def tasks(self) -> List[TaskType]:
        return task_service.get_tasks()

    @strawberry.field
    def task(self, id: int) -> TaskType:
        return task_service.get_task(id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_task(self, title: str, description: str, completed: bool) -> TaskType:
        task = task_service.create_task({"title": title, "description": description, "completed": completed})
        return task

    @strawberry.mutation
    def update_task(self, id: int, title: str, description: str, completed: bool) -> TaskType:
        task = task_service.update_task(id, {"title": title, "description": description, "completed": completed})
        return task

    @strawberry.mutation
    def delete_task(self, id: int) -> bool:
        return task_service.delete_task(id)

schema = strawberry.Schema(query=Query, mutation=Mutation)
