import pytest
from task import create_task

# First test: Create a task with a title
def test_create_task_with_title():
    task = create_task("Buy groceries")
    assert task.title == "Buy groceries"


def test_create_task_with_priority():
    task = create_task("Buy groceries", "high")
    assert task.priority == "high"

def test_create_task_without_priority():
    task = create_task("Buy groceries")
    assert task.priority is None

def test_create_task_without_title():
    with pytest.raises(ValueError) as excinfo:
        create_task("")
    assert str(excinfo.value) == "Title cannot be empty"

def test_create_task_with_class_implementation():
    task= create_task("Buy groceries")
    assert task.title == "Buy groceries"
    assert task.priority is None
