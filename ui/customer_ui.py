import tkinter
import tkinter.messagebox
from tkinter import ttk

import customtkinter

from utils.colors import *
from database import CustomerDb
from database.account_db import LoginDb
from utils import clear_frames

class CustomerUi:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk,
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self._root = root
        self._square_frame = square_frame
        self.__token = token

        clear_frames(self._square_frame)
        self._customer_ui()

    def _topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        self._topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                                    text_color=WHITE_COLOR, 
                                                    font=("arial black", 25),
                                                    text="Customer")
        self._topbar_label.place(x=20, y=5)

        self._search_customers_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                              width=1227, height=35,
                                                              fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                              border_color=LIGHT_GRAY_COLOR, 
                                                              placeholder_text="Search by customer name",
                                                              font=("arial", 17),
                                                              border_width=1)
        self._search_customers_entry.place(x=174, y=8)

        self._search_customers_button = customtkinter.CTkButton(master=topbar_frame,
                                                               width=230, height=32,
                                                               corner_radius=4,
                                                               text_color=WHITE_COLOR,
                                                               font=("arial", 15), 
                                                               text="Search",
                                                               fg_color=LIGHT_BLUE_COLOR, 
                                                               hover_color=LIGHT_BLUE_HOVER_COLOR,
                                                               command=lambda:self.__fn_search_customer(self._search_customers_entry.get()))
        self._search_customers_button.place(x=1425, y=9)

    def _customer_ui(self) -> None:
        self._topbar()

        # https://stackoverflow.com/questions/75492266/changing-font-style-of-rows-in-treeview
        style = ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground=BLACK_GRAY_COLOR)
        style.configure("Treeview", font=("Arial", 13), foreground=BLACK_GRAY_COLOR, rowheight=28)

        self.__customer_treeview = ttk.Treeview(master=self._square_frame,
                                                height=28,
                                                style="style_treeview.Treeview",
                                                columns=("customer id", "name", "address", 
                                                            "cell phone", "email", "registration date"),
                                                show="headings")
        self.__customer_treeview.place(x=0, y=50)

        self.__customer_treeview.heading("#1", text="customer id", anchor="center")
        self.__customer_treeview.heading("#2", text="name", anchor="center")
        self.__customer_treeview.heading("#3", text="address", anchor="center")
        self.__customer_treeview.heading("#4", text="cell phone", anchor="center")
        self.__customer_treeview.heading("#5", text="email", anchor="center")
        self.__customer_treeview.heading("#6", text="registration date", anchor="center")

        self.__customer_treeview.column("#1", minwidth=100, width=225, anchor="center")
        self.__customer_treeview.column("#2", minwidth=150, width=300, anchor="center")
        self.__customer_treeview.column("#3", minwidth=150, width=300, anchor="center")
        self.__customer_treeview.column("#4", minwidth=150, width=300, anchor="center")
        self.__customer_treeview.column("#5", minwidth=150, width=300, anchor="center")
        self.__customer_treeview.column("#6", minwidth=262, width=237, anchor="center")

        divider_frame = tkinter.Frame(master=self._square_frame, 
                                      height=55, width=1678, 
                                      bg=LIGHT_GRAY_COLOR)
        divider_frame.place(x=0, y=860)

        __del_customer_button = customtkinter.CTkButton(master=self._square_frame,
                                                        width=230, height=32,
                                                        text_color=WHITE_COLOR,
                                                        fg_color=RED_COLOR,
                                                        hover_color=RED_HOVER_COLOR,
                                                        bg_color=LIGHT_GRAY_COLOR,
                                                        corner_radius=3,
                                                        font=("arial", 15),
                                                        text="Delete Customer",
                                                        command=self.__fn_delete_customer)
        __del_customer_button.place(x=905, y=868)

        update_customer_button = customtkinter.CTkButton(master=self._square_frame,
                                                         width=230, height=32,
                                                         text_color=WHITE_COLOR,
                                                         fg_color=ORANGE_COLOR,
                                                         hover_color=ORANGE_HOVER_COLOR,
                                                         bg_color=LIGHT_GRAY_COLOR,
                                                         corner_radius=3,
                                                         font=("arial", 15),
                                                         text="Update Customer",
                                                         command=self._update_customer_ui)
        update_customer_button.place(x=1165, y=868)

        create_customer_button = customtkinter.CTkButton(master=self._square_frame,
                                                         width=230, height=32,
                                                         text_color=WHITE_COLOR,
                                                         fg_color=GREEN_COLOR,
                                                         hover_color=GREEN_HOVER_COLOR,
                                                         bg_color=LIGHT_GRAY_COLOR, 
                                                         corner_radius=3,
                                                         font=("arial", 15),
                                                         text="Add Customer",
                                                         command=self.__create_customer_ui)
        create_customer_button.place(x=1425, y=868)

        treeview_scrollbar = tkinter.Scrollbar(self._square_frame, 
                                               orient=tkinter.VERTICAL, 
                                               command=self.__customer_treeview.yview)
        self.__customer_treeview.configure(yscroll=treeview_scrollbar.set)
        treeview_scrollbar.place(x=1660, y=50, height=808)

        self.__fn_read_customers()

    def __create_customer_ui(self) -> None:
        clear_frames(self._square_frame)
        self._topbar()
        
        self._topbar_label.configure(text="Add Customer")
        self._search_customers_entry.destroy()
        self._search_customers_button.destroy()

        add_customer_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                    width=1668, height=440,
                                                    fg_color=WHITE_COLOR,
                                                    corner_radius=10)
        add_customer_frame.place(x=5, y=55)

        name_label = customtkinter.CTkLabel(master=add_customer_frame,
                                            font=("arial bold", 17),
                                            text_color=GRAY_TEXT_COLOR,
                                            text="Name:")
        name_label.place(x=25, y=25)

        self.__name_entry = customtkinter.CTkEntry(master=add_customer_frame,
                                                   width=1618, height=35,
                                                   border_color=LIGHT_GRAY_COLOR, 
                                                   corner_radius=3, 
                                                   font=("arial", 17), 
                                                   border_width=1)
        self.__name_entry.place(x=25, y=62)

        address_label = customtkinter.CTkLabel(master=add_customer_frame,
                                               font=("arial bold", 17),
                                               text_color=GRAY_TEXT_COLOR,
                                               text="Address:")
        address_label.place(x=25, y=120)

        self.__address_entry = customtkinter.CTkEntry(master=add_customer_frame,
                                                      width=1618, height=35,
                                                      border_color=LIGHT_GRAY_COLOR, 
                                                      corner_radius=3, 
                                                      font=("arial", 17), 
                                                      border_width=1)
        self.__address_entry.place(x=25, y=160)

        cellphone_label = customtkinter.CTkLabel(master=add_customer_frame,
                                                 font=("arial bold", 17),
                                                 text_color=GRAY_TEXT_COLOR,
                                                 text="Cell Phone:")
        cellphone_label.place(x=25, y=215)

        self.__cellphone_entry = customtkinter.CTkEntry(master=add_customer_frame,
                                                        width=1618, height=35,
                                                        border_color=LIGHT_GRAY_COLOR, 
                                                        corner_radius=3, 
                                                        font=("arial", 17),
                                                        border_width=1)
        self.__cellphone_entry.place(x=25, y=255)

        email_label = customtkinter.CTkLabel(master=add_customer_frame,
                                             font=("arial bold", 17),
                                             text_color=GRAY_TEXT_COLOR,
                                             text="Email:")
        email_label.place(x=25, y=310)

        self.__email_entry = customtkinter.CTkEntry(master=add_customer_frame,
                                                    width=1618, height=35,                                                  
                                                    border_color=LIGHT_GRAY_COLOR, 
                                                    corner_radius=3,
                                                    font=("arial", 17),
                                                    border_width=1)
        self.__email_entry.place(x=25, y=350)

        divider_frame = tkinter.Frame(master=self._square_frame, 
                                      height=55, width=1678, 
                                      bg=LIGHT_GRAY_COLOR)
        divider_frame.place(x=0, y=860)

        __add_customer_button = customtkinter.CTkButton(master=self._square_frame,
                                                        width=230, height=32,
                                                        text_color=WHITE_COLOR,
                                                        fg_color=GREEN_COLOR,
                                                        hover_color=GREEN_HOVER_COLOR,
                                                        bg_color=LIGHT_GRAY_COLOR, 
                                                        corner_radius=3,
                                                        font=("arial", 15),
                                                        text="Add Customer",
                                                        command=self.__fn_create_customer)
        __add_customer_button.place(x=1165, y=868)
    
        self._cancel_button = customtkinter.CTkButton(master=self._square_frame,
                                                      width=230, height=32,
                                                      text_color=WHITE_COLOR,
                                                      bg_color= LIGHT_GRAY_COLOR, 
                                                      fg_color=GRAY_COLOR,
                                                      hover_color=GRAY_HOVER_COLOR,
                                                      corner_radius=3,
                                                      font=("arial", 15),
                                                      text="Cancel",
                                                      command=self._to_back)
        self._cancel_button.place(x=1425, y=868)

    def _update_customer_ui(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
        
        clear_frames(self._square_frame)
        self._topbar()
        
        self._topbar_label.configure(text="Update Customer")
        self._search_customers_entry.destroy()
        self._search_customers_button.destroy()

        update_customer_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                       width=1668, height=537,
                                                       corner_radius=10, 
                                                       fg_color=WHITE_COLOR)
        update_customer_frame.place(x=5, y=55)

        id_label = customtkinter.CTkLabel(master=update_customer_frame,
                                          font=("arial bold", 17),
                                          text_color=GRAY_TEXT_COLOR,
                                          text="ID:")
        id_label.place(x=25, y=25)

        self.__id_entry = customtkinter.CTkEntry(master=update_customer_frame,
                                                 width=1618, height=35,
                                                 border_color=LIGHT_GRAY_COLOR, 
                                                 corner_radius=3, 
                                                 font=("arial", 17), 
                                                 border_width=1)
        self.__id_entry.place(x=25, y=62)

        name_label = customtkinter.CTkLabel(master=update_customer_frame,
                                            font=("arial bold", 17),
                                            text_color=GRAY_TEXT_COLOR,
                                            text="Name:")
        name_label.place(x=25, y=120)

        self.__name_entry = customtkinter.CTkEntry(master=update_customer_frame,
                                                   width=1618, height=35,
                                                   border_color=LIGHT_GRAY_COLOR, 
                                                   corner_radius=3, 
                                                   font=("arial", 17), 
                                                   border_width=1)
        self.__name_entry.place(x=25, y=160)

        address_label = customtkinter.CTkLabel(master=update_customer_frame,
                                               font=("arial bold", 17),
                                               text_color=GRAY_TEXT_COLOR,
                                               text="Address:")
        address_label.place(x=25, y=215)

        self.__address_entry = customtkinter.CTkEntry(master=update_customer_frame,
                                                      width=1618, height=35,
                                                      border_color=LIGHT_GRAY_COLOR,
                                                      corner_radius=3, 
                                                      font=("arial", 17),
                                                      border_width=1)
        self.__address_entry.place(x=25, y=255)

        cellphone_label = customtkinter.CTkLabel(master=update_customer_frame,
                                                 font=("arial bold", 17),
                                                 text_color=GRAY_TEXT_COLOR,
                                                 text="Cell Phone:")
        cellphone_label.place(x=25, y=310)

        self.__cellphone_entry = customtkinter.CTkEntry(master=update_customer_frame,
                                                        width=1618, height=35,
                                                        border_color=LIGHT_GRAY_COLOR, 
                                                        corner_radius=3, 
                                                        font=("arial", 17), 
                                                        border_width=1)
        self.__cellphone_entry.place(x=25, y=350)

        email_label = customtkinter.CTkLabel(master=update_customer_frame,
                                             font=("arial bold", 17),
                                             text_color=GRAY_TEXT_COLOR,
                                             text="Email:")
        email_label.place(x=25, y=405)

        self.__email_entry = customtkinter.CTkEntry(master=update_customer_frame,
                                                    width=1618, height=35,
                                                    border_color=LIGHT_GRAY_COLOR, 
                                                    corner_radius=3, 
                                                    font=("arial", 17),
                                                    border_width=1)
        self.__email_entry.place(x=25, y=445)

        divider_frame = tkinter.Frame(master=self._square_frame, 
                                      height=55, width=1678, 
                                      bg=LIGHT_GRAY_COLOR)
        divider_frame.place(x=0, y=860)

        __update_customer_button = customtkinter.CTkButton(master=self._square_frame,
                                                           width=230, height=32,
                                                           text_color=WHITE_COLOR,
                                                           fg_color=GREEN_COLOR, 
                                                           hover_color=GREEN_HOVER_COLOR,
                                                           corner_radius=3,
                                                           font=("arial", 15), 
                                                           text="Save Changes",
                                                           command=self.__fn_update_customer)
        __update_customer_button.place(x=1165, y=868)

        cancel_button = customtkinter.CTkButton(master=self._square_frame,
                                                width=230, height=32,
                                                fg_color=GRAY_COLOR,
                                                hover_color=GRAY_HOVER_COLOR, 
                                                text_color=WHITE_COLOR,
                                                corner_radius=3,
                                                font=("arial", 15), 
                                                text="Cancel",
                                                command=self._to_back)
        cancel_button.place(x=1425, y=868)

        self.__customer_data()

    def __fn_create_customer(self) -> None:
        if CustomerDb(token=self.__token).create_customer(name=self.__name_entry.get(), 
                                                          address=self.__address_entry.get(), 
                                                          cellphone=self.__cellphone_entry.get(), 
                                                          email=self.__email_entry.get()):
            for i in [self.__name_entry, self.__address_entry, self.__cellphone_entry, self.__email_entry]:
                i.delete(0, "end")
            self._root.focus()
            self._cancel_button.configure(text="Back")

    def __fn_read_customers(self) -> None:
        self.__customer_treeview.delete(*self.__customer_treeview.get_children())

        __all_customers = [(i[0], i[1], i[2], i[3], i[4], i[5].replace(microsecond=0)) 
                           for i in CustomerDb(token=self.__token).read_customers()]

        self.__customer_treeview.tag_configure("even_row", background=EVEN_ROW_COLOR)
        self.__customer_treeview.tag_configure("odd_row", background=ODD_ROW_COLOR)
        
        tag = "even_row"
        for i in __all_customers:
            tag = "even_row" if tag == "odd_row" else "odd_row"
            self.__customer_treeview.insert("", "end", values=i, tags=tag)

    def __fn_update_customer(self) -> None:
        if CustomerDb(token=self.__token).update_customer(customer_id=self.__id_entry.get(),
                                                          name=self.__name_entry.get(),
                                                          address=self.__address_entry.get(),
                                                          cellphone=self.__cellphone_entry.get(),
                                                          email=self.__email_entry.get()):
            self._to_back()

    def __fn_delete_customer(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
          
        message = f"Are you sure you want to delete\nthis customer? {self.__data[1]}."
        if tkinter.messagebox.askyesno(title="Delete Customer", 
                                       message=message, 
                                       icon=tkinter.messagebox.WARNING) == True:
            CustomerDb(self.__token).delete_customer(customer_id=self.__data[0])
            self.__fn_read_customers()

    def __fn_search_customer(self, typed: str) -> None:
        self.__customer_treeview.delete(*self.__customer_treeview.get_children())

        __customer = [(i[0], i[1], i[2], i[3], i[4], i[5].replace(microsecond=0))
                      for i in CustomerDb(self.__token).search_customer(typed=typed)]

        tag = "even_row"
        for i in __customer:
            tag = "even_row" if tag == "odd_row" else "odd_row"
            self.__customer_treeview.insert("", "end", values=i, tags=tag)

    def __customer_data(self) -> None:
        list_entries = [self.__id_entry, 
                        self.__name_entry, 
                        self.__address_entry, 
                        self.__cellphone_entry, 
                        self.__email_entry]
        for k, v in enumerate(list_entries):
            v.insert(0, self.__data[k])

        self.__id_entry.configure(state="disabled", fg_color=LIGHT_GRAY_COLOR, border_color=WHITE_COLOR)

    def __selected_row(self) -> tuple:
        try:
            selected_customer = self.__customer_treeview.item(self.__customer_treeview.selection()[0], "values")
            return selected_customer
        except IndexError:
            tkinter.messagebox.showerror(title=None, message="Please select a customer")

    def _to_back(self) -> None:
        clear_frames(self._square_frame)
        self._customer_ui()
