from behave import given, when, then
from todo_list import (Task, tasks_list, add_task, list_all_task, mark_completed,
                       clear_completed, clear_all_task, mark_all_completed,find_task_by_name,get_all_task_names,
                       mark_completed_with_name)


@given('an empty task list')
def empty_task_list(context):
    global tasks_list
    clear_all_task()



@given('a task list with tasks')
def task_list_with_tasks(context):
    global tasks_list
    clear_all_task()
    for row in context.table:
        task_name = row['Task Name']
        add_task(task_name)


@when('a task named "{task_name}" is added')
def add_task_named(context, task_name):
    global tasks_list
    add_task(task_name)


@when('I list all tasks')
def list_all_tasks(context):
    global tasks_list
    list_all_task()


@when('I mark task "{task_name}" as completed')
def mark_task_as_completed(context, task_name):
    global tasks_list
    mark_completed_with_name(task_name)


@when('I clear completed tasks')
def clear_completed_tasks(context):
    global tasks_list
    clear_completed()


@when('I clear all tasks')
def clear_all_tasks(context):
    global tasks_list
    clear_all_task()


@when('I mark all tasks as completed')
def mark_all_tasks_as_completed(context):
    global tasks_list
    mark_all_completed()


@then('the task list should contain "{task_name}"')
def assert_task_in_list(context, task_name):
    task = find_task_by_name(task_name)
    print(len(tasks_list))
    assert task is not None, f'Task "{task_name}" not found in the list'


@then('I should see the following tasks in the list')
def assert_tasks_in_list(context):
    global tasks_list
    expected_tasks = [row['Task Name'] for row in context.table]
    actual_tasks = get_all_task_names()
    try:
        assert actual_tasks == expected_tasks, f'Expected tasks: {expected_tasks}, Actual tasks: {actual_tasks}'
    except AssertionError as e:
        raise AssertionError(f'Tasks do not match. {e}')


@then('the status of task "{task_name}" should be "{status}"')
def assert_task_status(context, task_name, status):
    global tasks_list
    task = find_task_by_name(task_name)
    assert task is not None, f'Task "{task_name}" not found in the list'
    assert task.estado == status, f'Expected status: {status}, Actual status: {task.estado}'


@then('the task list should only contain tasks with status "{status}"')
def assert_tasks_with_status(context, status):
    global tasks_list
    for task in tasks_list:
        assert task.estado == status, f'Task "{task.nombre}" has unexpected status: {task.estado}'


@then('the task list should be empty')
def assert_empty_task_list(context):
    global tasks_list
    assert len(tasks_list) == 0, f'Task list is not empty'


@then('all tasks in the list should have status "{status}"')
def assert_all_tasks_status(context, status):
    global tasks_list
    for task in tasks_list:
        assert task.estado == status, f'Task "{task.nombre}" has unexpected status: {task.estado} need {status}'