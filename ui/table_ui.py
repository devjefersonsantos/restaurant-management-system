import customtkinter

from utils.colors import *
from database.account_db import LoginDb
from utils import clear_frames

class TableUi:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self._root = root
        self._square_frame = square_frame
        self.__token = token

        clear_frames(self._square_frame)

        self._table_ui()

    def _topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        self._topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                                    font=("arial black", 25),
                                                    text_color=WHITE_COLOR, 
                                                    text="Table")
        self._topbar_label.place(x=20, y=5)

    def _table_ui(self) -> None:
        clear_frames(self._square_frame)

        self._topbar()
