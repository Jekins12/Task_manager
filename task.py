import datetime

class Task:
    def __init__(self, description: str, created_at=None, completed=False, hidden=False,
                 hide_after_minutes=60, deadline=None):
        self.description = description
        self.created_at = created_at or datetime.datetime.now()
        self.completed = completed
        self.hidden = hidden
        self.hide_after_minutes = hide_after_minutes
        self.deadline = deadline  # ISO string or None

    def mark_done(self):
        self.completed = True

    def check_visibility(self):
        if not self.completed:
            elapsed = (datetime.datetime.now() - self.created_at).total_seconds() / 60
            self.hidden = elapsed >= self.hide_after_minutes

    def is_due_soon(self):
        if self.deadline:
            try:
                deadline_dt = datetime.datetime.fromisoformat(self.deadline)
                delta = deadline_dt - datetime.datetime.now()
                return 0 <= delta.total_seconds() <= 3600  # within the next hour
            except Exception:
                return False
        return False

    def is_overdue(self):
        if self.deadline:
            try:
                deadline_dt = datetime.datetime.fromisoformat(self.deadline)
                return datetime.datetime.now() > deadline_dt
            except Exception:
                return False
        return False

    def to_dict(self):
        return {
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "completed": self.completed,
            "hidden": self.hidden,
            "hide_after_minutes": self.hide_after_minutes,
            "deadline": self.deadline
        }

    @staticmethod
    def from_dict(data):
        return Task(
            description=data["description"],
            created_at=datetime.datetime.fromisoformat(data["created_at"]),
            completed=data["completed"],
            hidden=data["hidden"],
            hide_after_minutes=data["hide_after_minutes"],
            deadline=data.get("deadline")
        )

    def __str__(self):
        status = "✔" if self.completed else " "
        warn = ""
        if self.is_overdue():
            warn = " ⛔️"
        elif self.is_due_soon():
            warn = " ⏰"
        deadline_str = f" | deadline: {self.deadline}" if self.deadline else ""
        return f"[{status}]{warn} {self.description}{deadline_str} (dodano: {self.created_at.strftime('%H:%M')})"