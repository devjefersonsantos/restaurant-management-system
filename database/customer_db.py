from tkinter import messagebox

from database import AccountDb
from database import Database
from logs import *
from utils import empty_entries

class CustomerDb(Database):
    def __init__(self, token) -> None:
        super().__init__()
        self.__account_id = AccountDb(token).get_account_id()

    def create_customer(self, name: str, address: str, cellphone: str, email: str | None) -> True:
        entry_items = {"name": name, "address": address, "cellphone": cellphone}
        
        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, email, account_account_id)
                                        VALUES (%s, %s, %s, %s, %s) RETURNING customer_id;""", (name, address, cellphone, email, self.__account_id))
                    self.connection.commit()
                    customer_id = self.cursor.fetchone()
                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while creating a customer.")
                    messagebox.showerror(title="Create Customer Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Create customer with ID: {customer_id[0]}.")
                    messagebox.showinfo(title="Create Customer", message=f"Customer: {name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_customers(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM customer
                                    ORDER BY customer_id""")
                result = self.cursor.fetchall()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Read Customers Error.")
                messagebox.showerror(title="Read Customers Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def update_customer(self, customer_id: str, name: str, address: str, cellphone: str, email: str | None = None) -> True:
        entry_items = {"name": name, "address": address, "cellphone": cellphone}
        
        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE customer 
                                        SET name = %s, address = %s, cell_phone = %s, email = %s
                                        WHERE customer_id = %s;""", (name, address, cellphone, email, customer_id))
                    self.connection.commit()
                except Exception as error:
                    log_error(f"System user ID: {self.__account_id}. An error occurred while updating a customer.")
                    messagebox.showerror(title="Update Customer Error", message=error)
                else:
                    log_info(f"System user ID: {self.__account_id}. Customer ID: {customer_id} has been updated.")
                    messagebox.showinfo(title="Update Customer", message=f"Customer: {name}, updated successfully!")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()
    
    def delete_customer(self, customer_id: int):
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM customer
                                    WHERE customer_id = %s""", (customer_id,))
                self.connection.commit()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. An error occurred while deleting a customer.")
                messagebox.showerror(title="Delete Customer Error", message=error)
            else:
                log_warning(f"System user ID: {self.__account_id}. Customer ID: {customer_id} was deleted.")
            finally:
                self.cursor.close()
                self.connection.close()

    def search_customer(self, typed: str) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM customer 
                                    WHERE name ILIKE %s""", ("%" + typed + "%",))
                result = self.cursor.fetchall()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Search Customer Error.")
                messagebox.showerror(title="Search Customer Error", message=error)
            else:
                return result
            finally:
                self.cursor.close()
                self.connection.close()

    def get_customer_names(self) -> list[str]:
        if self.connect_to_database():
            try:
                self.cursor.execute("SELECT name FROM customer")
                result = self.cursor.fetchall()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Get Customer Names Error.")
                messagebox.showerror(title="Get Customer Names Error", message=error)
            else:
                return [i[0] for i in result]
            finally:
                self.cursor.close()
                self.connection.close()

    def get_customer_id_by_name(self, customer_name: str) -> int:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT customer_id FROM customer 
                                    WHERE name = %s """, (customer_name,))
                result = self.cursor.fetchone()
            except Exception as error:
                log_error(f"System user ID: {self.__account_id}. Get Customer ID by Name Error.")
                messagebox.showerror(title="Get Customer ID by Name Error", message=error)
            else:
                return result[0]
            finally:
                self.cursor.close()
                self.connection.close()
