from datetime import datetime
from typing import Literal
from uuid import uuid4

from exceptions import InvalidTaskStateError

StateType = Literal["pending", "in_progress", "complete"] 
States = ["pending", "in_progress", "complete"]

class Task:
    def __init__(
        self, title: str, description: str, 
        expiration_date: datetime, state: StateType = "pending"
    ) -> None:
        self.__id = uuid4()
        self.title = title
        self.description = description
        self.expiration_date = expiration_date
        self.__state = state

    @property
    def id(self) -> str:
        return self.__id

    def print(self) -> None:
        print(f"Task: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nExpiration Date: {self.expiration_date}\nState: {self.__state}")

    def change_task_state(self, state: StateType) -> None:
        if not state in States: raise InvalidTaskStateError("You must enter a valid status to change the status of a task.")
        
        self.__state = state
        print(f"{self.title} task with pending status was changed to in_progress")

    def edit(self, title: str, description: str, expiration_date: datetime) -> None:
        if not title and not description and not expiration_date: return

        dict = {
            "title": title,
            "description": description,
            "expiration_date": expiration_date
        }

        for key, value in dict.items():
            if value:
                setattr(self, key, value)

def main() -> None:
    print("----- Main Task.py -----")

    task = Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=datetime(year=2025, month=2, day=24)
    )

    task.print()

    task.change_task_state(state="in_progress")

if __name__ == "__main__":
    main()