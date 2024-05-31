from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *
from utils import empty_entries

class CategoryDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_category(self, category_name: str, description: str) -> True:
        entry_items = {"category name": category_name, "description ": description}
        
        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO category (category_name, description)
                                        VALUES (%s, %s) RETURNING category_id;""", (category_name, description))
                    self.connection.commit()
                    category_id = self.cursor.fetchone()

                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while creating a category.")
                    messagebox.showerror(title="Create Category Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Create category with ID: {category_id[0]}.")
                    messagebox.showinfo(title="Create Category", message=f"Category: {category_name}, successfully registered.")
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

    def update_category(self, new_category_name: str, new_description: str, category_id: str) -> True:
        entry_items = {"category_name": new_category_name, "description ": new_description}
        
        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE category
                                        SET category_name = %s, description = %s
                                        WHERE category_id = %s""", (new_category_name, new_description, category_id))
                    self.connection.commit()
                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while updating a category.")
                    messagebox.showerror(title="Update Category Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Category ID: {category_id} has been updated.")
                    messagebox.showinfo(title="Update Category", message=f"Category: {new_category_name}, updated successfully!")
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
                log_error(f"System user ID: {self.__account_id}. An error occurred while deleting a category.")
                messagebox.showerror(title="Delete Category Error", message=error)
            else:
                log_warning(f"System user ID: {self.__account_id}. Category ID: {category_id} was deleted.")
            finally:
                self.cursor.close()
                self.connection.close()

    def search_category(self, typed: str) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM category 
                                    WHERE category_name ILIKE %s""", ("%" + typed + "%",))
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
                                    WHERE category_name = %s""", (category_name,))
                result = self.cursor.fetchone()
            except Exception as error:
                messagebox.showerror(title="Search Category Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def get_category_names(self) -> list[str]:
        if self.connect_to_database():
            try:
                self.cursor.execute("SELECT category_name FROM category")
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Get Category Names Error", message=error)
            else:
                return [i[0] for i in result]
            finally:
                self.cursor.close()
                self.connection.close()
