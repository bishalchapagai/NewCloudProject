import json
from .AddTask import AddTask

class SaveData:

    def saveData(self, tasks):
        data = []

        for task in tasks:
            data.append(task.to_dict())

        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)

    def loadData(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)

            tasks = []

            for item in data:
                task = AddTask(
                    item["task_name"],
                    item["priority"],
                    item["status"]
                )
                tasks.append(task)

            return tasks

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []