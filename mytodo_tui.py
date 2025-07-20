import curses
import json

def show_tasks(dict_task, selected=False):
    """
    Is used for printing a task on the right way.
    The task is shown in these 5 ways:
        1. Cyan: If the task is "Low" priority
        2. Yellow: If the task is "Medium" priority
        3. Orange: If the task is "High" priority
        4. Red: If the task is "Urgent" priority
        5. Green: If the task is completed
        6. White background: If the task is selected

    Args:
        stdscr: This represents the window where the tasks will be printed
        dict_task (dict): This is the task after is extracted from the .json file
        selected (bool): This shows if the task is selected. 
    """
    # Step 1: Initialize the colors for each priority and for completed tasks
    # This is the text color when the priority is low  
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_WHITE)
    cyan = curses.color_pair(1)
    cyan_selected = curses.color_pair(2)

    # This is the text color when the priority is medium
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    yellow = curses.color_pair(3)
    yellow_selected = curses.color_pair(4)

    # This is the text color when the priority is high
    curses.init_pair(5, 208, curses.COLOR_BLACK)
    curses.init_pair(6, 208, curses.COLOR_WHITE)
    orange = curses.color_pair(5)
    orange_selected = curses.color_pair(6)

    # This is the text color when the priority is urgent
    curses.init_pair(7, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_RED, curses.COLOR_WHITE)
    red = curses.color_pair(7)
    red_selected = curses.color_pair(8)

    # This is the text color when the task is completed
    curses.init_pair(9, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_WHITE)
    completed = curses.color_pair(9)
    completed_selected = curses.color_pair(10)

    # Step 2: Return the right color based on the task
    if dict_task["completed"] == True:
        return completed if selected == False else completed_selected
    elif dict_task["priority"] == "Low":
        return cyan if selected == False else completed_cyan
    elif dict_task["priority"] == "Medium":
        return yellow if selected == False else completed_yellow
    elif dict_task["priority"] == "High":
        return orange if selected == False else completed_orange
    elif dict_task["priority"] == "Urgent":
        return red if selected == False else completed_red


def get_tasks(group="Daily"):
    """
    Returns all the tasks of a specific group. If the tasks' group is empty, returns a statement that the tasks' group are completed.

    Args:
        group (str): This is the name of the group. If not specified, the "Daily" group will be used

    Returns:
        tasks (list of dicts): All the tasks of that group, extracted from the corresponding .json file
    """

    # Step 1: Get the .json filename for the given group
    with open("groups.json", "r") as file:
        groups = json.load(file)

    for i in groups:
        if i["group_name"] == group:
            g = i["group_file"]
            break

    # Step 2: Read the tasks of the group's .json file
    with open(f"tasks/{g}.json", "r") as file:
        tasks = json.load(file)

    # Step 3: Return the tasks' variable
    return tasks

def main(stdscr):
    """
    This is the main code for the TUI
    """
    stdscr.clear()
    curses.curs_set(0)
    
    group = get_tasks()

    while True:

        current_location = 0

        for n, i in enumerate(group):
            stdscr.addstr(n, 0, f"  {i['task']}", show_tasks(i))
            stdscr.refresh()


curses.wrapper(main)
