from task import Task
import datetime

class TaskList:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, description: str, hide_after_minutes: int = 60, deadline: str = None):
        final_deadline = None
        if deadline:
            if deadline.startswith("-"):
                try:
                    offset = int(deadline[1:])
                    final_deadline = (datetime.datetime.now() + datetime.timedelta(minutes=hide_after_minutes - offset)).isoformat()
                except:
                    final_deadline = None
            else:
                final_deadline = deadline
        self.tasks.append(Task(description, hide_after_minutes=hide_after_minutes, deadline=final_deadline))

    def get_visible_tasks(self):
        for task in self.tasks:
            task.check_visibility()
        return [t for t in self.tasks if not t.hidden]

    def get_hidden_tasks(self):
        for task in self.tasks:
            task.check_visibility()
        return [t for t in self.tasks if t.hidden]

    def find_task_by_index(self, index):
        visible = self.get_visible_tasks()
        if 0 <= index - 1 < len(visible):
            return visible[index - 1]
        return None

    def delete_task_by_index(self, index):
        visible = self.get_visible_tasks()
        if 0 <= index - 1 < len(visible):
            task = visible[index - 1]
            self.tasks.remove(task)
            return True
        return False

    def edit_task_by_index(self, index, new_description=None, new_minutes=None, new_deadline=None):
        visible = self.get_visible_tasks()
        if 0 <= index - 1 < len(visible):
            task = visible[index - 1]
            if new_description:
                task.description = new_description
            if new_minutes:
                task.hide_after_minutes = new_minutes
            if new_deadline:
                if new_deadline.startswith("-"):
                    try:
                        offset = int(new_deadline[1:])
                        task.deadline = (datetime.datetime.now() + datetime.timedelta(minutes=task.hide_after_minutes - offset)).isoformat()
                    except:
                        pass
                else:
                    task.deadline = new_deadline
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @staticmethod
    def from_dict(data):
        tl = TaskList(data["name"])
        tl.tasks = [Task.from_dict(t) for t in data["tasks"]]
        return tl