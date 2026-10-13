class DeleteTask:
    def deleteTask(self,db,view):
        view.viewData(db);
        print("Which data to update? give id?")
        choice = int(input("Enter the id? "))
        db.deleteTask(choice);
