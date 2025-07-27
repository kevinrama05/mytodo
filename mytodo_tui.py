import curses
import json
import mytodo_funct

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
        return cyan if selected == False else cyan_selected
    elif dict_task["priority"] == "Medium":
        return yellow if selected == False else yellow_selected
    elif dict_task["priority"] == "High":
        return orange if selected == False else orange_selected
    elif dict_task["priority"] == "Urgent":
        return red if selected == False else red_selected


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

    # Step 3: Return the tasks' variable and the argument
    return tasks, group

def true_false(tasks):
    """
    Returns two lists of dictionaries, one with completed tasks, and one with uncompleted tasks

    Args:
        tasks (list of dicts): This is the list of the tasks in dictionary form

    Returns
        completed and uncompleted (list of dicts): Returns two lists of dictionaries, one with completed tasks and one with uncompleted tasks
    """
    # Step 1: Create two empty lists
    completed = []
    uncompleted = []

    # Step 2: Add each task to the corresponding list
    for i in tasks:
        if i["completed"] == True:
            completed.append(i)
        else:
            uncompleted.append(i)

    # Step 3: Return the lists
    return completed, uncompleted

def add_task_tui(stdscr, group="Daily"):
    """
    Makes a TUI for adding a task to a specific group

    Args:
        group (str): This is the group name, which is used for identifying the group
    """
    # Step 1: Clear the screen
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(1)

    # Step 2: Add an input field for the task and an input field for the priority
    stdscr.addstr(0, 0, "Task: ")
    stdscr.refresh()
    stdscr.addstr(1, 0, "Priority: ")
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Step 3: Handle the input for the task
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ") | set(r"""~`!@#$%^&*()-_=+[{]}\|;:'",<.>/?""")
    task = ""
    while True:
        stdscr.addstr(0, 6, task)
        key = stdscr.get_wch()
        if isinstance(key, str) and key in allowed_chars:
            task += key
        if key in ('\x7f', '\b', '\x08'):
            task = task[:-1]
            stdscr.addstr(0, 6+len(task), " ")
        if key == "\n":
            break
        if key == '\x1b':
            return
    # Step 4: Handle the input for the priority
    priority = ""
    while True:
        stdscr.addstr(1, 10, priority)
        key = stdscr.get_wch()
        if isinstance(key, str) and key in allowed_chars:
            priority += key
        if key in ('\x7f', '\b', '\x08'):
            priority = priority[:-1]
            stdscr.addstr(1, 10+len(priority), " ")
        if key == "\n":
            if priority.capitalize() not in ["Low", "Medium", "High", "Urgent"]:
                stdscr.addstr(3, 0, "Please add a valid priority (Low, Medium, High or Urgent)", curses.color_pair(1))
                stdscr.addstr(1, 10, " " * len(priority))
                priority = ""
            else:
                break
        if key == '\x1b':
            return

    stdscr.addstr(3, 0, " " * 57)
    stdscr.addstr(3, 0, f'Task "{task}" successfully added. Press any button to exit', curses.color_pair(2))
    stdscr.refresh()
    stdscr.getch()

    # Step 5: Add the task to the corresponding group
    mytodo_funct.add_task(task, priority, mytodo_funct.find_group(group))

def main(stdscr):
    """
    This is the main code for the TUI
    """
    stdscr.clear()
    curses.curs_set(0)

    # Get the "Daily" tasks, and split them into completed and uncompleted tasks
    group, group_name = get_tasks()
    completed, uncompleted = true_false(group)

    location = 0
    while True:
        # Print the tasks using a for loop
        for n, i in enumerate(uncompleted):
            if location == n:
                stdscr.addstr(n, 0, f"> {i['task']}", show_tasks(i, True))
                stdscr.refresh()
            else:
                stdscr.addstr(n, 0, f"  {i['task']}", show_tasks(i))
                stdscr.refresh()
        if completed != []:
            stdscr.addstr(len(uncompleted) + 1, 0, "--------------------")
            stdscr.refresh()

            for n, i in enumerate(completed):
                if location == n + len(uncompleted):
                    stdscr.addstr(n+3+len(uncompleted), 0, f"> {i['task']}", show_tasks(i, True))
                    stdscr.refresh()
                else:
                    stdscr.addstr(n+3+len(uncompleted), 0, f"  {i['task']}", show_tasks(i))

        key = stdscr.getch()
        if key == curses.KEY_UP and location > 0 :
            location -= 1
        elif key == curses.KEY_DOWN and location < len(group) - 1:
            location += 1

        if key == (ord("a") & 0x1f):
            add_task_tui(stdscr, group_name)
            stdscr.clear()
            group, group_name = get_tasks()
            completed, uncompleted = true_false(group)
            curses.curs_set(0)

        if key == 27:
            return


curses.wrapper(main)
