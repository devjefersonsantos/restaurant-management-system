import tkinter
from tkinter import Toplevel
from tkinter import messagebox

import customtkinter

from utils.colors import *
from database.account_db import LoginDb
from database import TableDb
from database import WaiterDb
from utils import clear_frames

class TableUI:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self.__root = root
        self.__square_frame = square_frame
        self.__token = token

        clear_frames(self.__square_frame)
        self.__table_ui()
        
    def __topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                              text_color=WHITE_COLOR,
                                              font=("arial black", 25),
                                              text="Table")
        topbar_label.place(x=20, y=5)

        delete_table_button = customtkinter.CTkButton(master=topbar_frame,
                                                      width=197, height=32,
                                                      fg_color=RED_COLOR, 
                                                      hover_color=RED_HOVER_COLOR,
                                                      text_color=WHITE_COLOR,
                                                      corner_radius=4,
                                                      font=("arial", 15), 
                                                      text="Delete Table",
                                                      command=self.__delete_table_ui)
        delete_table_button.place(x=1249, y=9)

        create_table_button = customtkinter.CTkButton(master=topbar_frame,
                                                      width=197, height=32,
                                                      fg_color=GREEN_COLOR,
                                                      hover_color=GREEN_HOVER_COLOR,
                                                      text_color=WHITE_COLOR,
                                                      corner_radius=4,
                                                      font=("arial", 15), 
                                                      text="Add Table",
                                                      command=self.__create_table_ui)
        create_table_button.place(x=1455, y=9)

    def __table_ui(self) -> None:
        self.__topbar()
        
        # https://www.youtube.com/watch?v=Envp9yHb2Ho
        table_screen_frame = customtkinter.CTkFrame(master=self.__square_frame, 
                                                    width=1678, height=962,
                                                    corner_radius=0)
        table_screen_frame.place(x=0, y=50)

        table_screen_canvas = tkinter.Canvas(master=table_screen_frame, width=1678, height=858)
        table_screen_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

        table_scrollbar = tkinter.Scrollbar(master=table_screen_frame, 
                                            orient=tkinter.VERTICAL, 
                                            command=table_screen_canvas.yview)
        table_scrollbar.place(x=1660, y=0, height=858)

        table_screen_canvas.configure(yscrollcommand=table_scrollbar.set)

        ###########################################################################################
        def configure_scroll_region(event) -> None:
            table_screen_canvas.configure(scrollregion=table_screen_canvas.bbox("all"))
        ###########################################################################################
        table_screen_canvas.bind("<Configure>", configure_scroll_region)

        window_frame = tkinter.Frame(master=table_screen_canvas)
        table_screen_canvas.create_window((0,0), window=window_frame, anchor="nw")

        tables = TableDb(self.__token).read_tables()
        table_row = table_column = 0

        for table in tables:
            table_button = customtkinter.CTkButton(master=window_frame,
                                                   width=197, height=140,
                                                   fg_color=GREEN_COLOR,
                                                   hover_color=GREEN_HOVER_COLOR,
                                                   font=("arial bold", 20),
                                                   text=table[0],
                                                   command=lambda t=table[0]: self.__open_table_ui(table_id=t))
            table_button.grid(row=table_row, column=table_column, padx=5, pady=5) 

            table_column += 1
            if table_column == 8:
                table_row += 1
                table_column = 0

    def __create_table_ui(self) -> None:
        try:
            self.__table_toplevel.destroy()
        except:
            pass

        self.__table_toplevel = Toplevel(master=self.__root)
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("./images/global_images/icon.ico")) 
        self.__table_toplevel.title("Add Table")
        self.__table_toplevel.geometry("420x71+760+28")
        self.__table_toplevel.resizable(False, False)

        table_tabview = customtkinter.CTkTabview(master=self.__table_toplevel,
                                                 width=420, height=80,
                                                 bg_color=WHITE_COLOR,
                                                 corner_radius=0)
        table_tabview.place(x=0, y=-10)
        table_tabview.add("ID")
        table_tabview.add("Quantity")
        
        only_numbers = self.__root.register(lambda _ : _.isdigit())

        create_table_id_entry = customtkinter.CTkEntry(master=table_tabview.tab("ID"),
                                                       width=224, height=29,
                                                       border_color= WHITE_COLOR,
                                                       validate="key",
                                                       validatecommand=(only_numbers, "%P"),
                                                       border_width=1,
                                                       corner_radius=0,
                                                       font=("arial bold", 19))
        create_table_id_entry.grid(row=0, column=0, padx=5, pady=5)
        create_table_id_entry.focus()

        create_table_id_button = customtkinter.CTkButton(master=table_tabview.tab("ID"),
                                                         width=180, height=30,
                                                         text_color=WHITE_COLOR,
                                                         fg_color=GREEN_COLOR,
                                                         hover_color=GREEN_HOVER_COLOR,
                                                         corner_radius=4,
                                                         font=("arial", 15), 
                                                         text="Add Table",
                                                         command=lambda:self.__fn_create_table_id(create_table_id_entry.get()))
        create_table_id_button.grid(row=0, column=1)

        create_table_spinbox = tkinter.Spinbox(master=table_tabview.tab("Quantity"),
                                               width=17,
                                               validate="key",
                                               validatecommand=(only_numbers, "%P"),
                                               font=("arial bold", 16),
                                               from_=0, to=100)
        create_table_spinbox.grid(row=0, column=0, padx=5, pady=5)

        create_table_button = customtkinter.CTkButton(master=table_tabview.tab("Quantity"),
                                                      width=180, height=30,
                                                      text_color=WHITE_COLOR,
                                                      fg_color=GREEN_COLOR,
                                                      hover_color=GREEN_HOVER_COLOR,
                                                      corner_radius=4,
                                                      font=("arial", 15), 
                                                      text="Add Tables",
                                                      command=lambda:self.__fn_create_table(multiplier=int(create_table_spinbox.get())))
        create_table_button.grid(row=0, column=1)

    def __delete_table_ui(self) -> None:
        try:
            self.__table_toplevel.destroy()
        except:
            pass

        self.__table_toplevel = Toplevel(master=self.__root)
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("./images/global_images/icon.ico")) 
        self.__table_toplevel.title("Delete Table")
        self.__table_toplevel.geometry("426x54+760+35")
        self.__table_toplevel.resizable(False, False)

        delete_table_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
                                                              width=230, height=30,
                                                              text_color=GRAY_TEXT_COLOR,
                                                              fg_color=WHITE_COLOR,
                                                              button_color=OPTION_MENU_BUTTON_COLOR,
                                                              button_hover_color=OPTION_MENU_HOVER_COLOR,
                                                              corner_radius=4,
                                                              font=("arial", 17),
                                                              dropdown_font=("arial", 15),
                                                              values=[str(i[0]) for i in TableDb(self.__token).get_table_ids()])
        delete_table_optionmenu.grid(row=0, column=0, padx=5, pady=12)
        
        delete_table_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                      width=180, height=30,
                                                      text_color=WHITE_COLOR,
                                                      fg_color=RED_COLOR,
                                                      hover_color=RED_HOVER_COLOR,
                                                      corner_radius=4,
                                                      font=("arial", 15), 
                                                      text="Delete Table",
                                                      command=lambda:self.__fn_delete_table(int(delete_table_optionmenu.get())))
        delete_table_button.grid(row=0, column=1)

    def __fn_create_table_id(self, table_id: int) -> None:
        if TableDb(self.__token).create_table_id(table_id):
            self._to_back()

    def __fn_create_table(self, multiplier: int) -> None:
            if multiplier > 0:
                if TableDb(self.__token).create_table(multiplier=multiplier):
                    messagebox.showinfo(title=None, message="Table created successfully")
                    self.__table_toplevel.destroy()
                    self._to_back()

    def __fn_delete_table(self, table_id: int) -> None:
        if TableDb(self.__token).delete_table(table_id):
            self._to_back()

    def __open_table_ui(self, table_id: int) -> None:
        try:
            self.__table_toplevel.destroy()
        except:
            pass

        self.__table_toplevel = tkinter.Toplevel(master=self.__root)
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("./images/global_images/icon.ico"))
        self.__table_toplevel.title("Open Table")
        self.__table_toplevel.geometry("300x250+815+390")
        self.__table_toplevel.resizable(False, False)
        self.__table_toplevel.configure(background=WHITE_COLOR)

        number_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                              text_color=GRAY_TEXT_COLOR,
                                              font=("arial bold", 17),
                                              text="Number:")
        number_label.place(x=25, y=10)

        number_entry = customtkinter.CTkEntry(master=self.__table_toplevel,
                                              width=250, height=35,
                                              border_color=WHITE_COLOR,
                                              fg_color=LIGHT_GRAY_COLOR,
                                              corner_radius=3,
                                              border_width=1, 
                                              font=("arial", 17))
        number_entry.place(x=25, y=47)
        number_entry.insert(0, table_id)
        number_entry.configure(state="disabled")

        waiter_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                              text_color=GRAY_TEXT_COLOR,
                                              font=("arial bold", 17),
                                              text="Waiter:")
        waiter_label.place(x=25, y=95)

        waiter_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
                                                        width=250, height=35,
                                                        fg_color=FG_OPTION_MENU_COLOR,
                                                        text_color=GRAY_TEXT_COLOR,
                                                        button_color=GRAY_COLOR,
                                                        button_hover_color=GRAY_HOVER_COLOR,
                                                        corner_radius=4,
                                                        font=("arial", 17),
                                                        dropdown_font=("arial", 15),
                                                        values=self.__list_waiters() if self.__list_waiters() else ["No waiter registered"],
                                                        state=tkinter.NORMAL if self.__list_waiters() else tkinter.DISABLED)
        waiter_optionmenu.place(x=25, y=132)

        order_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                               width=250, height=32,
                                               text_color=WHITE_COLOR,
                                               fg_color=GREEN_COLOR,
                                               hover_color=GREEN_HOVER_COLOR,
                                               corner_radius=4,
                                               font=("arial", 15), 
                                               text="Order")
        order_button.place(x=25, y=195)

    def __list_waiters(self) -> list[str]:
        waiters = WaiterDb(self.__token).read_waiters()
        return [i[1] for i in waiters]

    def _to_back(self) -> None:
        clear_frames(self.__square_frame)
        self.__table_ui()
