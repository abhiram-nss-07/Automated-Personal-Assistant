from utils.helper import read_lines_from_file, write_lines_to_file
import config

def add_task():
    task = input("Enter the task: ")
    with open(config.TASK_FILE, "a") as file:
        file.write(f"{task}\n")
    print("Task added successfully!")

def remove_task():
    tasks = read_lines_from_file(config.TASK_FILE)
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task.strip()}")

    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
        write_lines_to_file(config.TASK_FILE, tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

def list_tasks():
    tasks = read_lines_from_file(config.TASK_FILE)
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(f"- {task.strip()}")
    else:
        print("No tasks available.")
