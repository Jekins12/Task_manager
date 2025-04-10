import datetime

class Task:
    def __init__(self, description: str, created_at=None, completed=False, hidden=False, hide_after_minutes=60):
        self.description = description
        self.created_at = created_at or datetime.datetime.now()
        self.completed = completed
        self.hidden = hidden
        self.hide_after_minutes = hide_after_minutes

    def mark_done(self):
        self.completed = True

    def check_visibility(self):
        if not self.completed:
            elapsed = (datetime.datetime.now() - self.created_at).total_seconds() / 60
            self.hidden = elapsed >= self.hide_after_minutes

    def to_dict(self):
        return {
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "completed": self.completed,
            "hidden": self.hidden,
            "hide_after_minutes": self.hide_after_minutes
        }

    @staticmethod
    def from_dict(data):
        return Task(
            description=data["description"],
            created_at=datetime.datetime.fromisoformat(data["created_at"]),
            completed=data["completed"],
            hidden=data["hidden"],
            hide_after_minutes=data["hide_after_minutes"]
        )

    def __str__(self):
        status = "✔" if self.completed else " "
        return f"[{status}] {self.description} (dodano: {self.created_at.strftime('%H:%M')})"