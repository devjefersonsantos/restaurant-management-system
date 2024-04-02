import mysql.connector
import json

class DbConnection:
    def db_logged(self) -> bool:
        mysql_connection = None
        try:
            with open("database/connection/config.json") as __file:
                __data = json.load(__file)
                __host = __data["host"]
                __user = __data["user"]
                __password = __data["password"]
            
            mysql_connection = mysql.connector.connect(
                host=__host,
                user=__user,
                password=__password,
                database= None
            )
            mysql_connection.cursor()
        except:
            return False
        else:
            return True
        finally:
            if mysql_connection:
                mysql_connection.close()
