class AddTask:
    def __init__(self, task_name, priority, status="Pending"):
        self.task_name = task_name
        self.priority = priority
        self.status = status

    def update_priority(self, new_priority):
        self.priority = new_priority

    def completed(self):
        self.set_status("Completed")

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

    def set_task_name(self, new_task_name):
        self.task_name = new_task_name

    def get_task_name(self):
        return self.task_name

    def set_priority(self, new_priority):
        self.priority = new_priority

    def get_priority(self):
        return self.priority

    def to_dict(self):
        return {
            "task_name": self.task_name,
            "priority": self.priority,
            "status": self.status
        }