from database.database import Database
from utils.empty_entries import empty_entries
from tkinter import messagebox
from database.db_login import DbLogin
from logs.events import *

class DbCategory(Database):
    def __init__(self, token):
        super().__init__()
        self.__id_account = DbLogin.token_to_id_account(token)

    def create_category(self, name: str, description: str) -> True:
        __entry_items = {"name": name, "description ": description}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO category (name, description)
                                        VALUES (%s, %s) RETURNING id_category;""", (name, description))
                    self.connection.commit()
                    __id_category = self.cursor.fetchone()[0]

                except Exception as error:
                    log_error(f"System user id: {self.__id_account}. An error occurred while creating a category.")
                    messagebox.showerror(title="Create Category Error", message=error)
                else:
                    log_info(f"System user id: {self.__id_account}. Create category with id: {__id_category}.")
                    messagebox.showinfo(title="Create Category", message=f"Category: {name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_categories(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM category
                                    ORDER BY id_category""")
                self.result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Categories Error", message=error)
            else:
                return self.result
            finally:
                self.cursor.close()
                self.connection.close()
