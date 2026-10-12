from tasks.AddTask import AddTask
from tasks.SaveData import SaveData
from tasks.ViewData import ViewData;
from tasks.UpdatData import UpdateData;
from tasks.DeleteData import DeleteTask;
def main():
    print("--- welcome to cloud task management system ---")

    save = SaveData()
    tasks = save.loadData()
    view = ViewData();
    update = UpdateData();
    delete = DeleteTask();

    while True:
        print("\n1. Create a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")

        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter task priority: ")
            status = input("Enter task status (default Pending): ") or "Pending"

            new_task = AddTask(task_name, priority, status)
            tasks.append(new_task)

            save.saveData(tasks)
            print("Task created successfully!")

        elif choice == "2":
            view.viewData(tasks);
        
        elif choice == "3":
            print("what do you want to do?")
            print("1.change status")
            print("2.change data")
            choic=input("Enter the choice: ")
            if choic == "1":
                update.changeStatus(tasks,view);
            if choic == "2":
                update.changeData(tasks,view);
            else:
                print("Enter the valid choice.")
            view.viewData(tasks);

        elif choice == "4":
            delete.deleteTask(tasks,view)
            
           

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Option not implemented in this test.")


if __name__ == "__main__":
    main()
