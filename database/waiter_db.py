from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *
from utils.empty_entries import empty_entries

class WaiterDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_waiter(self, name: str, cellphone: str) -> True:
        __entry_items = {"name": name, "cellphone ": cellphone}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO waiter (name, cell_phone)
                                        VALUES (%s, %s) RETURNING waiter_id;""", (name, cellphone))
                    self.connection.commit()
                    __waiter_id = self.cursor.fetchone()

                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while creating a waiter.")
                    messagebox.showerror(title="Create Waiter Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Create waiter with ID: {__waiter_id[0]}.")
                    messagebox.showinfo(title="Create Waiter", message=f"Waiter: {name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_waiters(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM waiter
                                    ORDER BY waiter_id""")
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Waiters Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def update_waiter(self, new_name: str, new_cellphone: str, waiter_id: int) -> True:
        __entry_items = {"name": new_name, "cellphone": new_cellphone}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE waiter
                                        SET name = %s, cell_phone = %s
                                        WHERE waiter_id = %s""", (new_name, new_cellphone, waiter_id))

                    self.connection.commit()
                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while updating a waiter.")
                    messagebox.showerror(title="Update Waiter Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Waiter ID: {waiter_id} has been updated.")
                    messagebox.showinfo(title="Update Waiter", message=f"Waiter: {new_name}, updated successfully!")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def delete_waiter(self, waiter_id: int) -> None:
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM waiter
                                    WHERE waiter_id = %s""", (waiter_id,))
                self.connection.commit()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while deleting a waiter.")
                messagebox.showerror(title="Delete Waiter Error", message=error)
            else:
                log_warning(f"System user ID: {self.__account_id}. Waiter ID: {waiter_id} was deleted.")
            finally:
                self.cursor.close()
                self.connection.close()

    def search_waiter(self, typed: str) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM waiter 
                                    WHERE name LIKE %s""", ("%" + typed + "%",))
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Search Waiter Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()
