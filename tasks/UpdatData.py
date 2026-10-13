from tasks.ViewData import ViewData


class UpdateData:
    def changeStatus(self,db,view):
            view.viewData(db)
            print("Which data to update? give id?")
            choi = int(input("Enter the id? "))
            newStatus = input("Which status currently? ")
            db.updateStatus(choi, newStatus)

        

    def changeData(self,db,view):
                    view.viewData(db);
                    print("Which data to update? give id?")
                    choi = int(input("Enter the id? "))
                    db.changeData(choi)
        
        
