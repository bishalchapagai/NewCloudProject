from tasks.ViewData import ViewData


class UpdateData:
    def changeStatus(self, task, view):
        if not task:
            print("no task t show")
            return

        view.viewData(task)
        try:
            print("Which number?")
            choice = int(input("Enter the number: "))
            if 0 < choice <= len(task):
                task[choice - 1].set_status("Completed")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid task number")


    def changeData(self,task,view):
        if not task:
            print("Nothing to display");
            return;
        view.viewData(task);
        choice = int(input("Which data to change?"))
        new_name = input("Enter the name: ")
        new_priority = input("Enter the priority.")
        new_status = "Pending";
        task[choice-1].set_task_name(new_name);
        task[choice-1].set_priority(new_priority);
        task[choice-1].set_status(new_status);
        
