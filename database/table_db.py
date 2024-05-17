from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *

class TableDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_table(self) -> True:
        if self.connect_to_database():
            try:
                self.cursor.execute("""INSERT INTO "table" (table_id) 
                                    VALUES (DEFAULT) RETURNING table_id;""")
                self.connection.commit()
                __table_id = self.cursor.fetchone()

            except Exception as error:
                log_error(f"System user id: {self.__account_id}. An error occurred while creating a table.")
                messagebox.showerror(title=None, message=f"Error: {error}")
            else:
                log_info(f"System user ID: {self.__account_id}. Table created with ID: {__table_id[0]}.")
                return True
            finally:
                self.cursor.close()
                self.connection.close()
