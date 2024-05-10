from tkinter import messagebox

from database import Database
from database import DbLogin
from logs import *
from utils import empty_entries

class DbMeal(Database):
    def __init__(self, token):
        super().__init__()
        self.__id_account = DbLogin.token_to_id_account(token)

    def create_meal(self, meal_name: str, sale_price: float, category_id_category: int, status: str) -> True:
        __entry_items = {
            "meal name": meal_name, 
            "sale price": sale_price, 
            "category_id_category": category_id_category, 
            "status": status
        }
        
        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO meal (meal_name, sale_price, category_id_category, status)
                                        VALUES (%s, %s, %s, %s) RETURNING id_meal;""", (meal_name, sale_price, category_id_category, status))
                    self.connection.commit()
                    __id_meal = self.cursor.fetchone()[0]

                except Exception as error:
                    log_error(f"System user id: {self.__id_account}. An error occurred while creating a meal.")
                    messagebox.showerror(title="Create Meal Error", message=error)
                else:
                    log_info(f"System user id: {self.__id_account}. Create meal with id: {__id_meal}.")
                    messagebox.showinfo(title="Create Meal", message=f"Meal: {meal_name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_meals(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT me.id_meal, me.meal_name, me.sale_price, ca.name, me.status
                                    FROM meal me
                                    LEFT JOIN category ca ON ca.id_category = me.category_id_category
                                    ORDER BY me.id_meal;""")
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Meals Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def update_meal(self, id_meal: int, meal_name: str, sale_price: float, category_id_category: int, status: str) -> True:
        __entry_items = {
            "meal name": meal_name, 
            "sale price": sale_price, 
            "category_id_category": category_id_category, 
            "status": status
        }

        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE meal 
                                        SET meal_name = %s, sale_price = %s, category_id_category = %s, status = %s
                                        WHERE id_meal = %s;""", (meal_name, sale_price, category_id_category, status, id_meal))
                    self.connection.commit()
                except Exception as error:
                    log_error(f"System user id: {self.__id_account}. An error occurred while updating a meal.")
                    messagebox.showerror(title="Update Meal Error", message=error)
                else:
                    log_info(f"System user id: {self.__id_account}. Meal id: {id_meal} has been updated.")
                    messagebox.showinfo(title="Update meal", message=f"Meal: {meal_name}, updated successfully!")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def delete_meal(self, id_meal: int) -> None:
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM meal
                                    WHERE id_meal = %s""", (id_meal,))
                self.connection.commit()
            except Exception as error:
                log_error(f"System user id: {self.__id_account}. An error occurred while deleting a meal.")
                messagebox.showerror(title="Delete Meal Error", message=error)
            else:
                log_warning(f"System user id: {self.__id_account}. Meal id: {id_meal} was deleted.")
            finally:
                self.cursor.close()
                self.connection.close()

    def search_meal(self, typed: str) -> str:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM meal 
                                    WHERE meal_name LIKE %s""", ("%" + typed + "%",))
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Search Meal Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()
