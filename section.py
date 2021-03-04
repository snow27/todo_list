from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        filtered_tasks = [t for t in self.tasks if t.name == task_name]
        if filtered_tasks:
            task = filtered_tasks[0]
            task.completed = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        all_not_completed_task = [t for t in self.tasks if not t.completed]
        removed_tasks = len(self.tasks) - len(all_not_completed_task)
        self.tasks = all_not_completed_task
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details()+"\n"
        return result


