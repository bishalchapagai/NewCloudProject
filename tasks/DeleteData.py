class DeleteTask:
    def deleteTask(self,task,view):
        if not task:
            print("Nothing to delete.")
            return
        view.viewData(task);
        print("Which number you want to delete.")
        choice = int(input("Enter the umber: "))
        if 0<choice<=len(task):
            task.pop(choice-1);
        else:
            print("Invalid choice");
        return task;
