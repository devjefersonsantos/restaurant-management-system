import customtkinter
from database.db_login import DbLogin
from utils.clear_frames import clear_frames

class UiHome:
    def __init__(self, root: customtkinter.CTk, square_frame: customtkinter.CTk, token: str):
        self.root = root
        self.square_frame = square_frame
        self.__token = token
        DbLogin.verify_token(self.__token)

        clear_frames(self.square_frame)
        self.ui_home()

    def topbar(self):
        topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                              font=("arial black", 25),
                                              text_color="#ffffff", 
                                              text="Home")
        topbar_label.place(x=20, y=5)

    def ui_home(self):
        self.topbar()
