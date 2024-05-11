from tkinter import messagebox

from database import Database
from database import DbLogin
from logs import *
from utils.empty_entries import empty_entries

class DbWaiter(Database):
    def __init__(self, token):
        super().__init__()
        self.__id_account = DbLogin.token_to_id_account(token)

    def create_waiter(self, name: str, cellphone: str) -> True:
        __entry_items = {"name": name, "cellphone ": cellphone}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO waiter (name, cell_phone)
                                        VALUES (%s, %s) RETURNING id_waiter;""", (name, cellphone))
                    self.connection.commit()
                    __id_waiter = self.cursor.fetchone()

                except Exception as error:
                    log_error(f"System user id: {self.__id_account}. An error occurred while creating a waiter.")
                    messagebox.showerror(title="Create Waiter Error", message=error)
                else:
                    log_info(f"System user id: {self.__id_account}. Create waiter with id: {__id_waiter[0]}.")
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
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Waiters Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def update_waiter(self, new_name: str, new_cellphone: str, id_waiter: int) -> True:
        __entry_items = {"name": new_name, "cellphone": new_cellphone}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE waiter
                                        SET name = %s, cell_phone = %s
                                        WHERE id_waiter = %s""", (new_name, new_cellphone, id_waiter))

                    self.connection.commit()
                except Exception as error:
                    log_error(f"System user id: {self.__id_account}. An error occurred while updating a waiter.")
                    messagebox.showerror(title="Update Waiter Error", message=error)
                else:
                    log_info(f"System user id: {self.__id_account}. Waiter id: {id_waiter} has been updated.")
                    messagebox.showinfo(title="Update Waiter", message=f"Waiter: {new_name}, updated successfully!")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def delete_waiter(self, id_waiter: int) -> None:
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM waiter
                                    WHERE id_waiter = %s""", (id_waiter,))
                self.connection.commit()
            except Exception as error:
                log_error(f"System user id: {self.__id_account}. An error occurred while deleting a waiter.")
                messagebox.showerror(title="Delete Waiter Error", message=error)
            else:
                log_warning(f"System user id: {self.__id_account}. Waiter id: {id_waiter} was deleted.")
            finally:
                self.cursor.close()
                self.connection.close()

    def search_waiter(self, typed: str) -> str:
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
