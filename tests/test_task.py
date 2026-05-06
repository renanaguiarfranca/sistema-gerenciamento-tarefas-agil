import pytest
from a import TaskManager

def test_create_task():
    manager = TaskManager()
    task = manager.create_task("Test Task", "Description", "Alta")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.status == "A Fazer"

def test_read_tasks():
    manager = TaskManager()
    manager.create_task("Task 1", "Desc 1", "Alta")
    manager.create_task("Task 2", "Desc 2", "Média")
    tasks = manager.read_tasks()
    assert len(tasks) == 2

def test_update_task():
    manager = TaskManager()
    task = manager.create_task("Task", "Desc", "Alta")
    updated = manager.update_task(1, status="Concluído")
    assert updated.status == "Concluído"

def test_delete_task():
    manager = TaskManager()
    manager.create_task("Task", "Desc", "Alta")
    deleted = manager.delete_task(1)
    assert deleted is not None
    assert len(manager.tasks) == 0