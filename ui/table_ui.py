import os
import tkinter
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

from PIL import Image
import customtkinter

from utils.colors import *
from database.account_db import LoginDb
from database import AccountDb
from database import CustomerDb
from database import MealDb
from database import TableDb
from database import WaiterDb
from database import OrderDb
from logs import log_error
from utils import clear_frames
from utils import empty_entries
from utils import find_tuple_by_name

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
        self.__images_ui()
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

        greenstatus_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                   width=30, height=30,
                                                   bg_color=DEFAULT_BACKGROUND_COLOR,
                                                   fg_color=GREEN_COLOR,
                                                   corner_radius=100)
        greenstatus_frame.place(x=245, y=9)
        greenstatus_label = customtkinter.CTkLabel(master=self.__square_frame,
                                                   text_color=GRAY_TEXT_COLOR,
                                                   bg_color=DEFAULT_BACKGROUND_COLOR,
                                                   text="Unoccupied",
                                                   font=("arial", 17))
        greenstatus_label.place(x=285, y=9)

        redstatus_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                 width=30, height=30,
                                                 bg_color=DEFAULT_BACKGROUND_COLOR,
                                                 fg_color=RED_COLOR,
                                                 corner_radius=100)
        redstatus_frame.place(x=445, y=9)
        redstatus_label = customtkinter.CTkLabel(master=self.__square_frame,
                                                 text_color=GRAY_TEXT_COLOR,
                                                 bg_color=DEFAULT_BACKGROUND_COLOR,
                                                 text="Occupied",
                                                 font=("arial", 17))
        redstatus_label.place(x=485, y=9)

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

        self.__root.bind("<Return>", lambda _ : create_table_button.invoke())

    def __images_ui(self) -> None:
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        mealpil_image = Image.open("./images/tables_images/meal.png")
        self.__meal_image = customtkinter.CTkImage(dark_image=mealpil_image,
                                                   light_image=mealpil_image,
                                                   size=(47,47))
        
        pricepil_image = Image.open("./images/tables_images/price.png")
        self.__price_image = customtkinter.CTkImage(dark_image=pricepil_image,
                                                    light_image=pricepil_image,
                                                    size=(47,47))
        
        paymentpil_image = Image.open("./images/tables_images/payment.png")
        self.__payment_image = customtkinter.CTkImage(dark_image=paymentpil_image,
                                                      light_image=paymentpil_image,
                                                      size=(47,47))
        
        changepil_image = Image.open("images/tables_images/change.png")
        self.__change_image = customtkinter.CTkImage(dark_image=changepil_image,
                                                     light_image=changepil_image,
                                                     size=(47,47))
        
        userpil_image = Image.open("./images/login_images/user.png")
        self.__user_image = customtkinter.CTkImage(dark_image=userpil_image,
                                                   light_image=userpil_image,
                                                   size=(32,32))

        passwordpil_image = Image.open("./images/login_images/password.png")
        self.__password_image = customtkinter.CTkImage(dark_image=passwordpil_image,
                                                       light_image=passwordpil_image,
                                                       size=(32,32))
        
        # https://pixabay.com/vectors/eye-see-viewing-icon-1103592/
        showpasswordpil_image = Image.open("./images/login_images/showpassword.png")
        self.__showpassword_image = customtkinter.CTkImage(dark_image=showpasswordpil_image,
                                                           light_image=showpasswordpil_image,
                                                           size=(25,15))

        hidepasswordpil_image = Image.open("./images/login_images/hidepassword.png")
        self.__hidepassword_image = customtkinter.CTkImage(dark_image=hidepasswordpil_image,
                                                           light_image=hidepasswordpil_image,
                                                           size=(25,15))
        
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

        tables = TableDb(self.__token).get_table_order_values()
        table_row = table_column = 0

        for table in tables:
            table_button = customtkinter.CTkButton(master=window_frame,
                                                   width=197, height=140,
                                                   fg_color=RED_COLOR if table[1] else GREEN_COLOR,
                                                   hover_color=RED_HOVER_COLOR if table[1] else GREEN_HOVER_COLOR,
                                                   font=("arial bold", 20),
                                                   text=f"{table[0]}\n\n{table[2]}" if table[1] else table[0],
                                                   command=lambda t=table[0]: self.__open_table_ui(table_id=t))
            table_button.grid(row=table_row, column=table_column, padx=5, pady=5)
            
            if table_button.cget("fg_color") == RED_COLOR:
                table_button.configure(command=lambda _= table[0]: self.__table_with_orders_ui(table_id=_))

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
                                                 corner_radius=0,
                                                 command=lambda:__tabview_bind(table_tabview.get()))
        
        ###########################################################################################
        def __tabview_bind(tab: str) -> None:
            if tab == "ID":
                self.__table_toplevel.bind("<Return>", lambda _ : create_table_id_button.invoke())
            elif tab == "Quantity":
                self.__table_toplevel.bind("<Return>", lambda _ : create_table_button.invoke())
        ###########################################################################################
        self.__table_toplevel.bind("<Return>", lambda _ : create_table_id_button.invoke())

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
        self.__table_toplevel.focus()

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

        waiter_names = WaiterDb(self.__token).get_waiter_names()
        waiter_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
            width=250, height=35,
            fg_color=FG_OPTION_MENU_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=GRAY_COLOR,
            button_hover_color=GRAY_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=waiter_names if waiter_names else ["No waiter registered"],
            state=tkinter.NORMAL if waiter_names else tkinter.DISABLED
        )
        waiter_optionmenu.place(x=25, y=132)

        order_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                               width=250, height=32,
                                               text_color=WHITE_COLOR,
                                               fg_color=GREEN_COLOR,
                                               hover_color=GREEN_HOVER_COLOR,
                                               corner_radius=4,
                                               font=("arial", 15), 
                                               text="Order",
                                               command=lambda:self.__initial_order_ui(table_id=table_id, waiter=waiter_optionmenu.get()))
        order_button.place(x=25, y=195)

    def __initial_order_ui(self, table_id: int, waiter: str) -> None:
        self.__table_toplevel.destroy()

        self.__table_toplevel = tkinter.Toplevel(master=self.__root)
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("./images/global_images/icon.ico")) 
        self.__table_toplevel.title("Initial Order")
        self.__table_toplevel.geometry("669x669+650+200")
        self.__table_toplevel.resizable(False, False)
        self.__table_toplevel.focus()

        table_id_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                text_color=BLACK_GRAY_COLOR,
                                                font=("arial bold", 17),
                                                text="Table:")
        table_id_label.place(x=25, y=10)

        table_id_entry = customtkinter.CTkEntry(master=self.__table_toplevel,
                                                width=150, height=35,
                                                border_color=WHITE_COLOR,
                                                fg_color=LIGHT_GRAY_COLOR,
                                                corner_radius=3,
                                                border_width=1, 
                                                font=("arial", 17))
        table_id_entry.place(x=25, y=47)
        table_id_entry.insert(0, table_id)
        table_id_entry.configure(state="disabled")

        waiter_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                              text_color=BLACK_GRAY_COLOR,
                                              font=("arial bold", 17),
                                              text="Waiter:")
        waiter_label.place(x=194, y=10)

        waiter_entry = customtkinter.CTkEntry(master=self.__table_toplevel,
                                              width=450, height=35,
                                              fg_color=LIGHT_GRAY_COLOR,
                                              border_color=WHITE_COLOR,
                                              text_color=WHITE_COLOR if waiter == "No waiter registered" else None,
                                              corner_radius=3,
                                              border_width=1, 
                                              font=("arial", 17))
        waiter_entry.place(x=194, y=47)
        waiter_entry.insert(0, "Unregistered" if waiter == "No waiter registered" else waiter)
        waiter_entry.configure(state="disabled")

        customer_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial bold", 17),
                                                text="Customer:")
        customer_label.place(x=25, y=95)

        customer_names : list[str] = CustomerDb(self.__token).get_customer_names()
        customer_names.insert(0, "Unregistered")
        customer_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
            width=619, height=35,
            fg_color=WHITE_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=OPTION_MENU_BUTTON_COLOR,
            button_hover_color=OPTION_MENU_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=customer_names if customer_names else ["No customer registered"],
            state=tkinter.NORMAL if customer_names else tkinter.DISABLED
        )
        customer_optionmenu.place(x=25, y=132)

        meals_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                             font=("arial bold", 17),
                                             text_color=GRAY_TEXT_COLOR,
                                             text="Meals:")
        meals_label.place(x=25, y=180)

        meals_info : list[tuple] = MealDb(self.__token).read_meals()
        self.__meal_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
            width=300, height=35,
            fg_color=WHITE_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=OPTION_MENU_BUTTON_COLOR,
            button_hover_color=OPTION_MENU_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=[i[1] for i in meals_info] if meals_info else ["No meal registered"],
            state=tkinter.NORMAL if meals_info else tkinter.DISABLED
        )
        self.__meal_optionmenu.place(x=25, y=214)

        self.__total_spinbox = tkinter.Spinbox(master=self.__table_toplevel,
                                             width=3,
                                             font=("arial", 19),
                                             from_=1, to=100)
        self.__total_spinbox.place(x=336, y=215)

        self.__add_button = customtkinter.CTkButton(master=self.__table_toplevel,
            width=100, height=35,
            text_color=WHITE_COLOR,
            fg_color=GREEN_COLOR,
            hover_color=GREEN_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 15), 
            text="Add to list",
            command=lambda:self.__add_to_list(meals_info=meals_info, 
                                              meal=self.__meal_optionmenu.get(), 
                                              total=self.__total_spinbox.get()))
        self.__add_button.place(x=410, y=214)

        self.__remove_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                       width=100, height=35,
                                                       text_color=WHITE_COLOR,
                                                       fg_color=RED_COLOR, 
                                                       hover_color=RED_HOVER_COLOR,
                                                       corner_radius=4,
                                                       font=("arial", 15), 
                                                       text="Remove selected",
                                                       command=lambda:self.__remove_from_list(parent=self.__table_toplevel))
        self.__remove_button.place(x=520, y=214)

        # https://stackoverflow.com/questions/75492266/changing-font-style-of-rows-in-treeview
        style = ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground=BLACK_GRAY_COLOR)
        style.configure("Treeview", font=("Arial", 13), foreground=BLACK_GRAY_COLOR, rowheight=28)

        self.__meal_treeview = ttk.Treeview(master=self.__table_toplevel,
                                            height=8,
                                            style="style_treeview.Treeview",
                                            columns=("ID", "meal name", "sale price", "category"),
                                            show="headings")
        self.__meal_treeview.place(x=25, y=260)

        self.__meal_treeview.heading("#1", text="ID", anchor="center")
        self.__meal_treeview.heading("#2", text="meal name", anchor="center")
        self.__meal_treeview.heading("#3", text="sale price", anchor="center")
        self.__meal_treeview.heading("#4", text="category", anchor="center")

        self.__meal_treeview.column("#1", minwidth=50, width=70, anchor="center")
        self.__meal_treeview.column("#2", minwidth=100, width=260, anchor="center")
        self.__meal_treeview.column("#3", minwidth=100, width=130, anchor="w")
        self.__meal_treeview.column("#4", minwidth=100, width=150, anchor="w")

        self.__treeview_scrollbar = tkinter.Scrollbar(master=self.__table_toplevel, 
                                                      orient=tkinter.VERTICAL, 
                                                      command=self.__meal_treeview.yview)
        self.__meal_treeview.configure(yscroll=self.__treeview_scrollbar.set)
        self.__treeview_scrollbar.place(x=627, y=260, height=248)

        self.__treeview_tag = "even_row"
        self.__meal_treeview.tag_configure("even_row", background=EVEN_ROW_COLOR)
        self.__meal_treeview.tag_configure("odd_row", background=ODD_ROW_COLOR)

        square_status_frame = customtkinter.CTkFrame(master=self.__table_toplevel,
                                                     width=619, height=90,
                                                     fg_color=WHITE_COLOR)
        square_status_frame.place(x=25, y=520)

        meal_image_label = customtkinter.CTkLabel(master=square_status_frame,
                                                  text="", 
                                                  image=self.__meal_image)
        meal_image_label.place(x=25, y=22)
        total_meal_label = customtkinter.CTkLabel(master=square_status_frame, 
                                                  text_color=BLACK_GRAY_COLOR,
                                                  font=("arial", 17), 
                                                  text="Total meals:")
        total_meal_label.place(x=95, y=10)

        self.__total_meal_stringvar = customtkinter.StringVar()
        self.__total_meal_stringvar.set(0)
        total_meal_stringvar_label = customtkinter.CTkLabel(master=square_status_frame, 
                                                            text_color=GRAY_TEXT_COLOR, 
                                                            font=("arial", 19), 
                                                            textvariable=self.__total_meal_stringvar)
        total_meal_stringvar_label.place(x=140, y=36)

        divider_frame = tkinter.Frame(master=square_status_frame, 
                                      height=70, width=1)
        divider_frame.place(x=309, y=10)


        sale_price_image_label = customtkinter.CTkLabel(master=square_status_frame,
                                                        text="", 
                                                        image=self.__price_image)
        sale_price_image_label.place(x=334, y=22)
        sale_price_label = customtkinter.CTkLabel(master=square_status_frame, 
                                                  font=("arial", 17), 
                                                  text_color=BLACK_GRAY_COLOR, 
                                                  text="Total price:")
        sale_price_label.place(x=404, y=10)

        self.__sale_price_stringvar = customtkinter.StringVar()
        self.__sale_price_stringvar.set(0.00)
        sale_price_stringvar_label = customtkinter.CTkLabel(master=square_status_frame, 
                                                            font=("arial", 19), 
                                                            text_color=GRAY_TEXT_COLOR, 
                                                            textvariable=self.__sale_price_stringvar)
        sale_price_stringvar_label.place(x=449, y=36)

        start_order_button = customtkinter.CTkButton(master=self.__table_toplevel,
            width=230, height=32,
            text_color=WHITE_COLOR,
            fg_color=GREEN_COLOR, 
            hover_color=GREEN_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 15), 
            text="Start Order",
            command=lambda:self.__fn_create_initial_order(table_id=table_id,
                                                          waiter_name=waiter,
                                                          customer_name=customer_optionmenu.get(),
                                                          treeview_children=self.__meal_treeview.get_children()))
        start_order_button.place(x=412, y=623)

        back_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                              width=230, height=32,
                                              text_color=WHITE_COLOR,
                                              fg_color=GRAY_COLOR,
                                              hover_color=GRAY_HOVER_COLOR,
                                              corner_radius=3,
                                              font=("arial", 15),
                                              text="Back",
                                              command=lambda:self.__open_table_ui(table_id))
        back_button.place(x=170, y=623)

    def __table_with_orders_ui(self, table_id: int) -> None:
        try:
            self.__table_toplevel.destroy()
        except:
            pass

        # Example: ('Jeferson Santos', 'Customer Name', 4)
        waiter, customer, order_id = TableDb(self.__token).table_information(table_id=table_id)

        self.__table_toplevel = Toplevel(master=self.__root)
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__table_toplevel.title("Orders")
        self.__table_toplevel.after(200, lambda: self.__table_toplevel.iconbitmap("./images/global_images/icon.ico"))
        self.__table_toplevel.geometry("669x895+625+50")
        self.__table_toplevel.resizable(False, False)
        self.__table_toplevel.focus()

        table_id_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                font=("arial bold", 17),
                                                text_color=BLACK_GRAY_COLOR,
                                                text="Table:")
        table_id_label.place(x=25, y=10)

        table_id_entry = customtkinter.CTkEntry(master=self.__table_toplevel,
                                                width=150, height=35,
                                                border_color=WHITE_COLOR,
                                                fg_color=LIGHT_GRAY_COLOR,
                                                corner_radius=3,
                                                border_width=1, 
                                                font=("arial", 17))
        table_id_entry.place(x=25, y=47)
        table_id_entry.insert(0, table_id)
        table_id_entry.configure(state="disabled")

        waiter_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                              text_color=BLACK_GRAY_COLOR,
                                              font=("arial bold", 17),
                                              text="Waiter:")
        waiter_label.place(x=194, y=10)

        waiter_entry = customtkinter.CTkEntry(master=self.__table_toplevel,
                                              width=450, height=35,
                                              border_color=WHITE_COLOR,
                                              fg_color=LIGHT_GRAY_COLOR, 
                                              corner_radius=3,
                                              border_width=1, 
                                              font=("arial", 17))
        waiter_entry.place(x=194, y=47)
        waiter_entry.insert(0, waiter if waiter != None else "Unregistered")
        waiter_entry.configure(state="disabled")

        customer_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                text_color=BLACK_GRAY_COLOR,
                                                font=("arial bold", 17),
                                                text="Customer:")
        customer_label.place(x=25, y=95)

        customer_entry = customtkinter.CTkEntry(master=self.__table_toplevel,
                                                width=620, height=35,
                                                fg_color=LIGHT_GRAY_COLOR,
                                                border_color=WHITE_COLOR,
                                                corner_radius=3,
                                                border_width=1, 
                                                font=("arial", 17))
        customer_entry.place(x=25, y=132)
        customer_entry.insert(0, customer if customer != None else "Unregistered")
        customer_entry.configure(state="disabled")

        self.__meals_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                    text_color=BLACK_GRAY_COLOR,
                                                    font=("arial bold", 17),
                                                    text="Meals:")
        self.__meals_label.place(x=25, y=180)

        meals_info : list[tuple] = MealDb(self.__token).read_meals()
        self.__meal_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
            width=300, height=35,
            fg_color=WHITE_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=OPTION_MENU_BUTTON_COLOR,
            button_hover_color=OPTION_MENU_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=[i[1] for i in meals_info] if meals_info else ["No meal registered"],
            state=tkinter.NORMAL if meals_info else tkinter.DISABLED
        )
        self.__meal_optionmenu.place(x=25, y=214)

        self.__total_spinbox = tkinter.Spinbox(master=self.__table_toplevel,
                                               width=3,
                                               font=("arial", 19),
                                               from_=1, to=100)
        self.__total_spinbox.place(x=336, y=215)

        # https://stackoverflow.com/questions/75492266/changing-font-style-of-rows-in-treeview
        style = ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground=BLACK_GRAY_COLOR)
        style.configure("Treeview", font=("Arial", 13), foreground=BLACK_GRAY_COLOR, rowheight=28)

        self.__meal_treeview = ttk.Treeview(master=self.__table_toplevel,
                                            height=16,
                                            style="style_treeview.Treeview",
                                            columns=("ID", "meal name", "sale price", "category"),
                                            show="headings")
        self.__meal_treeview.place(x=25, y=260)

        self.__meal_treeview.heading("#1", text="ID", anchor="center")
        self.__meal_treeview.heading("#2", text="meal name", anchor="center")
        self.__meal_treeview.heading("#3", text="sale price", anchor="center")
        self.__meal_treeview.heading("#4", text="category", anchor="center")

        self.__meal_treeview.column("#1", minwidth=50, width=70, anchor="center")
        self.__meal_treeview.column("#2", minwidth=100, width=260, anchor="center")
        self.__meal_treeview.column("#3", minwidth=100, width=130, anchor="w")
        self.__meal_treeview.column("#4", minwidth=100, width=150, anchor="w")

        self.__treeview_scrollbar = tkinter.Scrollbar(master=self.__table_toplevel, 
                                                      orient=tkinter.VERTICAL, 
                                                      command=self.__meal_treeview.yview)
        self.__meal_treeview.configure(yscroll=self.__treeview_scrollbar.set)
        self.__treeview_scrollbar.place(x=627, y=260, height=472)

        self.__square_status_frame = customtkinter.CTkFrame(master=self.__table_toplevel,
                                                            width=619, height=90,
                                                            fg_color=WHITE_COLOR)
        self.__square_status_frame.place(x=25, y=742)

        meal_image_label = customtkinter.CTkLabel(master=self.__square_status_frame,
                                                  text="", 
                                                  image=self.__meal_image)
        meal_image_label.place(x=25, y=22)
        total_meal_label = customtkinter.CTkLabel(master=self.__square_status_frame, 
                                                  text_color=BLACK_GRAY_COLOR,
                                                  font=("arial", 17), 
                                                  text="Total meals:")
        total_meal_label.place(x=95, y=10)

        self.__total_meal_stringvar = customtkinter.StringVar()
        self.__total_meal_stringvar.set(0)
        total_meal_stringvar_label = customtkinter.CTkLabel(master=self.__square_status_frame,
                                                            text_color=GRAY_TEXT_COLOR, 
                                                            font=("arial", 19), 
                                                            textvariable=self.__total_meal_stringvar)
        total_meal_stringvar_label.place(x=140, y=36)

        divider_frame = tkinter.Frame(master=self.__square_status_frame, height=70, width=1)
        divider_frame.place(x=309, y=10)


        sale_price_image_label = customtkinter.CTkLabel(master=self.__square_status_frame,
                                                        text="", 
                                                        image=self.__price_image)
        sale_price_image_label.place(x=334, y=22)
        sale_price_label = customtkinter.CTkLabel(master=self.__square_status_frame,
                                                  font=("arial", 17), 
                                                  text_color=BLACK_GRAY_COLOR, 
                                                  text="Total price:")
        sale_price_label.place(x=404, y=10)

        self.__sale_price_stringvar = customtkinter.StringVar()
        self.__sale_price_stringvar.set(0.00)
        sale_price_stringvar_label = customtkinter.CTkLabel(master=self.__square_status_frame,
                                                            font=("arial", 19), 
                                                            text_color=GRAY_TEXT_COLOR, 
                                                            textvariable=self.__sale_price_stringvar)
        sale_price_stringvar_label.place(x=449, y=36)

        self.__treeview_tag = "even_row"
        self.__meal_treeview.tag_configure("even_row_2", background=EVEN_ROW_COLOR_2)
        self.__meal_treeview.tag_configure("odd_row_2", background=ODD_ROW_COLOR_2)
        
        self.__fn_read_order_list(meals_info=meals_info, order_id=order_id, antecedent_orders=True)

        self.__meal_treeview.tag_configure("even_row", background=EVEN_ROW_COLOR)
        self.__meal_treeview.tag_configure("odd_row", background=ODD_ROW_COLOR)

        self.__add_button = customtkinter.CTkButton(master=self.__table_toplevel,
            width=100, height=35,
            text_color=WHITE_COLOR,
            fg_color=GREEN_COLOR,
            hover_color=GREEN_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 15), 
            text="Add to list",
            command=lambda:self.__add_to_list(meals_info=meals_info, 
                                              meal=self.__meal_optionmenu.get(), 
                                              total=self.__total_spinbox.get()))
        self.__add_button.place(x=410, y=214)

        antecedent_orders = self.__meal_treeview.get_children()
        self.__remove_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                       width=100, height=35,
                                                       text_color=WHITE_COLOR,
                                                       fg_color=RED_COLOR, 
                                                       hover_color=RED_HOVER_COLOR,
                                                       corner_radius=4,
                                                       font=("arial", 15), 
                                                       text="Remove selected",
                                                       command=lambda:self.__permission_to_remove(parent=self.__table_toplevel, 
                                                                                                  antecedent_orders=antecedent_orders))
        self.__remove_button.place(x=520, y=214)

        previous_meals_ids : list[int] = [self.__meal_treeview.item(children)["values"][0] for children in self.__meal_treeview.get_children()]

        self.__apply_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                      width=230, height=32,
                                                      text_color=WHITE_COLOR,
                                                      fg_color=GREEN_COLOR, 
                                                      hover_color=GREEN_HOVER_COLOR,
                                                      corner_radius=4,
                                                      font=("arial", 15), 
                                                      text="Apply",
                                                      command=lambda:self.__fn_update_order_meals(order_id=order_id, 
                                                                                                  previous_meals_ids=previous_meals_ids, 
                                                                                                  treeview_children=self.__meal_treeview.get_children()))
        self.__apply_button.place(x=412, y=847)

        self.__finish_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                       width=230, height=32,
                                                       text_color=WHITE_COLOR,
                                                       fg_color=ORANGE_COLOR,
                                                       hover_color=ORANGE_HOVER_COLOR,
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text="Finish",
                                                       command=lambda:self.__finalize_order(table_id,
                                                                                            order_id,
                                                                                            waiter,
                                                                                            customer,
                                                                                            self.__total_meal_stringvar.get(),
                                                                                            self.__sale_price_stringvar.get()))
        self.__finish_button.place(x=170, y=847)

    def __finalize_order(self, table_id: int, 
                         order_id: int, 
                         waiter: str, 
                         customer: str, 
                         total_meals: float, 
                         total_price: float) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            text = (
                f"TABLE: {table_id}\nWAITER: {waiter if waiter else "Unregistered"}\n\n"
                f"ORDER ID: {order_id}\n"
                f"CUSTOMER: {customer if customer else "Unregistered"}\n\n"
                "ID, MEAL NAME,  SALE PRICE,  CATEGORY,  STATUS:\n\n"
            )
            for item in self.__meal_treeview.get_children():
                text += str(self.__meal_treeview.item(item, "values")) + "\n"
            text += f"\nTOTAL MEALS: {total_meals}\nTOTAL PRICE: {total_price}"

            with open(file_path, "w") as file:
                file.write(text)
            
            os.system(f"start {file_path}")

        widgets = [self.__meals_label,
                   self.__meal_optionmenu,
                   self.__total_spinbox,
                   self.__add_button,
                   self.__remove_button,
                   self.__apply_button]
        
        for widget in widgets:
            widget.destroy()

        self.__table_toplevel.geometry("669x920+625+50")
        self.__meal_treeview.place(x=25, y=185)
        self.__treeview_scrollbar.place(x=627, y=185, height=472)
        self.__square_status_frame.place(x=25, y=667)
        
        self.__table_toplevel.attributes("-topmost", True)

        payment_frame = customtkinter.CTkFrame(master=self.__table_toplevel,
                                               width=619, height=90,
                                               fg_color=WHITE_COLOR)
        payment_frame.place(x=25, y=770)

        self.__change_stringvar = customtkinter.StringVar()
        self.__change_stringvar.trace_add("write", self.__update_change_stringvar)

        payment_image_label = customtkinter.CTkLabel(master=payment_frame,text="", image=self.__payment_image)
        payment_image_label.place(x=25, y=22)
        payment_label = customtkinter.CTkLabel(master=payment_frame, text_color=GRAY_TEXT_COLOR, font=("arial", 17), text="Payment:")
        payment_label.place(x=95, y=10)
        
        only_numbers = self.__root.register(lambda _ : _.isdigit())

        payment_entry = customtkinter.CTkEntry(master=payment_frame,
                                               width=180, height=30,
                                               border_color=LIGHT_GRAY_COLOR, 
                                               text_color=GRAY_TEXT_COLOR,
                                               validate="key",
                                               validatecommand=(only_numbers, "%P"),
                                               textvariable=self.__change_stringvar,
                                               corner_radius=3, 
                                               font=("arial", 19), 
                                               border_width=1)
        payment_entry.place(x=110, y=39)

        divider_frame = tkinter.Frame(master=payment_frame, height=70, width=1)
        divider_frame.place(x=309, y=10)

        change_image_label = customtkinter.CTkLabel(master=payment_frame, text="", image=self.__change_image)
        change_image_label.place(x=334, y=22)
        change_label = customtkinter.CTkLabel(master=payment_frame, 
                                              text_color=GRAY_TEXT_COLOR, 
                                              font=("arial", 17), 
                                              text="Change:")
        change_label.place(x=404, y=10)
        self.__change_stringvar_label = customtkinter.CTkLabel(master=payment_frame, 
                                                               text_color=RED_HOVER_COLOR,
                                                               font=("arial", 19))
        self.__change_stringvar_label.place(x=443, y=36)

        if self.__sale_price_stringvar.get() == "":
            self.__change_stringvar_label.configure(text="")
            payment_entry.destroy()
        else:
            self.__change_stringvar_label.configure(text=f"-{self.__sale_price_stringvar.get()}")

        back_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                              width=230, height=32,
                                              text_color=WHITE_COLOR,
                                              fg_color=GRAY_COLOR,
                                              hover_color=GRAY_COLOR,
                                              corner_radius=3,
                                              font=("arial", 15),
                                              text="Back",
                                              command=lambda:self.__back_orders_ui(table_id=table_id))
        back_button.place(x=170, y=872)

        self.__finish_button.place(x=412, y=872)
        self.__finish_button.configure(command=lambda:self.__finalize_table(table_id=table_id, 
                                                                            order_id=order_id, 
                                                                            total_price=total_price, 
                                                                            payment=payment_entry.get(), 
                                                                            change=self.__change))

        payment_entry.insert(0, 0)

    def __authorize_remove_ui(self, parent: Toplevel, antecedent_orders: tuple) -> None:
        self.__authorize_remove_toplevel = Toplevel(master=parent)
        self.__authorize_remove_toplevel.title("Authorize Remove")
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.__authorize_remove_toplevel.after(50, lambda: self.__authorize_remove_toplevel.iconbitmap("./images/global_images/icon.ico"))
        self.__authorize_remove_toplevel.geometry("460x340+735+290")
        self.__authorize_remove_toplevel.configure(background=WHITE_COLOR)
        self.__authorize_remove_toplevel.resizable(False, False)
        self.__authorize_remove_toplevel.focus()

        username_label = customtkinter.CTkLabel(master=self.__authorize_remove_toplevel,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 15),
                                                text="  Username:",
                                                compound="left",
                                                image=self.__user_image)
        username_label.grid(row=0, column=0, padx=30, pady=20, sticky=tkinter.W)

        username_entry = customtkinter.CTkEntry(master=self.__authorize_remove_toplevel, 
                                                width=400, height=40,
                                                border_color=LIGHT_GRAY_COLOR,
                                                fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 17),
                                                border_width=1)
        username_entry.grid(row=1, column=0, padx=30, pady=0)
        username_entry.insert(0, AccountDb(self.__token).get_username())
        username_entry.configure(state=tkinter.DISABLED)

        password_label = customtkinter.CTkLabel(master=self.__authorize_remove_toplevel,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                image=self.__password_image)
        password_label.grid(row=2, column=0, padx=30, pady=20, sticky=tkinter.W)

        self.__password_entry = customtkinter.CTkEntry(master=self.__authorize_remove_toplevel,
                                                       width=400, height=40,
                                                       border_color=LIGHT_GRAY_COLOR,
                                                       fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                       text_color=GRAY_TEXT_COLOR,
                                                       font=("arial", 17), 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.grid(row=3, column=0, padx=30, pady=3)

        self.__hide_password = True

        self.__status_password_button = customtkinter.CTkButton(master=self.__authorize_remove_toplevel,
                                                                width=1, height=1, 
                                                                fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                bg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                hover_color=LIGHT_GRAY_HOVER_COLOR, 
                                                                image=self.__hidepassword_image, 
                                                                text="",
                                                                command=self.__show_password)
        self.__status_password_button.place(x=385, y=194)

        confirm_button = customtkinter.CTkButton(master=self.__authorize_remove_toplevel,
                                                 width=400, height=40, 
                                                 fg_color=LIGHT_BLUE_COLOR, 
                                                 hover_color=LIGHT_BLUE_HOVER_COLOR,
                                                 text_color=WHITE_COLOR,
                                                 text="Confirm",
                                                 command=lambda:self.__remove_after_authentication(username=username_entry.get(),
                                                                                                   password=self.__password_entry.get(),
                                                                                                   parent_ui=parent,
                                                                                                   antecedent_orders=antecedent_orders))
        confirm_button.grid(row=4, column=0, padx=30, pady=30)

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

        self.__table_toplevel.focus()
        self.__table_toplevel.bind("<Return>", lambda _ : delete_table_button.invoke())

    def __add_to_list(self, meals_info: list[tuple], meal: str, total: int) -> None:
        meal : tuple = find_tuple_by_name(list_of_tuples=meals_info, tuple_name=meal)
        
        for _ in range(int(total)):
            if meal:
                if self.__treeview_tag == "odd_row":
                    self.__treeview_tag = "even_row"
                else:
                    self.__treeview_tag = "odd_row"
                    
                self.__meal_treeview.insert("", "end", values=meal, tags=self.__treeview_tag)
                
                self.__total_meal_stringvar.set(int(self.__total_meal_stringvar.get()) + 1)
                self.__sale_price_stringvar.set(f"{float(self.__sale_price_stringvar.get()) + float(meal[2]):.2f}")
        
        self.__total_spinbox.delete(0, "end")
        self.__total_spinbox.insert(0, 1)

    def __remove_from_list(self, parent: Toplevel, antecedent_orders: tuple = None) -> None:
        selected_meal : tuple = self.__selected_row(parent=parent)
        if not selected_meal:
            return
        
        self.__meal_treeview.delete(self.__meal_treeview.selection()[0])
        self.__total_meal_stringvar.set(int(self.__total_meal_stringvar.get()) - 1)
        self.__sale_price_stringvar.set(f"{float(self.__sale_price_stringvar.get()) - float(selected_meal[2]):.2f}")

        self.__treeview_tag = "even_row"
        for item_id in self.__meal_treeview.get_children():
            if antecedent_orders and item_id in antecedent_orders:
                if self.__treeview_tag == "odd_row_2":
                    self.__treeview_tag = "even_row_2"
                else:
                    self.__treeview_tag = "odd_row_2"
            else:
                if self.__treeview_tag == "odd_row":
                    self.__treeview_tag = "even_row"
                else:
                    self.__treeview_tag = "odd_row"

            self.__meal_treeview.item(item=item_id, tags=self.__treeview_tag)

    def __permission_to_remove(self, parent: Toplevel, antecedent_orders: tuple) -> None:
        selected_meal : tuple = self.__selected_row(parent=parent)
        if not selected_meal:
            return

        if self.__meal_treeview.selection()[0] in antecedent_orders:
            self.__authorize_remove_ui(parent=parent, antecedent_orders=antecedent_orders)
        else:
            self.__remove_from_list(parent=parent, antecedent_orders=antecedent_orders)

    def __remove_after_authentication(self, username: str, password: str, parent_ui: Toplevel, antecedent_orders: tuple) -> None:
        account = LoginDb(username=username, password=password)
        if account.verify_credentials():
            self.__remove_from_list(parent=parent_ui, antecedent_orders=antecedent_orders)
            self.__authorize_remove_toplevel.destroy()
        else:
            self.__table_toplevel.focus()
            self.__authorize_remove_toplevel.focus()

    def __fn_create_table_id(self, table_id: int) -> None:
        entry_items = {"table id": table_id}
        if not empty_entries(**entry_items):
            if TableDb(self.__token).create_table_id(table_id):
                self._to_back()

    def __fn_create_table(self, multiplier: int) -> None:
            if multiplier > 0:
                if TableDb(self.__token).create_table(multiplier=multiplier):
                    messagebox.showinfo(title=None, message="Table created successfully")
                    self.__table_toplevel.destroy()
                    self._to_back()

    def __fn_create_initial_order(self, table_id: int, waiter_name: str, customer_name: str, treeview_children: tuple) -> None:
        try:
            waiter_id = None if waiter_name == "No waiter registered" else WaiterDb(self.__token).get_waiter_id_by_name(waiter_name)
            customer_id = None if customer_name == "No customer registered" or "Unregistered" else CustomerDb(self.__token).get_customer_id_by_name(customer_name)
            
            meals_ids : list[int] = [self.__meal_treeview.item(children)["values"][0] for children in treeview_children]
            
            order = OrderDb(self.__token)
            order_id = order.create_order_id(waiter_id=waiter_id, customer_id=customer_id)
            
            order.add_meal_to_order(order_id=order_id, meals_ids=meals_ids)
            TableDb(self.__token).set_table_order(order_id=order_id, table_id=table_id)
            
        except Exception as error:
            messagebox.showerror(title="Create Order Error", message=error)
        else:
            self._to_back()

    def __fn_read_order_list(self, meals_info: list[tuple], order_id: int, antecedent_orders: bool = False) -> None:
        if antecedent_orders == True:
            even_row_tag, odd_row_tag = "even_row_2", "odd_row_2"
        else:
            even_row_tag, odd_row_tag = "even_row", "odd_row"

        for m, q in OrderDb(self.__token).read_order_list(order_id=order_id):
            for _ in range(q):
                meal : tuple = find_tuple_by_name(list_of_tuples=meals_info, tuple_name=m)
                
                self.__total_meal_stringvar.set(int(self.__total_meal_stringvar.get()) + 1)
                self.__sale_price_stringvar.set(f"{float(self.__sale_price_stringvar.get()) + float(meal[2]):.2f}")

                if self.__treeview_tag == odd_row_tag:
                    self.__treeview_tag = even_row_tag
                else:
                    self.__treeview_tag = odd_row_tag
                
                self.__meal_treeview.insert("", "end", values=meal, tags=self.__treeview_tag)

    def __fn_update_order_meals(self, order_id: int, previous_meals_ids: list, treeview_children: tuple) -> None:
        try:
            current_meal_ids : list[int] = [self.__meal_treeview.item(children)["values"][0] for children in treeview_children]
            meals_ids_removed = list()
            
            for i in previous_meals_ids:
                if i not in current_meal_ids and i not in meals_ids_removed:
                    meals_ids_removed.append(i)

            orderbd = OrderDb(self.__token)
            orderbd.update_order_meals(order_id=order_id, 
                                       previous_meals_ids=previous_meals_ids, 
                                       meals_ids=current_meal_ids)
            if meals_ids_removed:
                orderbd.delete_meals_from_order(order_id, *meals_ids_removed)

        except Exception as error:
            messagebox.showerror(title="Update Order Meals Error", message=error)
        else:
            self._to_back()
            messagebox.showinfo(title=None, message="Table orders updated successfully.")

    def __fn_delete_table(self, table_id: int) -> None:
        if TableDb(self.__token).delete_table(table_id):
            self._to_back()
        else:
            self.__table_toplevel.focus()

    def __update_change_stringvar(self, *args) -> None:
        try:
            self.__change = float(self.__change_stringvar.get()) - float(self.__sale_price_stringvar.get())
            self.__change_stringvar_label.configure(text=f"{self.__change:.2f}")
            if self.__change < 0:
                self.__change_stringvar_label.configure(text_color=RED_HOVER_COLOR)
            else:
                self.__change_stringvar_label.configure(text_color=BLACK_GRAY_COLOR)
        except:
            self.__change_stringvar_label.configure(text=f"-{self.__sale_price_stringvar.get()}")

    def __selected_row(self, parent: Toplevel) -> tuple:
        try:
            selected_meal = self.__meal_treeview.item(self.__meal_treeview.selection()[0], "values")
            return selected_meal
        except IndexError:
            messagebox.showerror(parent=parent, title=None, message="Please select a meal")

    def __show_password(self) -> None:
        if self.__hide_password:
            self.__status_password_button.configure(image=self.__showpassword_image)
            self.__password_entry.configure(show="")
            self.__hide_password = False
        else:
            self.__status_password_button.configure(image=self.__hidepassword_image)
            self.__password_entry.configure(show="*")
            self.__hide_password = True

    def __finalize_table(self, table_id: int, order_id: int, total_price: float, payment: float, change: float) -> None:
        if self.__sale_price_stringvar.get() == "" or self.__change >= 0:
            remove_customer = TableDb(self.__token).remove_order_from_table(table_id=table_id,
                                                                                 order_id=order_id, 
                                                                                 total_price=float(total_price), 
                                                                                 payment=float(payment), 
                                                                                 change=float(change))
            if remove_customer:
                self.__table_toplevel.destroy()
                messagebox.showinfo(title=None, message="Table closed successfully.")
            self._to_back()

    def __back_orders_ui(self, table_id: int) -> None:
        self.__table_toplevel.destroy()
        self.__table_with_orders_ui(table_id=table_id)

    def _to_back(self) -> None:
        self.__table_toplevel.destroy()
        clear_frames(self.__square_frame)
        self.__table_ui()
