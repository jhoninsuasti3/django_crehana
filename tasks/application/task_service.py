from tasks.infrastructure.task_repository import TaskRepository

class TaskService:
    """Servicio que encapsula la lógica de negocio de las tareas."""

    def get_tasks(self):
        return TaskRepository.get_all()

    def get_task(self, task_id):
        return TaskRepository.get_by_id(task_id)

    def create_task(self, data):
        return TaskRepository.create(data)

    def update_task(self, task_id, data):
        task = TaskRepository.get_by_id(task_id)
        if not task:
            return None
        return TaskRepository.update(task, data)

    def delete_task(self, task_id):
        task = TaskRepository.get_by_id(task_id)
        if task:
            TaskRepository.delete(task)
            return True
        return False
