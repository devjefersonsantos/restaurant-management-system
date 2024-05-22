from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *

class TableDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_table_id(self, table_id: int) -> True:
        if self.connect_to_database():
            try:
                self.cursor.execute("""INSERT INTO "table" (table_id)
                                    VALUES (%s)""", (table_id,))
                self.connection.commit()

            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while creating a table.")
                messagebox.showerror(title="Create Table ID Error", message=error)
            else:
                log_info(f"System user ID: {self.__account_id}. Table created with ID: {table_id}.")
                messagebox.showinfo(title=None, message="Table created successfully")
                return True
            finally:
                self.cursor.close()
                self.connection.close()

    def create_table(self, multiplier: int) -> True:
        if self.connect_to_database():
            try:
                for _ in range(multiplier):
                    self.cursor.execute("""INSERT INTO "table" (table_id) 
                                        VALUES (DEFAULT) RETURNING table_id;""")
                    log_info(f"System user ID: {self.__account_id}. Table created with ID: {self.cursor.fetchone()[0]}.")
                self.connection.commit()

            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while creating a table.")
                messagebox.showerror(title="Create Table Error", message=error)
            else:
                return True
            finally:
                self.cursor.close()
                self.connection.close()

    def read_tables(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM "table"
                                    ORDER BY table_id""")
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Tables Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()
    
    def delete_table(self, table_id: int) -> True:
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM "table"
                                    WHERE table_id = %s""", (table_id,))
                self.connection.commit()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while deleting a table.")
                messagebox.showerror(title="Delete Table Error", message=error)
            else:
                log_warning(f"System user ID: {self.__account_id}. Table ID: {table_id} was deleted.")
                messagebox.showinfo(title="Delete Table", message=f"Table ID: {table_id} was deleted.")
                return True
            finally:
                self.cursor.close()
                self.connection.close()

    def get_table_ids(self) -> list[tuple[int]]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT table_id FROM "table"
                                    ORDER BY table_id;""")
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Get Table IDs", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()
