from database.database import Database
from utils.empty_entries import empty_entries
from tkinter import messagebox
import secrets
from database.database import Database
from utils.restart_program import restart_program

class DbLogin(Database):
    def __init__(self, username: str, password: str):
        super().__init__()
        self.__username = username
        self.__password = password

    def verify_credentials(self) -> True:
        __entry_items = {"username":self.__username, "password":self.__password}

        if not empty_entries(**__entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""SELECT * FROM ACCOUNT 
                                        WHERE username = %s AND password = SHA2(%s, 256);""", (self.__username, self.__password))
                    if self.cursor.fetchone():
                        return True
                    else:
                        messagebox.showerror(title=None, message="Incorrect username or password\nplease try again.")
                except Exception as error:
                    messagebox.showerror(title=None, message=error)
                finally:
                    self.mysql_connection.close()
                    self.cursor.close()
    
    def create_access_token(self) -> str:
        if self.verify_credentials():
            if self.connect_to_database():
                try:
                    __token = secrets.token_hex(32)
                    self.cursor.execute("""UPDATE account SET access_token = SHA2(%s, 256) 
                                        WHERE username = %s AND password = SHA2(%s, 256);""", (__token, self.__username, self.__password))
                    self.mysql_connection.commit()
                    return __token
                except Exception as error:
                    messagebox.showerror(title=None, message=error)
                finally:
                    self.mysql_connection.close()
                    self.cursor.close()
    
    @staticmethod
    def verify_token(func):
        def wrapper(*args, **kwargs):
            __database = Database()
            if __database.connect_to_database():
                try:
                    cursor = __database.mysql_connection.cursor()
                    cursor.execute("""SELECT * FROM account
                                   WHERE access_token = SHA2(%s, 256);""", (kwargs["token"],))
                    if not cursor.fetchone():
                        restart_program()
                except Exception as error:
                    messagebox.showerror(title=None, message=error)
                finally:
                    __database.mysql_connection.close()
                    cursor.close()
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def token_to_id_account(token) -> int:
        __database = Database()
        if __database.connect_to_database():
            try:
                cursor = __database.mysql_connection.cursor()
                cursor.execute("""SELECT id_account FROM account
                               WHERE access_token = SHA2(%s, 256);""", (token,))
                result = cursor.fetchone()
                
                if not result:
                    restart_program()
            except Exception as error:
                messagebox.showerror(title=None, message=error)
            else:
                return result[0]
            finally:
                __database.mysql_connection.close()
                cursor.close()
