# {
#     "tasks": [
#         {"id": 1, "task": "Finish homework", "status": "Pending"},
#         {"id": 2, "task": "Buy groceries", "status": "Completed"}
#     ]
# }

import json


choice = input(
    "\n(1) Add Task, \n(2) View Tasks, \n(3) Update Task, \n(4) Delete Task \nChoose an action:  "
)


# Save tasks
def save_tasks(tasks):
    with open("./tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Add tasks (Create)
def add_task(task, filename="./tasks.json"):
    tasks = load_tasks(filename)
    new_task = {"id": len(tasks["tasks"]) + 1, "task": task, "status": "pending"}
    tasks["tasks"].append(new_task)
    save_tasks(tasks)


# Load tasks from file (Read)
def load_tasks(filename="./tasks.json"):
    with open(filename, "r") as file:
        tasks = json.load(file)
        return tasks


# Update tasks (Update)


# Delete tasks (Delete)
def delete_task(task_id):
    tasks = load_tasks()
    tasks["tasks"] = [
        task for task in tasks["tasks"] if task["id"] != task_id
    ]  # List comprehension to filter out the task to be deleted
    save_tasks(tasks)


if choice == "1":
    task = input("Enter your task: ")
    add_task(task)

if choice == "2":
    tasks = load_tasks()
    for task in tasks["tasks"]:
        print(f"{task['id']}. {task['task']} - {task['status']}")
        
if choice == "3":
    tasks = load_tasks()
    task_id = int(input("Enter the task ID to update: "))
    new_status = input("Enter new status (pending/completed): ").lower()
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            task["status"] = new_status
            break
        else:
            print("Task ID not found.")
    save_tasks(tasks)

if choice == "4":
    task_id = int(input("Enter the task ID to delete: "))
    delete_task(task_id)