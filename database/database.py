import psycopg2
import json
from tkinter import messagebox

class Database:
    def connect_to_database(self, database: str | None = "restaurant_management_system") -> True:
        try:
            with open("database/config.json", "r") as __file:
                __data = json.load(__file)
                __user = __data["user"]
                __password = __data["password"]
                __host = __data["host"]
                __port = __data["port"]

            self.connection = psycopg2.connect(user=__user,
                                               password=__password,
                                               host=__host,
                                               port=__port,
                                               database=database)
            self.cursor = self.connection.cursor()

            return True
        except UnicodeDecodeError as error:
            if database:
                messagebox.showerror(title="Login Error", message="First, set up the connection\nand then create an account.")
            else:
                messagebox.showerror(title="Database Error", message=error)
        except Exception as error:
            messagebox.showerror(title="Database Error", message=error)
    
    def create_database(self):
        # https://stackoverflow.com/questions/44511958/python-postgresql-create-database-if-not-exists-is-error
        if self.connect_to_database(database=None):
            try:
                try:
                    self.connection.autocommit = True
                    self.cursor.execute("CREATE DATABASE restaurant_management_system;")
                except:
                    pass
                finally:
                    self.connection.close()
                    self.cursor.close()
                
                self.connect_to_database()

                self.cursor.execute("""CREATE TABLE IF NOT EXISTS account (
                                    id_account SERIAL PRIMARY KEY,
                                    access_token VARCHAR(255), 
                                    username VARCHAR(10) NOT NULL UNIQUE, 
                                    password VARCHAR(255) NOT NULL,
                                    email VARCHAR(255) NOT NULL);""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS customer (
                                    id_customer SERIAL PRIMARY KEY,
                                    name VARCHAR(255) NOT NULL,
                                    address VARCHAR(255) NOT NULL,
                                    cell_phone VARCHAR(13) NOT NULL,
                                    email VARCHAR(255),
                                    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    account_id_account INT NOT NULL,
                                    CONSTRAINT fk_customer_account
                                        FOREIGN KEY (account_id_account)
                                        REFERENCES account (id_account));""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS waiter (
                                    id_waiter SERIAL PRIMARY KEY,
                                    name VARCHAR(255) NOT NULL,
                                    cell_phone VARCHAR(13) NOT NULL,
                                    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS category (
                                    id_category SERIAL PRIMARY KEY,
                                    name VARCHAR(255) NOT NULL,
                                    description VARCHAR(300));""")

                self.cursor.execute("""CREATE TABLE IF NOT EXISTS meal (
                                    id_meal SERIAL PRIMARY KEY,
                                    meal_name VARCHAR(255) NOT NULL,
                                    sale_price DECIMAL(10,2) NOT NULL,
                                    category_id_category INT NOT NULL,
                                    status VARCHAR(10) CHECK (status IN ('Disabled', 'Enabled')) NOT NULL,
                                    CONSTRAINT fk_meal_category
                                        FOREIGN KEY (category_id_category)
                                        REFERENCES category (id_category));""")
                
                self.connection.commit()
            except Exception as error:
                messagebox.showerror(title="Database Error", message=error)
            else:
                self.connection.close()
                self.cursor.close()

    @staticmethod
    def database_status() -> bool:
        try:
            with open("database/config.json", "r") as file:
                config = json.load(file)
            connection = psycopg2.connect(**config, database=None)
        except:
            return False
        else:
            connection.close()
            return True
