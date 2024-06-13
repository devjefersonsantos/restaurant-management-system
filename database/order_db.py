from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *
from utils import number_of_items

class OrderDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_order_id(self, waiter_id: int | None, customer_id: int | None) -> int:
        if self.connect_to_database():
            try:
                self.cursor.execute("""INSERT INTO "order" (waiter_waiter_id, customer_customer_id)
                                    VALUES (%s, %s) RETURNING order_id;""", (waiter_id, customer_id))
                self.connection.commit()
                order_id = self.cursor.fetchone()

            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while creating a order.")
                messagebox.showerror(title="Create Order ID Error", message=error)
            else:
                log_info(f"System user ID: {self.__account_id}. Order created with ID: {order_id[0]}.")
                messagebox.showinfo(title=None, message="order created successfully")
                return order_id[0]
            finally:
                self.cursor.close()
                self.connection.close()

    def read_order_list(self, order_id: int) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT meal.meal_name, order_has_meal.quantity 
                                    FROM order_has_meal
                                    JOIN meal ON order_has_meal.meal_id = meal.meal_id
                                    WHERE order_has_meal.order_id = %s;""", (order_id,))
                result = self.cursor.fetchall()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Read Order List Error.")
                messagebox.showerror(title="Read Order List Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()
                
    def add_meal_to_order(self, order_id: int, meals_ids: list) -> None:
        if self.connect_to_database():
            try:
                meals_ids_and_quantity : dict = number_of_items(meals_ids)

                for i in meals_ids_and_quantity.items():
                    self.cursor.execute("""INSERT INTO order_has_meal (order_id, meal_id, quantity)
                                        VALUES (%s, %s, %s);""", (order_id, i[0], i[1]))
                self.connection.commit()

            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while adding meals to the order.")
                messagebox.showerror(title="Add Meal To Order Error", message=error)
            else:
                log_info(f"System user ID: {self.__account_id}. Meal id, quantity: {meals_ids_and_quantity}, added to order {order_id}.")
            finally:
                self.cursor.close()
                self.connection.close()
