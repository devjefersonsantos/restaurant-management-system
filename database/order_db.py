from tkinter import messagebox
from datetime import datetime

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

    def update_order_meals(self, order_id: int, previous_meals_ids: list[int], meals_ids: list[int]) -> None:
        if self.connect_to_database():
            try:
                meals_ids_and_quantity: dict = number_of_items(meals_ids)

                for meal_id, quantity in meals_ids_and_quantity.items():
                    self.cursor.execute("""
                        INSERT INTO order_has_meal (order_id, meal_id, quantity)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (order_id, meal_id)
                        DO UPDATE SET quantity = EXCLUDED.quantity""", 
                        (order_id, meal_id, quantity))
                self.connection.commit()

            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while updating order meals.")
                messagebox.showerror(title="Update Order Meals", message=error)
            else:
                previous_meals_ids = number_of_items(previous_meals_ids)
                log_info(f"System user ID: {self.__account_id}. Meal id, quantity: {previous_meals_ids} to {meals_ids_and_quantity}, updated Order ID: {order_id}.")
            finally:
                self.cursor.close()
                self.connection.close()

    def delete_meals_from_order(self, order_id: int, *meal_ids: int) -> None:
        if self.connect_to_database():
            try:
                for meal_id in meal_ids:
                    self.cursor.execute("""DELETE FROM order_has_meal
                                        WHERE order_id = %s and meal_id = %s;""", 
                                        (order_id, meal_id,))
                self.connection.commit()

            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while deleting a meal from the order.")
                messagebox.showerror(title="Delete Meals From Order Error", message=error)
            else:
                log_warning(f"System user ID: {self.__account_id}. Meal ID: {meal_ids} was deleted from Order ID {order_id}.")
            finally:
                self.cursor.close()
                self.connection.close()

    def add_meal_to_order(self, order_id: int, meals_ids: list[int]) -> None:
        if self.connect_to_database():
            try:
                meals_ids_and_quantity : dict = number_of_items(meals_ids)

                for meal_id, quantity in meals_ids_and_quantity.items():
                    self.cursor.execute("""INSERT INTO order_has_meal (order_id, meal_id, quantity)
                                        VALUES (%s, %s, %s);""", (order_id, meal_id, quantity))
                self.connection.commit()

            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while adding meals to the order.")
                messagebox.showerror(title="Add Meal To Order Error", message=error)
            else:
                log_info(f"System user ID: {self.__account_id}. Meal id, quantity: {meals_ids_and_quantity}, added to order {order_id}.")
            finally:
                self.cursor.close()
                self.connection.close()

    def get_monthly_sales(self) -> list[int]:
        if self.connect_to_database():
            try:
                current_year = datetime.now().year
                monthly_sales = list()
                for i in range(1, 13):
                    self.cursor.execute("""SELECT SUM(payment) FROM "order"
                                        WHERE EXTRACT(MONTH FROM end_time) = %s
                                        AND EXTRACT(YEAR FROM end_time) = %s;""", (i, current_year))
                    result = self.cursor.fetchone()
                    monthly_sales.append(result[0] if result and result[0] != None else 0)
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Get Monthly Sales Error.")
                messagebox.showerror(title="Get Monthly Sales Error", message=error)
            else:     
                return monthly_sales
            finally:
                self.cursor.close()
                self.connection.close()
