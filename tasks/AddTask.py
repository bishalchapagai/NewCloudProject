
class AddTask:
    def addTask(self,db):
        task_name = input("Enter task name: ")
        priority = input("Enter task priority: ")
        db.addTask(task_name,priority);
        print("Task added sucessfully!");