import pytest

from src.app import app, manager


@pytest.fixture(autouse=True)
def reset_manager():
    manager.tasks = []
    manager.next_id = 1
    yield


def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Gerenciamento de Tarefas' in response.data


def test_create_task_form():
    client = app.test_client()
    response = client.post('/tasks', data={
        'title': 'Nova Tarefa',
        'description': 'Descrição da tarefa',
        'priority': 'Alta',
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Nova Tarefa' in response.data


def test_create_task_api():
    client = app.test_client()
    response = client.post('/tasks', json={
        'title': 'Api Tarefa',
        'description': 'Teste JSON',
        'priority': 'Média',
    })
    assert response.status_code == 201
    assert response.is_json
    data = response.get_json()
    assert data['title'] == 'Api Tarefa'


def test_update_task_form():
    client = app.test_client()
    manager.create_task('Tarefa', 'Desc', 'Alta')
    response = client.post('/tasks/1/update', data={'status': 'Em Progresso'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Em Progresso' in response.data


def test_delete_task_form():
    client = app.test_client()
    manager.create_task('Tarefa', 'Desc', 'Alta')
    response = client.post('/tasks/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Nenhuma tarefa encontrada.' in response.data
