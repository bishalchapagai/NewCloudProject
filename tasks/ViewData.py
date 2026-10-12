class ViewData:
    def viewData(self,task):
        if not task:
                print("Nothing to show yet")
                return
        else:
                
                for index, task in enumerate(task, start=1):
                        print(
                            f"{index}. Task Name: {task.get_task_name()} / "
                            f"Priority: {task.get_priority()} / "
                            f"Status: {task.get_status()}"
                        )