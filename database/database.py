import json
from tkinter import messagebox

import psycopg2

class Database:
    def connect_to_database(self, database: str | None = "restaurant_management_system") -> True:
        try:
            with open("./database/config.json", "r") as file:
                data = json.load(file)
                user = data["user"]
                password = data["password"]
                host = data["host"]
                port = data["port"]

            self.connection = psycopg2.connect(user=user,
                                               password=password,
                                               host=host,
                                               port=port,
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
    
    def create_database(self) -> None:
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
                                    account_id SERIAL PRIMARY KEY,
                                    access_token VARCHAR(255), 
                                    username VARCHAR(10) NOT NULL UNIQUE, 
                                    password VARCHAR(255) NOT NULL,
                                    email VARCHAR(255) NOT NULL UNIQUE,
                                    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    last_login_date TIMESTAMP,
                                    current_login_date TIMESTAMP
                                    )""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS customer (
                                    customer_id SERIAL PRIMARY KEY,
                                    name VARCHAR(255) NOT NULL UNIQUE,
                                    address VARCHAR(255) NOT NULL,
                                    cell_phone VARCHAR(13) NOT NULL,
                                    email VARCHAR(255) UNIQUE,
                                    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    account_account_id INT NOT NULL,
                                    CONSTRAINT fk_customer_account
                                        FOREIGN KEY (account_account_id)
                                        REFERENCES account (account_id)
                                    )""")

                self.cursor.execute("""CREATE TABLE IF NOT EXISTS waiter (
                                    waiter_id SERIAL PRIMARY KEY,
                                    name VARCHAR(255) NOT NULL UNIQUE,
                                    cell_phone VARCHAR(13) NOT NULL,
                                    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                                    )""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS category (
                                    category_id SERIAL PRIMARY KEY,
                                    category_name VARCHAR(255) NOT NULL UNIQUE,
                                    description VARCHAR(300)
                                    )""")

                self.cursor.execute("""CREATE TABLE IF NOT EXISTS meal (
                                    meal_id SERIAL PRIMARY KEY,
                                    meal_name VARCHAR(255) NOT NULL UNIQUE,
                                    sale_price DECIMAL(10,2) NOT NULL,
                                    category_category_id INT NOT NULL,
                                    status VARCHAR(10) CHECK (status IN ('Disabled', 'Enabled')) NOT NULL,
                                    CONSTRAINT fk_meal_category
                                        FOREIGN KEY (category_category_id)
                                        REFERENCES category (category_id)
                                    )""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS "order" (
                                    order_id SERIAL PRIMARY KEY,
                                    start_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    waiter_waiter_id INT,
                                    customer_customer_id INT,
                                    payment DECIMAL(10,2),
                                    end_time TIMESTAMP,
                                    CONSTRAINT fk_order_customer
                                        FOREIGN KEY (customer_customer_id)
                                        REFERENCES customer (customer_id),
                                    CONSTRAINT fk_order_waiter
                                        FOREIGN KEY (waiter_waiter_id)
                                        REFERENCES waiter (waiter_id)
                                    )""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS order_has_meal (
                                    order_id INT NOT NULL,
                                    meal_id INT NOT NULL,
                                    quantity INT NOT NULL,
                                    PRIMARY KEY (order_id, meal_id),
                                    CONSTRAINT fk_order_has_meal_meal
                                        FOREIGN KEY (meal_id)
                                        REFERENCES meal (meal_id),
                                    CONSTRAINT fk_order_has_meal_order
                                        FOREIGN KEY (order_id)
                                        REFERENCES "order" (order_id)
                                    )""")
                
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS "table" (
                                    table_id SERIAL PRIMARY KEY,
                                    order_order_id INT,
                                    CONSTRAINT fk_table_order
                                        FOREIGN KEY (order_order_id)
                                        REFERENCES "order" (order_id)
                                    )""")

                self.connection.commit()
            except Exception as error:
                messagebox.showerror(title="Database Error", message=error)
            else:
                self.connection.close()
                self.cursor.close()

    @staticmethod
    def database_status() -> bool:
        try:
            with open("./database/config.json", "r") as file:
                config = json.load(file)
            connection = psycopg2.connect(**config, database=None)
        except:
            return False
        else:
            connection.close()
            return True
