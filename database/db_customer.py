from database.database import Database
from utils.empty_entries import empty_entries
from database.db_login import DbLogin
from tkinter import messagebox

class DbCustomer(Database):
    def __init__(self, token):
        super().__init__()
        self.__token = token

    def create_customer(self, name: str, address: str, cellphone: str, email: str | None = None) -> True:
        __entry_items = {"name": name, "address": address, "cellphone": cellphone}
        
        if not empty_entries(**__entry_items):
            __id_account = DbLogin.token_to_id_account(self.__token)
            if self.connect_to_database():
                try:
                    if email is None:
                        self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, account_id_account)
                                            VALUES (%s, %s, %s, %s);""", (name, address, cellphone, __id_account))
                        self.connection.commit()
                    else:
                        self.cursor.execute("""INSERT INTO customer (name, address, cell_phone, email, account_id_account)
                                            VALUES (%s, %s, %s, %s, %s);""", (name, address, cellphone, email, __id_account))
                        self.connection.commit()
                except Exception as error:
                    messagebox.showerror(title="Create Customer Error", message=error)
                else:
                    messagebox.showinfo(title="Create Customer", message=f"Customer: {name}, successfully registered.")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()

    def read_customers(self) -> list[tuple]:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM customer
                                    ORDER BY id_customer""")
                self.result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Read Customers Error", message=error)
            else:
                return self.result
            finally:
                self.cursor.close()
                self.connection.close()

    def update_customer(self, id_customer: str, name: str, address: str, cellphone: str, email: str | None = None) -> True:
        __entry_items = {"name": name, "address": address, "cellphone": cellphone}
        
        if not empty_entries(**__entry_items):
            __id_account = DbLogin.token_to_id_account(self.__token)
            if self.connect_to_database():
                try:
                    self.cursor.execute("""UPDATE customer
                                        SET name = %s, address = %s, cell_phone = %s, account_id_account = %s, email = %s
                                        WHERE id_customer = %s""", (name, address, cellphone, __id_account, email, id_customer))

                    self.connection.commit()
                except Exception as error:
                    messagebox.showerror(title="Update Customer Error", message=error)
                else:
                    messagebox.showinfo(title="Update Customer", message=f"Customer: {name}, updated successfully!")
                    return True
                finally:
                    self.cursor.close()
                    self.connection.close()
    
    def delete_customer(self, id_customer: int):
        if self.connect_to_database():
            try:
                self.cursor.execute("""DELETE FROM customer
                                    WHERE id_customer = %s""", (id_customer,))
                self.connection.commit()
            except Exception as error:
                messagebox.showerror(title="Delete Customer Error", message=error)
            finally:
                self.cursor.close()
                self.connection.close()

    def search_customer(self, typed: str) -> str:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT * FROM customer 
                                    WHERE name LIKE %s""", ("%" + typed + "%",))
                self.result = self.cursor.fetchall()
            except Exception as error:
                messagebox.showerror(title="Search Customer Error", message=error)
            else:
                return self.result
            finally:
                self.cursor.close()
                self.connection.close()
