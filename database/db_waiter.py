from database.database import Database
from utils.empty_entries import empty_entries
from tkinter import messagebox

class DbWaiter(Database):
    def __init__(self, token):
        super().__init__()
        self.__token = token

    def create_waiter(self, name: str, cellphone: str) -> True:
        __entry_items = {"name": name, "cellphone": cellphone}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO waiter (name, cell_phone)
                                        VALUES (%s, %s);""", (name, cellphone))
                    self.connection.commit()

                except Exception as error:
                    messagebox.showerror(title="Create Waiter Error", message=error)
                else:
                    messagebox.showinfo(title="Create Waiter", message=f"Waiter: {name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_waiters(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM waiter
                                    ORDER BY id_waiter""")
                self.result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Waiters Error", message=error)
            else:
                return self.result
            finally:
                self.cursor.close()
                self.connection.close()
