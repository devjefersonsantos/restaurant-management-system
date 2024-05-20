import tkinter
from tkinter import Toplevel
from tkinter import messagebox

import customtkinter

from utils.colors import *
from database.account_db import LoginDb
from database import TableDb
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
        self.__table_ui()
        
    def _topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        _topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                               text_color=WHITE_COLOR,
                                               font=("arial black", 25),
                                               text="Table")
        _topbar_label.place(x=20, y=5)

        __delete_table_button = customtkinter.CTkButton(master=topbar_frame,
                                                        width=197, height=32,
                                                        fg_color=RED_COLOR, 
                                                        hover_color=RED_HOVER_COLOR,
                                                        text_color=WHITE_COLOR,
                                                        corner_radius=4,
                                                        font=("arial", 15), 
                                                        text="Delete Table",
                                                        command=self.__delete_table_ui)
        __delete_table_button.place(x=1249, y=9)

        __create_table_button = customtkinter.CTkButton(master=topbar_frame,
                                                        width=197, height=32,
                                                        fg_color=GREEN_COLOR,
                                                        hover_color=GREEN_HOVER_COLOR,
                                                        text_color=WHITE_COLOR,
                                                        corner_radius=4,
                                                        font=("arial", 15), 
                                                        text="Add Table",
                                                        command=self.__create_table_ui)
        __create_table_button.place(x=1455, y=9)

    def __table_ui(self) -> None:
        self._topbar()
        
        # https://www.youtube.com/watch?v=Envp9yHb2Ho
        __table_screen_frame = customtkinter.CTkFrame(master=self._square_frame, 
                                                      width=1678, height=962,
                                                      corner_radius=0)
        __table_screen_frame.place(x=0, y=50)

        __table_screen_canvas = tkinter.Canvas(master=__table_screen_frame, width=1678, height=858)
        __table_screen_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

        __table_scrollbar = tkinter.Scrollbar(master=__table_screen_frame, 
                                              orient=tkinter.VERTICAL, 
                                              command=__table_screen_canvas.yview)
        __table_scrollbar.place(x=1660, y=0, height=858)

        __table_screen_canvas.configure(yscrollcommand=__table_scrollbar.set)

        ###########################################################################################
        def configure_scroll_region(event) -> None:
            __table_screen_canvas.configure(scrollregion=__table_screen_canvas.bbox("all"))
        ###########################################################################################
        __table_screen_canvas.bind("<Configure>", configure_scroll_region)

        __window_frame = tkinter.Frame(master=__table_screen_canvas)
        __table_screen_canvas.create_window((0,0), window=__window_frame, anchor="nw")

        __tables = TableDb(self.__token).read_tables()
        table_row = table_column = 0

        for table in __tables:
            __table_button = customtkinter.CTkButton(master=__window_frame,
                                                     width=197, height=140,
                                                     fg_color=GREEN_COLOR,
                                                     hover_color=GREEN_HOVER_COLOR,
                                                     font=("arial bold", 20),
                                                     text=table[0])
            __table_button.grid(row=table_row, column=table_column, padx=5, pady=5)

            table_column += 1
            if table_column == 8:
                table_row += 1
                table_column = 0

    def __create_table_ui(self) -> None:
        try:
            self.__table_toplevel.destroy()
        except:
            pass

        self.__table_toplevel = Toplevel(master=self._root)
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("images/global_images/icon.ico")) 
        self.__table_toplevel.title("Add Total Tables")
        self.__table_toplevel.geometry("420x71+760+28")
        self.__table_toplevel.resizable(False, False)
        
        only_numbers = self._root.register(lambda _ : _.isdigit())

        quantity_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 17),
                                                text="Quantity")
        quantity_label.place(x=95, y=0)

        create_table_spinbox = tkinter.Spinbox(master=self.__table_toplevel,
                                               width=17,
                                               validate="key",
                                               validatecommand=(only_numbers, "%P"),
                                               font=("arial bold", 16),
                                               from_=0, to=100)
        create_table_spinbox.grid(row=0, column=0, padx=5, pady=29)

        create_table_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                      width=180, height=30,
                                                      text_color=WHITE_COLOR,
                                                      fg_color=GREEN_COLOR,
                                                      hover_color=GREEN_HOVER_COLOR,
                                                      corner_radius=4,
                                                      font=("arial", 15), 
                                                      text="Add Table",
                                                      command=lambda:self.__fn_create_table(multiplier=int(create_table_spinbox.get())))
        create_table_button.grid(row=0, column=1)

    def __delete_table_ui(self) -> None:
        try:
            self.__table_toplevel.destroy()
        except:
            pass

        self.__table_toplevel = Toplevel(master=self._root)
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("images/global_images/icon.ico")) 
        self.__table_toplevel.title("Delete Table")
        self.__table_toplevel.geometry("426x54+760+35")
        self.__table_toplevel.resizable(False, False)

        __delete_table_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
                                                                width=230, height=30,
                                                                text_color=GRAY_TEXT_COLOR,
                                                                fg_color=WHITE_COLOR,
                                                                button_color=OPTION_MENU_BUTTON_COLOR,
                                                                button_hover_color=OPTION_MENU_HOVER_COLOR,
                                                                corner_radius=4,
                                                                font=("arial", 17),
                                                                dropdown_font=("arial", 15),
                                                                values=[str(i[0]) for i in TableDb(self.__token).get_table_ids()])
        __delete_table_optionmenu.grid(row=0, column=0, padx=5, pady=12)
        
        __delete_table_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                        width=180, height=30,
                                                        text_color=WHITE_COLOR,
                                                        fg_color=RED_COLOR,
                                                        hover_color=RED_HOVER_COLOR,
                                                        corner_radius=4,
                                                        font=("arial", 15), 
                                                        text="Delete Table",
                                                        command=lambda:self.__fn_delete_table(int(__delete_table_optionmenu.get())))
        __delete_table_button.grid(row=0, column=1)

    def __fn_create_table(self, multiplier: int) -> None:
            if multiplier > 0:
                if TableDb(self.__token).create_table(multiplier=multiplier):
                    messagebox.showinfo(title=None, message="Table created successfully")
                    self.__table_toplevel.destroy()
                    self._to_back()

    def __fn_delete_table(self, table_id: int) -> None:
        if TableDb(self.__token).delete_table(table_id):
            self._to_back()

    def _to_back(self) -> None:
        clear_frames(self._square_frame)
        self.__table_ui()
