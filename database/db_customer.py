from database.database import Database
from utils.empty_entries import empty_entries
from tkinter import messagebox
from database.db_login import DbLogin

class DbCustomer(Database):
    def __init__(self, token):
        super().__init__()
        self.__token = token

    def create_customer(self, name: str, address: str, cellphone: str, email: str | None = None) -> True:
        __entry_items = {"name": name, "address": address, "cellphone": cellphone}
        
        if not empty_entries(**__entry_items):
            __id_account = DbLogin.token_to_id_account(self.__token)
            
            if self.connect_to_database():
                try:
                    if email is None:
                        self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, account_id_account)
                                            VALUES (%s, %s, %s, %s);""", (name, address, cellphone, __id_account))
                        self.connection.commit()
                    else:
                        self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, email, account_id_account)
                                            VALUES (%s, %s, %s, %s, %s);""", (name, address, cellphone, email, __id_account))
                        self.connection.commit()
                except Exception as error:
                    messagebox.showerror(title=None, message=error)
                else:
                    messagebox.showinfo(title=None, message=f"Customer: {name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()
