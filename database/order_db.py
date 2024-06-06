from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *

class OrderDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_order_id(self, waiter_id: int | None, customer_id: int | None) -> True:
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
                log_info(f"System user ID: {self.__account_id}. order created with ID: {order_id}.")
                messagebox.showinfo(title=None, message="order created successfully")
                return True
            finally:
                self.cursor.close()
                self.connection.close()
