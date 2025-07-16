import json
import curses

def add_task(task, priority, group="daily"):
    """
    Adds a new task to the specific group, or to "daily" group, if not specified

    Args:
        task (str): The task you want to add
        priority (str): The level of urgency the task has (Low, Medium, High, Urgent)
        group (str): This is the group where the task will be added. It will be added to "daily" group, if not specified
    """
    # Step 1: Read the .json file of the specified group. Create an empty list if json.decoder.JSONDecodeError is traced
    with open(f"tasks/{group}.json", "r") as file:
        try:
            tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            tasks = []

    # Step 2: Add the new task on the created variable as a dictionary
    tasks.append({"task": f"{task}", "priority": f"{priority}", "completed": False})

    # Step 3: Write the variable on the .json file
    with open(f"tasks/{group}.json", "w") as file:
        json.dump(tasks, file, indent=4)

def mark_as_completed(task, group="daily"):
    """
    Marks a task as completed on a specific group, or to "daily" group, if not specified

    Args:
        task (str): The task you want to mark as completed
        group (str): This is the group where the task is located. It will be marked at completed to "daily" group, if not specified and if it exists 
    """

    # Step 1: Read the .json file of the specified group.
    with open(f"tasks/{group}.json", "r") as file:
        tasks = json.load(file)

    # Step 2: Change the "completed" value to True
    for i in tasks:
        if i["task"] == task:
            i["completed"] = True

    # Step 3: Write the variable on the .json file
    with open(f"tasks/{group}.json", "w") as file:
        json.dump(tasks, file, indent=4)

task = "Go to sleep"
priority = "High"
add_task(task, priority)

mark_as_completed(task)

