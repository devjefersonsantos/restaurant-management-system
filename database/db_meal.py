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
                                    LEFT JOIN category ca ON ca.id_category = me.category_id_category;""")
                result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Meals Error", message=error)
            else:
                return result
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
