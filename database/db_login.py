from database.database import Database
from utils.empty_entries import empty_entries
from tkinter import messagebox
import secrets
from database.database import Database
from utils.restart_program import restart_program
from utils.convert_to_sha3_256 import convert_to_sha3_256

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
                                        WHERE username = %s AND password = %s;""", (self.__username, 
                                                                                    convert_to_sha3_256(self.__password)))
                    if self.cursor.fetchone():
                        return True
                    else:
                        messagebox.showerror(title="Login Error", message="Incorrect username or password\nplease try again.")
                except Exception as error:
                    messagebox.showerror(title="Login Error", message=error)
                finally:
                    self.connection.close()
                    self.cursor.close()
    
    def create_access_token(self) -> str:
        if self.verify_credentials():
            if self.connect_to_database():
                try:
                    __token = secrets.token_hex(32)
                    self.cursor.execute("""UPDATE account SET access_token = %s
                                        WHERE username = %s AND password = %s;""", (convert_to_sha3_256(__token), 
                                                                                    self.__username, 
                                                                                    convert_to_sha3_256(self.__password)))
                    self.connection.commit()
                    return __token
                except Exception as error:
                    messagebox.showerror(title="Authentication Failed", message=error)
                finally:
                    self.connection.close()
                    self.cursor.close()
    
    @staticmethod
    def verify_token(func):
        def wrapper(*args, **kwargs):
            __database = Database()
            if __database.connect_to_database():
                try:
                    cursor = __database.connection.cursor()
                    cursor.execute("""SELECT * FROM account
                                   WHERE access_token = %s;""", (convert_to_sha3_256(kwargs["token"]),))
                    if not cursor.fetchone():
                        raise Exception("Authentication Failed")
                except Exception as error:
                    messagebox.showerror(title="System User Error", message=error)
                    restart_program()
                finally:
                    __database.connection.close()
                    cursor.close()
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def token_to_id_account(token) -> int:
        __database = Database()
        if __database.connect_to_database():
            try:
                cursor = __database.connection.cursor()
                cursor.execute("""SELECT id_account FROM account
                               WHERE access_token = %s;""", (convert_to_sha3_256(token),))
                result = cursor.fetchone()
                
                if not result:
                    Exception("Authentication Failed")
            except Exception as error:
                messagebox.showerror(title="System User Error", message=error)
                restart_program()
            else:
                return result[0]
            finally:
                __database.connection.close()
                cursor.close()
