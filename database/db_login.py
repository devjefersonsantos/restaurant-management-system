from database.database import Database
from utils.empty_entries import empty_entries
from tkinter import messagebox

class DbLogin(Database):
    def __init__(self, username: str, password: str):
        super().__init__()
        self.__username = username
        self.__password = password

    def check_login(self) -> True:
        __entry_items = {"username":self.__username, "password":self.__password}

        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""SELECT * FROM ACCOUNT 
                                        WHERE username = %s AND password = md5(%s)""", (self.__username, self.__password))
                except Exception as error:
                    messagebox.showerror(title=None, message=error)
                else:
                    if self.cursor.fetchone():
                        return True
                    else:
                        messagebox.showerror(title=None, message="Incorrect username or password\nplease try again.")
