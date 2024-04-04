import mysql.connector
import json

class Database:
    def db_logged(self) -> bool:
        try:
            with open("database/config.json", "r") as file:
                config = json.load(file)
            mysql_connection = mysql.connector.connect(**config)
        except:
            return False
        else:
            mysql_connection.close()
            return True
