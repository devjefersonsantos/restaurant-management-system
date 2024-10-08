from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *
from utils import empty_entries

class MealDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_meal(self, meal_name: str, sale_price: float, category_category_id: int, status: str) -> True:
        entry_items = {
            "meal name": meal_name, 
            "sale price": sale_price, 
            "category": category_category_id, 
            "status": status
        }
        
        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO meal (meal_name, sale_price, category_category_id, status)
                                        VALUES (%s, %s, %s, %s) RETURNING meal_id;""", (meal_name, sale_price, category_category_id, status))
                    self.connection.commit()
                    meal_id = self.cursor.fetchone()

                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while creating a meal.")
                    messagebox.showerror(title="Create Meal Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Create meal with ID: {meal_id[0]}.")
                    messagebox.showinfo(title="Create Meal", message=f"Meal: {meal_name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_meals(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT me.meal_id, me.meal_name, me.sale_price, ca.category_name, me.status
                                    FROM meal me
                                    LEFT JOIN category ca ON ca.category_id = me.category_category_id
                                    ORDER BY me.meal_id;""")
                result = self.cursor.fetchall()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Read Meals Error.")
                messagebox.showerror(title="Read Meals Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def update_meal(self, meal_id: int, meal_name: str, sale_price: float, category_category_id: int, status: str) -> True:
        entry_items = {
            "meal name": meal_name, 
            "sale price": sale_price, 
            "category": category_category_id, 
            "status": status
        }

        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE meal 
                                        SET meal_name = %s, sale_price = %s, category_category_id = %s, status = %s
                                        WHERE meal_id = %s;""", (meal_name, sale_price, category_category_id, status, meal_id))
                    self.connection.commit()
                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while updating a meal.")
                    messagebox.showerror(title="Update Meal Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Meal ID: {meal_id} has been updated.")
                    messagebox.showinfo(title="Update meal", message=f"Meal: {meal_name}, updated successfully!")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def delete_meal(self, meal_id: int) -> True:
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM meal
                                    WHERE meal_id = %s""", (meal_id,))
                self.connection.commit()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while deleting a meal.")
                messagebox.showerror(title="Delete Meal Error", message=error)
            else:
                log_warning(f"System user ID: {self.__account_id}. Meal ID: {meal_id} was deleted.")
                return True
            finally:
                self.cursor.close()
                self.connection.close()

    def search_meal(self, typed: str) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT me.meal_id, me.meal_name, me.sale_price, ca.category_name, me.status
                                    FROM meal me
                                    LEFT JOIN category ca ON ca.category_id = me.category_category_id
                                    WHERE meal_name ILIKE %s
                                    ORDER BY me.meal_id""", ("%" + typed + "%",))
                result = self.cursor.fetchall()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Search Meal Error.")
                messagebox.showerror(title="Search Meal Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def count_meals(self) -> int:
        if self.connect_to_database():
            try:
                self.cursor.execute("SELECT COUNT(*) FROM meal")
                result = self.cursor.fetchone()
                return result[0]
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Count Meals Error.")
                messagebox.showerror(title="Count Meals Error", message=error)
            finally:
                self.cursor.close()
                self.connection.close()

    def count_meals_by_status(self, status:str) -> int:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT COUNT(*) FROM meal
                                    WHERE status = %s""", (status,))
                result = self.cursor.fetchone()
                return result[0]
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Count Meals by Status.")
                messagebox.showerror(title="Count Meals by Status", message=error)
            finally:
                self.cursor.close()
                self.connection.close()
