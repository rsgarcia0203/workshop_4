# features/testing.feature
Feature: Task Management

  Scenario: Adding a task
    Given an empty task list
    When a task named "<task_name>" is added
    Then the task list should contain "<task_name>"

  Scenario: Listing all tasks
    Given an empty task list
    When a task named "Task 1" is added
    When I list all tasks
    Then I should see the following tasks in the list:
      |Task Name|
      |Task 1|

  Scenario: Marking a task as completed
    Given a task list with tasks:
      | Task Name   |
      | Task 1       |
    When I mark task "Task 1" as completed
    Then the status of task "Task 1" should be "Completada"

  Scenario: Clearing completed tasks
    Given a task list with tasks:
      | Task Name   | Status      |
      | Task 1       | Completada  |
      | Task 2       | Pendiente   |
    When I clear completed tasks
    Then the task list should only contain tasks with status "Pendiente"

  Scenario: Clearing all tasks
    Given a task list with tasks:
      | Task Name   |
      | Task 1       |
      | Task 2       |
    When I clear all tasks
    Then the task list should be empty

  Scenario: Marking all tasks as completed
    Given a task list with tasks:
      | Task Name   | Status      |
      | Task 1       | Pendiente   |
      | Task 2       | Pendiente   |
    When I mark all tasks as completed
    Then all tasks in the list should have status "Completada"