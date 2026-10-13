from tasks.AddTask import AddTask
from tasks.ViewData import ViewData;
from tasks.UpdatData import UpdateData;
from tasks.DeleteData import DeleteTask;
from tasks.Database import DataBase;
def main():
    print("--- welcome to cloud task management system ---")

    add = AddTask();
    view = ViewData();
    update = UpdateData();
    delete = DeleteTask();
    db = DataBase();
    db.createTable();

    while True:
        print("\n1. Create a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")

        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
                add.addTask(db);
            

        elif choice == "2":
            view.viewData(db);
            
        
        elif choice == "3":
            print("what do you want to do?")
            print("1.change status")
            print("2.change data")
            choic=input("Enter the choice: ")
            if choic == "1":
                update.changeStatus(db,view);

            if choic == "2":
                update.changeData(db,view)
                

        elif choice == "4":
            delete.deleteTask(db,view);
           

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Option not implemented in this test.")


if __name__ == "__main__":
    main()
