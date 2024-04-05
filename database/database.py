import mysql.connector
import json
from tkinter import messagebox

class Database:
    def connect_to_database(self, database: str | None = "RESTAURANT_MANAGEMENTSYSTEM") -> True:
        try:
            with open("database/config.json", "r") as file:
                config = json.load(file)
            self.mysql_connection = mysql.connector.connect(**config, database=database)
            self.cursor = self.mysql_connection.cursor()
            return True
        except Exception as error:
            messagebox.showerror(title=None, message=error)
    
    def create_database(self):
        if self.connect_to_database(database=None):
            try:
                self.cursor.execute("CREATE DATABASE IF NOT EXISTS RESTAURANT_MANAGEMENTSYSTEM;")
                self.cursor.execute("USE RESTAURANT_MANAGEMENTSYSTEM;")

                self.cursor.execute("""CREATE TABLE IF NOT EXISTS ACCOUNT (
                                    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
                                    username VARCHAR(50) NOT NULL UNIQUE, 
                                    password VARCHAR(255) NOT NULL,
                                    email VARCHAR(255) NOT NULL);""")
                self.mysql_connection.commit()
            except Exception as error:
                messagebox.showerror(title=None, message=error)
            else:
                self.mysql_connection.close()
                self.cursor.close()

    @staticmethod
    def db_status() -> bool:
        try:
            with open("database/config.json", "r") as file:
                config = json.load(file)
            mysql_connection = mysql.connector.connect(**config)
        except:
            return False
        else:
            mysql_connection.close()
            return True
