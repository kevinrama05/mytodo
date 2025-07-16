import csv
import curses

class TaskManager:
    """
    Adds, deletes and marks as completed given tasks
    """
    def __init__(self, task, priority, group, completed=False):
        self.task = task
        self.priority = priority
        self.group = group
        self.completed = completed

    def add_task():
        # Adds a task on a specified group
        with open("tasks/{self.group}.csv", mode="a", newline="") as file:
            writer = csv.writer(file, delimiter="|")
            writer.writerows([self.task, self.priority, self.completed])

    def mark_completed():
        # Marks an existing task as completed
        with open("tasks/{self.group}.csv", "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            # Loops every dictionary, and when it finds the task, it changes the status to True
            for i in reader:
                if i["task"] == self.task:
                    i["completed"] == True

        with open("tasks/{self.group}.csv", mode="w", newline="") as outfile:
            fieldnames = reader.fieldnames  
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)

    def delete_file():
        # Deletes a file from a specific group
        with open("tasks/{self.gropu}.csv", "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            new_rows = []
            for i in rows:
                if rows["task"] == self.task:
                    pass
                else:
                    new_rows.append(i)

        with open("tasks/{self.group}.csv", mode="w", newline="") as outfile:
            fieldnames - reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)


class GroupManager:
    ...

def main():
    task = input("Add task: ")
    while True:
        priority = input("Add priority(Low, Medium, High, Urgent): ")
        if priority not in ["Low", "Medium", "High", "Urgent"]:
            continue
        else:
            break
    group = input("Group: ")

    TaskManager(task, priority, group).add_task()

    


