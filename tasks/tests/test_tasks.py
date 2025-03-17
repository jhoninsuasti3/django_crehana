import pytest
from rest_framework.test import APIClient
from tasks.domain.models import Task

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def task():
    return Task.objects.create(title="Test Task", description="Test Desc", completed=False)

def test_create_task(client):
    response = client.post('/graphql/', json={
        "query": "mutation { createTask(title: \"New Task\", description: \"Desc\", completed: false) { id } }"
    })
    assert response.status_code == 200

def test_get_task(client, task):
    response = client.post('/graphql/', json={
        "query": f"{{ task(id: {task.id}) {{ title }} }}"
    })
    assert response.status_code == 200
