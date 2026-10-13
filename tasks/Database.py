import sqlite3;
class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("CloudTask.db");
        self.cursor = self.connection.cursor();

    def createTable(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT DEFAULT 'Pending'
            )
            """
        )
        self.connection.commit();

    def addTask(self,task_name,priority,status="Pending"):
        self.cursor.execute(
            """
            INSERT INTO tasks(task_name,priority,status)
            VALUES(?,?,?)
            """,(task_name,priority,status)
        )
        self.connection.commit();

    def getTask(self):
        self.cursor.execute("""SELECT * FROM tasks""")
        return self.cursor.fetchall();

    def updateStatus(self, task_id, status):
        self.cursor.execute("""
            UPDATE tasks
            SET status = ?
            WHERE id = ?
            """, (status, task_id))

        self.connection.commit()

    def changeData(self,task_id):
        new_name = input("Enter the new name? ");
        new_priority = input("Enter the new Priority.");
        new_status = "Pending";
        self.cursor.execute("""
        UPDATE tasks
        SET task_name = ?,
            priority = ?,
            status = ?
        WHERE id = ?
    """, (new_name, new_priority, new_status, task_id))

        self.connection.commit();
    
    def deleteTask(self, task_id):
        self.cursor.execute("""
            DELETE FROM tasks
            WHERE id = ?
        """, (task_id,))

        deleted = self.cursor.rowcount
        self.connection.commit()

        return deleted > 0

    def close(self):
        self.connection.close();
    