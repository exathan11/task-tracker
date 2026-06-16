from typing import Literal
from datetime import datetime

class Task:
    id: int
    name: str
    status: Literal["todo", "in-progress", "done"]
    created_at: datetime
    updated_at: datetime

    # Should the id be included here or derived from somewhere else?
    def __init__(self, name, id):
        current_date = datetime.now()
        self.name = name
        self.id = id
        self.status = "todo"
        self.created_at = current_date
        self.updated_at = current_date

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "status": self.status,
            "createdAt": self.created_at.strftime("%d/%m/%Y - %H:%M"),
            "updatedAt": self.updated_at.strftime("%d/%m/%Y - %H:%M")
        }