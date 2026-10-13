class ViewData:
    def viewData(self,db):
        tasks = db.getTask();
        for task in tasks:
                        print(f"{task[0]}. Task: {task[1]} // Priority: {task[2]} // Status: {task[3]}")
        