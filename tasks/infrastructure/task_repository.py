from tasks.domain.models import Task

class TaskRepository:
    """Repositorio de Tareas que interactúa con la base de datos."""

    @staticmethod
    def get_all():
        return Task.objects.all()

    @staticmethod
    def get_by_id(task_id):
        return Task.objects.filter(id=task_id).first()

    @staticmethod
    def create(data):
        return Task.objects.create(**data)

    @staticmethod
    def update(task, data):
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return task

    @staticmethod
    def delete(task):
        task.delete()
