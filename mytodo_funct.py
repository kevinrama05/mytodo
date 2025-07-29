import json
import curses
import os

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

def unmark_as_completed(task, group="daily"):
    """
    Marks a completed task as uncompleted on a specific group, or to "daily" group, if ot specified

    Args:
        task (str): The task you want to unmark
         group (str): This is the group where the task is located. It will be marked at completed to "daily" group, if not specified and if it exists
    """

    # Step 1: Read the .json file of the specified group
    with open(f"tasks/{group}.json", "r") as file:
        tasks = json.load(file)

    # Step 2: Change the "completed" value to False
    for i in tasks:
        if i["task"] == task:
            i["completed"] = False

    # Step 3: Write the variable on the .json file
    with open(f"tasks/{group}.json", "w") as file:
        json.dump(tasks, file, indent=4)

def delete_task(task, group="daily"):
    """
    Deletes a task on a specific group, or to "daily" group, if not specified

    Args:
        task (str): The task you want to delete
        group (str): This is the group where you want to delete the task. The "daily" group will be chosen, if not specified
    """

    # Step 1: Read the .json file of the specified group
    with open(f"tasks/{group}.json", "r") as file:
        old_tasks = json.load(file)

    # Step 2: Make another list of tasks, excluding the task you want to delete
    tasks = []
    for i in old_tasks:
        if i["task"] == task:
            pass
        else:
            tasks.append(i)

    # Step 3: Write the list on the .json file
    with open(f"tasks/{group}.json", "w") as file:
        json.dump(tasks, file, indent=4)

def delete_completed_tasks(group="daily"):
    """
    Deletes all the tasks that are completed on the speciied group, or to "daily" group, if not specified

    Args:
        group (str): This is the group you want to delete all the completed tasks. The "daily" group will be chosen, if not specified
    """

    # Step 1: Read the .json file of the specified group
    with open(f"tasks/{group}.json", "r") as file:
        old_tasks = json.load(file)

    # Step 2: Remove all the tasks with a value True
    tasks = []
    for i in old_tasks:
        if i["completed"] == True:
            pass
        else:
            tasks.append(i)

    # Step 3: Write the list on the .json file
    with open(f"tasks/{group}.json", "w") as file:
        json.dump(tasks, file, indent=4)

def create_group(group_name):
    """
    Creates a new group for your tasks. The name of a group should not be used twice

    Args:
        group_name (str): This is the name of the new group. It should be unique
    """

    # Step 1: Read the .json file of the group names
    with open("groups.json", "r") as file:
        groups = json.load(file)

    # Step 2: Check if the name is a duplicant. If not, create one
    for i in groups:
        if i["group_name"] == group_name:
            return "This group already exists"

    group_file = ""
    for i in group_name:
        if i.isalpha():
            if i.isupper:
                group_file += i.lower()
            else:
                group_file += i
        elif  i == " " or i == "-":
            group_file += "_"
        else:
            group_file += i

    groups.append({"group_name": f"{group_name}", "group_file": f"{group_file}"})

    # Step 3: Write the list on the .json file
    with open("groups.json", "w") as file:
        json.dump(groups, file, indent=4)

    # Step 4: Create the .json file for the new group
    open(f"tasks/{group_file}.json", "w").close()

def delete_group(group_name):
    """
    Deletes an existing group, with all the tasks inside. The "Daily" group cannot be deleted, because is the default group

    Args:
        group_name (str): Deletes the group with the corresponding name
    """

    # Step 1: Check if is the "Daily" group. If yes, return and stop the function
    if group_name == "Daily":
        return 'You cannot remove the "Daily" group, because is the default group'

    # Step 2: Read the .json file
    with open("groups.json", "r") as file:
        groups = json.load(file)

    # Step 3: Locate the target group, and remove it
    new_groups = []
    for i in groups:
        if i["group_name"] == group_name:
            path = i["group_file"]
            pass
        else:
            new_groups.append(i)

    # Step 4: Write the list on the .json file
    with open("groups.json", "w") as file:
        json.dump(new_groups, file, indent=4)

    # Step 5: Deletes the .json file of the deleted group
    os.remove(f"tasks/{path}.json")

def find_group(group_name):
    """
    Returns the group file, when you give the group name

    Args:
        group_name (str): The name of the group

    Returns:
        grouo_file (str): The name of the group's .json file
    """
    # Step 1: Read the groups.json file
    with open("groups.json", "r") as file:
       groups = json.load(file)

    # Step 2: Find the group file, and return it
    for u in groups:
        if u["group_name"] == group_name:
            return u["group_file"]

unmark_as_completed("Go to work")
