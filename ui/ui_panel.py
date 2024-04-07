import customtkinter
from utils.clear_frames import clear_frames
from database.db_login import DbLogin

class Ui_panel:
    def __init__(self, root: customtkinter.CTk, token: str):
        self.root = root
        self.__token = token
        DbLogin.verify_token(self.__token)

        clear_frames(self.root)        
        self.root.geometry("1920x1012-8-2")
