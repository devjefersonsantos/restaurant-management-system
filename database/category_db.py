from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *
from utils import empty_entries

class CategoryDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_category(self, name: str, description: str) -> True:
        __entry_items = {"name": name, "description ": description}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO category (name, description)
                                        VALUES (%s, %s) RETURNING category_id;""", (name, description))
                    self.connection.commit()
                    __category_id = self.cursor.fetchone()

                except Exception as error:
                    log_error(f"System user id: {self.__account_id}. An error occurred while creating a category.")
                    messagebox.showerror(title="Create Category Error", message=error)
                else:
                    log_info(f"System user id: {self.__account_id}. Create category with id: {__category_id[0]}.")
                    messagebox.showinfo(title="Create Category", message=f"Category: {name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_categories(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM category
                                    ORDER BY category_id""")
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Categories Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def update_category(self, new_name: str, new_description: str, category_id: str) -> True:
        __entry_items = {"name": new_name, "description ": new_description}
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE category
                                        SET name = %s, description = %s
                                        WHERE category_id = %s""", (new_name, new_description, category_id))
                    self.connection.commit()
                except Exception as error:
                    log_error(f"System user id: {self.__account_id}. An error occurred while updating a category.")
                    messagebox.showerror(title="Update Category Error", message=error)
                else:
                    log_info(f"System user id: {self.__account_id}. Category id: {category_id} has been updated.")
                    messagebox.showinfo(title="Update Category", message=f"Category: {new_name}, updated successfully!")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def delete_category(self, category_id: int) -> None:
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM category
                                    WHERE category_id = %s""", (category_id,))
                self.connection.commit()
            except Exception as error:
                log_error(f"System user id: {self.__account_id}. An error occurred while deleting a category.")
                messagebox.showerror(title="Delete Category Error", message=error)
            else:
                log_warning(f"System user id: {self.__account_id}. Category id: {category_id} was deleted.")
            finally:
                self.cursor.close()
                self.connection.close()

    def search_category(self, typed: str) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM category 
                                    WHERE name LIKE %s""", ("%" + typed + "%",))
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Search Category Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def get_category_id(self, category_name) -> tuple[int]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT category_id FROM category 
                                    WHERE name = %s""", (category_name,))
                result = self.cursor.fetchone()
            except Exception as error:
                messagebox.showerror(title="Search Category Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()
