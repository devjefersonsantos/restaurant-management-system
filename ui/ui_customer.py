import customtkinter
from database.db_login import DbLogin

class UiCustomer:
    def __init__(self, root: customtkinter.CTk, square_frame: customtkinter.CTk, token: str):
        self.root = root
        self.square_frame = square_frame
        self.__token = token
        DbLogin.verify_token(self.__token)
