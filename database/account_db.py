import datetime
import secrets

from tkinter import messagebox

from database import Database
from logs import *
from utils import convert_to_sha3_256
from utils import empty_entries
from utils import restart_software

class LoginDb(Database):
    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.__username = username
        self.__password = password

    def process_login(self) -> str:
        """
        1º Verify account credentials (username, password)
        2ª Set access_token to new token (Account table)
        3ª Set current_login_date to last_login_date (Account table)
        4ª Set current_login_date to CURRENT_TIMESTAMP (Account table)
        5ª return token
        """
        if account_id := self.verify_credentials():
            if self.connect_to_database():
                try:
                    token = secrets.token_hex(32)
                    self.cursor.execute("""UPDATE account
                                        SET access_token = %s,
                                        last_login_date = (SELECT current_login_date FROM account WHERE account_id = %s),
                                        current_login_date = CURRENT_TIMESTAMP
                                        WHERE account_id = %s;""", (convert_to_sha3_256(token), account_id, account_id))
                    self.connection.commit()
                except Exception as error:
                    log_error(f"Login failed. Create access token failed for user with ID: {account_id}.")
                    messagebox.showerror(title="Login Process Failed", message=error)
                else:
                    log_info(f"Login successful. Access token created for user with ID: {account_id}.")
                    return token
                finally:
                    self.connection.close()
                    self.cursor.close()
                    
    def verify_credentials(self) -> int:
        entry_items = {"username":self.__username, "password":self.__password}

        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""SELECT account_id FROM ACCOUNT 
                                        WHERE username = %s AND password = %s;""", (self.__username, 
                                                                                    convert_to_sha3_256(self.__password)))
                    if account_id := self.cursor.fetchone():
                        log_info(f"Successful authentication for user with ID: {account_id[0]}.")
                        return account_id[0]
                    else:
                        log_error("Authentication failed.")
                        messagebox.showerror(title="Login Error", message="Incorrect username or password\nplease try again.")
                except Exception as error:
                    messagebox.showerror(title="Login Error", message=error)
                finally:
                    self.connection.close()
                    self.cursor.close()
    
    def create_access_token(self) -> str:
        if account_id := self.verify_credentials():
            if self.connect_to_database():
                try:
                    token = secrets.token_hex(32)
                    self.cursor.execute("""UPDATE account SET access_token = %s
                                        WHERE username = %s AND password = %s;""", (convert_to_sha3_256(token), 
                                                                                    self.__username, 
                                                                                    convert_to_sha3_256(self.__password)))
                    self.connection.commit()
                except Exception as error:
                    log_error(f"Create access token failed for user with ID: {account_id}.")
                    messagebox.showerror(title="Authentication Failed", message=error)
                else:
                    log_info(f"Access token created for user with ID: {account_id}.")
                    return token
                finally:
                    self.connection.close()
                    self.cursor.close()

    @staticmethod
    def verify_token(func):
        def wrapper(*args, **kwargs):
            database = Database()
            if database.connect_to_database():
                try:
                    cursor = database.connection.cursor()
                    cursor.execute("""SELECT * FROM account
                                   WHERE access_token = %s;""", (convert_to_sha3_256(kwargs["token"]),))
                    if not cursor.fetchone():
                        raise Exception("Authentication Failed")
                except Exception as error:
                    log_error(f"Software closed because an error occurred during token verification.")
                    messagebox.showerror(title="System User Error", message=error)
                    restart_software()
                finally:
                    database.connection.close()
                    cursor.close()
            return func(*args, **kwargs)
        return wrapper

class SignupDb(Database):
    def __init__(self, username: str, password: str, email: str) -> None:
        super().__init__()
        self.__username = username
        self.__password = password
        self.__email = email

        self.create_database()
        
        entry_items = {"username":self.__username, "password":self.__password, "email":self.__email}

        if not empty_entries(**entry_items):
            if self.connect_to_database():
                try:
                    self.cursor.execute("""INSERT INTO account (username, password, email)
                                        VALUES (%s, %s, %s) RETURNING account_id;""", 
                                        (self.__username, convert_to_sha3_256(self.__password), self.__email))
                    self.connection.commit()
                    account_id = self.cursor.fetchone()
                except Exception as error:
                    log_error("An error occurred while creating a account.")
                    messagebox.showerror(title="Sign Up Error", message=error)
                else:
                    log_info(f"Account has been created with ID {account_id[0]}.")
                    messagebox.showinfo(title="Sign Up", message="Congratulations! Your account\nhas been successfully created.")
                finally:
                    self.cursor.close()
                    self.connection.close()

class AccountDb(Database):
    def __init__(self, token) -> None:
        super().__init__()        
        self.__token = convert_to_sha3_256(token)

    def get_account_id(self) -> int:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT account_id FROM account
                                    WHERE access_token = %s;""", (self.__token,))
                result = self.cursor.fetchone()
                if not result:
                    Exception("Authentication Failed")
            except Exception as error:
                messagebox.showerror(title="System User Error", message=error)
                restart_software()
            else:
                return result[0]
            finally:
                self.connection.close()
                self.cursor.close()

    def get_username(self) -> str:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT username FROM account
                                    WHERE access_token = %s""", (self.__token,))
                result = self.cursor.fetchone()
            except Exception as error:
                messagebox.showerror(title="Get Username Error", message=error)
            else:
                return result[0]
            finally:
                self.cursor.close()
                self.connection.close()

    def get_creation_date(self) -> datetime.datetime:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT creation_date FROM account
                                    WHERE access_token = %s""", (self.__token,))
                result = self.cursor.fetchone()
            except Exception as error:
                messagebox.showerror(title="Get Creation Date Error", message=error)
            else:
                return result[0].replace(microsecond=0)
            finally:
                self.cursor.close()
                self.connection.close()

    def get_last_login_date(self) -> datetime.datetime:
        if self.connect_to_database():
            try:
                self.cursor.execute("""SELECT last_login_date FROM account
                                    WHERE access_token = %s""", (self.__token,))
                result = self.cursor.fetchone()
            except Exception as error:
                messagebox.showerror(title="Get Last Login Error", message=error)
            else:
                return result[0].replace(microsecond=0)
            finally:
                self.cursor.close()
                self.connection.close()
