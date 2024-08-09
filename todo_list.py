# todo_list.py
class Task:
    def __init__(self, nombre, estado="Pendiente"):
        self.nombre = nombre
        self.estado = estado

    def completar(self):
        self.estado = "Completada"

tasks_list = []
def add_task(nombre):
    global tasks_list
    task = Task(nombre)
    tasks_list.append(task)

def list_all_task():
    print("Tasks:")
    for task in tasks_list:
        print(f"\t- {task.nombre} ({task.estado})")

def mark_completed(task):
    task.completar()

def clear_completed():
    global tasks_list
    tasks_list = [task for task in tasks_list if task.estado == "Pendiente"]

def clear_all_task():
    global tasks_list
    tasks_list = []

def mark_all_completed():
    global tasks_list
    for task in tasks_list:
        task.completar()

def find_task_by_name(task_name):
    global tasks_list
    for task in tasks_list:
        if task.nombre == task_name:
            return task
    return None

def get_all_task_names():
    global tasks_list
    return [task.nombre for task in tasks_list]

def mark_completed_with_name(task_name):
    for task in tasks_list:
        if task.nombre == task_name:
            task.completar()