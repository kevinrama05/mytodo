import curses
import json
import mytodo_funct

def unmark_task_completed(task):
    with open("tasks/daily.json", "r") as file:
        tasks = json.load(file)

    for i in tasks:
        if i["task"] == task:
            i["completed"] = False

    for i in tasks:
        print(i)

unmark_task_completed("Go to work")
