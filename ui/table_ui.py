import tkinter
from tkinter import Toplevel

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
                                                    text_color=WHITE_COLOR,
                                                    font=("arial black", 25),
                                                    text="Table")
        self._topbar_label.place(x=20, y=5)

        self._addtable_button = customtkinter.CTkButton(master=topbar_frame,
                                                        width=230, height=32,
                                                        fg_color=GREEN_COLOR,
                                                        hover_color=GREEN_HOVER_COLOR,
                                                        text_color=WHITE_COLOR,
                                                        corner_radius=4,
                                                        font=("arial", 15), 
                                                        text="Add Table",
                                                        command=self.__create_table_ui)
        self._addtable_button.place(x=1425, y=9)

    def _table_ui(self) -> None:
        self._topbar()

    def __create_table_ui(self):
        try:
            self.__table_toplevel.destroy()
        except:
            pass

        self.__table_toplevel = Toplevel(master=self._root)
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("images/global_images/icon.ico")) # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.title("Add Total Tables")
        self.__table_toplevel.geometry("390x70+760+25")
        self.__table_toplevel.resizable(False, False)
        
        only_numbers = self._root.register(lambda _ : _.isdigit())

        quantity_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 17),
                                                text="Quantity")
        quantity_label.place(x=95, y=0)

        add_table_spinbox = tkinter.Spinbox(master=self.__table_toplevel,
                                            width=17,
                                            validate="key",
                                            validatecommand=(only_numbers, "%P"),
                                            font=("arial bold", 16),
                                            from_=0, to=100)
        add_table_spinbox.place(x=5, y=28)

        add_table_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                   width=150, height=30,
                                                   text_color=WHITE_COLOR,
                                                   fg_color=GREEN_COLOR,
                                                   hover_color=GREEN_HOVER_COLOR,
                                                   corner_radius=4,
                                                   font=("arial", 15), 
                                                   text="Add Table")
        add_table_button.place(x=235, y=28)
