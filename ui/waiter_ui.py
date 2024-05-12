import tkinter
from tkinter import ttk

import customtkinter

from .colors import *
from database import LoginDb
from database import WaiterDb
from utils import clear_frames

class WaiterUi:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self._root = root
        self._square_frame = square_frame
        self.__token = token

        clear_frames(self._square_frame)
        self._waiter_ui()

    def _topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        self._topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                                    text_color=WHITE_COLOR, 
                                                    font=("arial black", 25),
                                                    text="Waiter")
        self._topbar_label.place(x=20, y=5)

        self._search_waiters_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                            width=1227, height=35,
                                                            fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                            border_color=LIGHT_GRAY_COLOR, 
                                                            placeholder_text="Search by name",
                                                            font=("arial", 17), 
                                                            border_width=1)
        self._search_waiters_entry.place(x=174, y=8)

        self._search_waiters_button = customtkinter.CTkButton(master=topbar_frame,
                                                              width=230, height=32,
                                                              text_color=WHITE_COLOR,
                                                              fg_color=LIGHT_BLUE_COLOR,
                                                              hover_color=LIGHT_BLUE_HOVER_COLOR,
                                                              corner_radius=4,
                                                              font=("arial", 15), 
                                                              text="Search",
                                                              command=lambda:self.__fn_search_waiter(self._search_waiters_entry.get()))
        self._search_waiters_button.place(x=1425, y=9)

    def _waiter_ui(self) -> None:
        clear_frames(self._square_frame)

        self._topbar()

        self._create_waiter_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                           width=350, height=240,
                                                           fg_color=WHITE_COLOR,
                                                           corner_radius=10)
        self._create_waiter_frame.place(x=10, y=58)

        waiter_name_label = customtkinter.CTkLabel(master=self._create_waiter_frame, 
                                                   text_color=GRAY_TEXT_COLOR, 
                                                   font=("arial", 17), 
                                                   text="Name:")
        waiter_name_label.place(x=10, y=10)

        self.__waiter_name_entry = customtkinter.CTkEntry(master=self._create_waiter_frame,
                                                          width=330, height=35,
                                                          border_color=LIGHT_GRAY_COLOR, 
                                                          corner_radius=3, 
                                                          font=("arial", 17), 
                                                          border_width=1)
        self.__waiter_name_entry.place(x=10, y=45)

        waiter_cellphone_label = customtkinter.CTkLabel(master=self._create_waiter_frame, 
                                                        text_color=GRAY_TEXT_COLOR,
                                                        font=("arial", 17), 
                                                        text="Cell Phone:")
        waiter_cellphone_label.place(x=10, y=90)

        self.__waiter_cellphone_entry = customtkinter.CTkEntry(master=self._create_waiter_frame,
                                                               width=330, height=35,
                                                               border_color=LIGHT_GRAY_COLOR, 
                                                               corner_radius=3, 
                                                               font=("arial", 17),
                                                               border_width=1)
        self.__waiter_cellphone_entry.place(x=10, y=125)

        self.__create_waiter_button = customtkinter.CTkButton(master=self._create_waiter_frame,
                                                              width=330, height=35,
                                                              fg_color=GREEN_COLOR, 
                                                              hover_color=GREEN_HOVER_COLOR,
                                                              text_color=WHITE_COLOR,
                                                              corner_radius=3,
                                                              font=("arial", 15),
                                                              text="Add Waiter",
                                                              command=self.__fn_create_waiter)
        self.__create_waiter_button.place(x=10, y=185)

        self._update_waiter_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                           width=350, height=100,
                                                           fg_color=WHITE_COLOR,
                                                           corner_radius=10)
        self._update_waiter_frame.place(x=10, y=680)

        update_waiter_label = customtkinter.CTkLabel(master=self._update_waiter_frame, 
                                                     text_color=GRAY_TEXT_COLOR, 
                                                     font=("arial", 17), 
                                                     text="Update selected waiter:")
        update_waiter_label.place(x=10, y=10)

        update_waiter_button = customtkinter.CTkButton(master=self._update_waiter_frame,
                                                       width=330, height=35,
                                                       text_color=WHITE_COLOR,
                                                       fg_color=ORANGE_COLOR, 
                                                       hover_color=ORANGE_HOVER_COLOR,
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text="Update Waiter",
                                                       command=self._ui_update_waiter)
        update_waiter_button.place(x=10, y=45)

        self._delete_waiter_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                           width=350, height=100,
                                                           fg_color=WHITE_COLOR,
                                                           corner_radius=10)
        self._delete_waiter_frame.place(x=10, y=795)

        delete_waiter_label = customtkinter.CTkLabel(master=self._delete_waiter_frame, 
                                                     text_color=GRAY_TEXT_COLOR, 
                                                     font=("arial", 17), 
                                                     text="Delete selected waiter:")
        delete_waiter_label.place(x=10, y=10)

        __delete_waiter_button = customtkinter.CTkButton(master=self._delete_waiter_frame,
                                                         width=330, height=35,
                                                         text_color=WHITE_COLOR,
                                                         fg_color=RED_COLOR,
                                                         hover_color=RED_HOVER_COLOR,
                                                         corner_radius=3,
                                                         font=("arial", 15),
                                                         text="Delete Waiter",
                                                         command=self.__fn_delete_waiter)
        __delete_waiter_button.place(x=10, y=45)

        # https://stackoverflow.com/questions/75492266/changing-font-style-of-rows-in-treeview
        style = ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground=BLACK_GRAY_COLOR)
        style.configure("Treeview", font=("Arial", 13), foreground=BLACK_GRAY_COLOR, rowheight=28)

        self.__waiter_treeview = ttk.Treeview(master=self._square_frame,
                                              height=29,
                                              style="style_treeview.Treeview",
                                              columns=("waiter id", "name", "cell phone", "registration date"),
                                              show="headings")
        self.__waiter_treeview.place(x=370, y=58)

        self.__waiter_treeview.heading("#1", text="waiter id", anchor="center")
        self.__waiter_treeview.heading("#2", text="name", anchor="center")
        self.__waiter_treeview.heading("#3", text="cell phone", anchor="center")
        self.__waiter_treeview.heading("#4", text="registration date", anchor="center")

        self.__waiter_treeview.column("#1", minwidth=100, width=225, anchor="center")
        self.__waiter_treeview.column("#2", minwidth=200, width=350, anchor="center")
        self.__waiter_treeview.column("#3", minwidth=250, width=375, anchor="center")
        self.__waiter_treeview.column("#4", minwidth=300, width=350, anchor="center")

        _treeview_scrollbar = tkinter.Scrollbar(self._square_frame, orient=tkinter.VERTICAL, command=self.__waiter_treeview.yview)
        self.__waiter_treeview.configure(yscroll=_treeview_scrollbar.set)
        _treeview_scrollbar.place(x=1660, y=58, height=837)

        self.__fn_read_waiters()

    def _ui_update_waiter(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
        
        self._topbar_label.configure(text="Update Waiter")
        self._search_waiters_entry.destroy()
        self._search_waiters_button.destroy()
        
        self._update_waiter_frame.destroy()
        self._delete_waiter_frame.destroy()

        self.__waiter_name_entry.delete(0, "end")
        self.__waiter_cellphone_entry.delete(0, "end")

        self._create_waiter_frame.configure(height=300)
        self.__create_waiter_button.configure(text="Save Changes", 
                                              command=self.__fn_update_waiter)

        self._cancel_button = customtkinter.CTkButton(master=self._create_waiter_frame,
                                                      width=330, height=35,
                                                      text_color=WHITE_COLOR,
                                                      fg_color=GRAY_COLOR,
                                                      hover_color=GRAY_HOVER_COLOR,
                                                      corner_radius=3,
                                                      font=("arial", 15),
                                                      text="Cancel",
                                                      command=self._waiter_ui)
        self._cancel_button.place(x=10, y=240)

        self.__waiter_name_entry.insert(0, self.__data[1])
        self.__waiter_cellphone_entry.insert(0, self.__data[2])

    def __fn_create_waiter(self) -> None:
        if WaiterDb(token=self.__token).create_waiter(name=self.__waiter_name_entry.get(),
                                                      cellphone=self.__waiter_cellphone_entry.get()):
            self._clear_entries()
            self.__fn_read_waiters()

    def __fn_read_waiters(self) -> None:
        self.__waiter_treeview.delete(*self.__waiter_treeview.get_children())

        __all_waiters = [(i[0], i[1], i[2], i[3].replace(microsecond=0))
                         for i in WaiterDb(token=self.__token).read_waiters()]

        self.__waiter_treeview.tag_configure("even_row", background=EVEN_ROW_COLOR)
        self.__waiter_treeview.tag_configure("odd_row", background=ODD_ROW_COLOR)
        
        tag = "even_row"
        for i in __all_waiters:
            tag = "even_row" if tag == "odd_row" else "odd_row"
            self.__waiter_treeview.insert("", "end", values=i, tags=tag)
    
    def __fn_update_waiter(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
        
        updated_waiter = WaiterDb(self.__token).update_waiter(new_name=self.__waiter_name_entry.get(),
                                                              new_cellphone=self.__waiter_cellphone_entry.get(),
                                                              waiter_id=self.__data[0])
        
        if updated_waiter:
            self._waiter_ui()

    def __fn_delete_waiter(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
        
        message = f"Are you sure you want to delete\nthis waiter? {self.__data[1]}."
        if tkinter.messagebox.askyesno(title="Delete Waiter", 
                                       message=message, 
                                       icon=tkinter.messagebox.WARNING) == True:
            WaiterDb(self.__token).delete_waiter(waiter_id=self.__data[0])
            self.__fn_read_waiters()
    
    def __fn_search_waiter(self, typed: str) -> None:
        self.__waiter_treeview.delete(*self.__waiter_treeview.get_children())

        __waiter = WaiterDb(self.__token).search_waiter(typed=typed)

        tag = "even_row"
        for i in __waiter:
            tag = "even_row" if tag == "odd_row" else "odd_row"
            self.__waiter_treeview.insert("", "end", values=i, tags=tag)

    def __selected_row(self) -> tuple:
        try:
            selected_waiter = self.__waiter_treeview.item(self.__waiter_treeview.selection()[0], "values")
            return selected_waiter
        except IndexError:
            tkinter.messagebox.showerror(title=None, message="Please select a waiter")

    def _clear_entries(self) -> None:
        self.__waiter_name_entry.delete(0, "end")
        self.__waiter_cellphone_entry.delete(0, "end")
        self._root.focus()
