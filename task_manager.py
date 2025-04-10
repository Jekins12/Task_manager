import json
import os
from task_list import TaskList

SAVE_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.task_lists: dict[str, TaskList] = {}
        self.current_list: TaskList | None = None
        self.load()

    def create_list(self, name: str):
        self.task_lists[name] = TaskList(name)
        self.current_list = self.task_lists[name]
        self.save()

    def switch_list(self, name: str):
        if name in self.task_lists:
            self.current_list = self.task_lists[name]
        else:
            print(f"Lista '{name}' nie istnieje.")

    def list_names(self):
        return list(self.task_lists.keys())

    def show(self):
        if not self.current_list:
            print("Nie wybrano listy zadań. Użyj 'create [nazwa]' lub 'switch [nazwa]'.")
            return
        print(f"\n-- Lista zadań: {self.current_list.name} --")
        visible = self.current_list.get_visible_tasks()
        if not visible:
            print("Brak widocznych zadań.")
        else:
            for idx, task in enumerate(visible, start=1):
                print(f"{idx}: {task}")

    def show_hidden(self):
        if not self.current_list:
            print("Nie wybrano listy zadań.")
            return
        hidden = self.current_list.get_hidden_tasks()
        if not hidden:
            print("Brak ukrytych zadań.")
        else:
            print("\n-- Ukryte zadania --")
            for idx, task in enumerate(hidden, start=1):
                print(f"{idx}: {task}")

    def save(self):
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "lists": [lst.to_dict() for lst in self.task_lists.values()],
                "current": self.current_list.name if self.current_list else None
            }, f, indent=2, ensure_ascii=False)

    def load(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for lst_data in data.get("lists", []):
                    lst = TaskList.from_dict(lst_data)
                    self.task_lists[lst.name] = lst
                current_name = data.get("current")
                if current_name and current_name in self.task_lists:
                    self.current_list = self.task_lists[current_name]