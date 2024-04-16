from database.database import Database
from utils.empty_entries import empty_entries
from tkinter import messagebox
from utils.convert_to_sha3_256 import convert_to_sha3_256

class DbSignup(Database):
    def __init__(self, username: str, password: str, email: str):
        super().__init__()
        self.__username = username
        self.__password = password
        self.__email = email

        self.create_database()
        
        __entry_items = {"username":self.__username, "password":self.__password, "email":self.__email}

        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO account (username, password, email)
                                        VALUES (%s, %s, %s);""", (self.__username, convert_to_sha3_256(self.__password), self.__email))
                    self.connection.commit()
                except Exception as error:
                    messagebox.showerror(title="Sign Up Error", message=error)
                else:
                    messagebox.showinfo(title="Sign Up", message="Congratulations! Your account\nhas been successfully created.")
                finally:
                    self.cursor.close()
                    self.connection.close()
