import tkinter
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk

from PIL import Image
import customtkinter

from utils.colors import *
from database.account_db import LoginDb
from database import CustomerDb
from database import MealDb
from database import TableDb
from database import WaiterDb
from utils import clear_frames
from utils import empty_entries

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

    def __images_ui(self):
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        mealpil_image = Image.open("./images/tables_images/meal.png")
        self.__meal_image = customtkinter.CTkImage(dark_image=mealpil_image,
                                                   light_image=mealpil_image,
                                                   size=(47,47))
        
        pricepil_image = Image.open("./images/tables_images/price.png")
        self.__price_image = customtkinter.CTkImage(dark_image=pricepil_image,
                                                    light_image=pricepil_image,
                                                    size=(47,47))
        
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

        waiter_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
            width=250, height=35,
            fg_color=FG_OPTION_MENU_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=GRAY_COLOR,
            button_hover_color=GRAY_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=WaiterDb(self.__token).get_waiter_names() if WaiterDb(self.__token).get_waiter_names() else ["No waiter registered"],
            state=tkinter.NORMAL if WaiterDb(self.__token).get_waiter_names() else tkinter.DISABLED
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

        id_table_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                                text_color=BLACK_GRAY_COLOR,
                                                font=("arial bold", 17),
                                                text="Table:")
        id_table_label.place(x=25, y=10)

        id_table_entry = customtkinter.CTkEntry(master=self.__table_toplevel,
                                                width=150, height=35,
                                                border_color=WHITE_COLOR,
                                                fg_color=LIGHT_GRAY_COLOR,
                                                corner_radius=3,
                                                border_width=1, 
                                                font=("arial", 17))
        id_table_entry.place(x=25, y=47)
        id_table_entry.insert(0, table_id)
        id_table_entry.configure(state="disabled")

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

        customer_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
            width=619, height=35,
            fg_color=WHITE_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=OPTION_MENU_BUTTON_COLOR,
            button_hover_color=OPTION_MENU_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=CustomerDb(self.__token).get_customer_names() if CustomerDb(self.__token).get_customer_names() else ["No customer registered"],
            state=tkinter.NORMAL if CustomerDb(self.__token).get_customer_names() else tkinter.DISABLED
        )
        customer_optionmenu.place(x=25, y=132)

        meals_label = customtkinter.CTkLabel(master=self.__table_toplevel,
                                             font=("arial bold", 17),
                                             text_color=GRAY_TEXT_COLOR,
                                             text="Meals:")
        meals_label.place(x=25, y=180)

        meal_optionmenu = customtkinter.CTkOptionMenu(master=self.__table_toplevel,
            width=300, height=35,
            fg_color=WHITE_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=OPTION_MENU_BUTTON_COLOR,
            button_hover_color=OPTION_MENU_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=MealDb(self.__token).get_meal_names() if MealDb(self.__token).get_meal_names() else ["No meal registered"],
            state=tkinter.NORMAL if MealDb(self.__token).get_meal_names() else tkinter.DISABLED
        )
        meal_optionmenu.place(x=25, y=214)

        self.__total_spinbox = tkinter.Spinbox(master=self.__table_toplevel,
                                             width=3,
                                             font=("arial", 19),
                                             from_=1, to=100)
        self.__total_spinbox.place(x=336, y=215)

        add_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                             width=100, height=35,
                                             text_color=WHITE_COLOR,
                                             fg_color=GREEN_COLOR,
                                             hover_color=GREEN_HOVER_COLOR,
                                             corner_radius=4,
                                             font=("arial", 15), 
                                             text="Add to list",
                                             command=lambda:self.__add_to_list(meal=meal_optionmenu.get(), total=self.__total_spinbox.get()))
        add_button.place(x=410, y=214)

        remove_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                width=100, height=35,
                                                text_color=WHITE_COLOR,
                                                fg_color=RED_COLOR, 
                                                hover_color=RED_HOVER_COLOR,
                                                corner_radius=4,
                                                font=("arial", 15), 
                                                text="Remove selected",
                                                command=lambda:self.__remove_from_list(parent=self.__table_toplevel))
        remove_button.place(x=520, y=214)

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

        self.__treeview_scrollbar = tkinter.Scrollbar(master=self.__table_toplevel, orient=tkinter.VERTICAL, command=self.__meal_treeview.yview)
        self.__meal_treeview.configure(yscroll=self.__treeview_scrollbar.set)
        self.__treeview_scrollbar.place(x=627, y=260, height=248)

        self.__treeview_tag = "even_row"

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

        divider_frame = tkinter.Frame(master=square_status_frame, height=70, width=1)
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
                                                            text_color="#383838", 
                                                            textvariable=self.__sale_price_stringvar)
        sale_price_stringvar_label.place(x=449, y=36)

        start_order_button = customtkinter.CTkButton(master=self.__table_toplevel,
                                                     width=230, height=32,
                                                     text_color=WHITE_COLOR,
                                                     fg_color=GREEN_COLOR, 
                                                     hover_color=GREEN_HOVER_COLOR,
                                                     corner_radius=4,
                                                     font=("arial", 15), 
                                                     text="Start Order")
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

    def __add_to_list(self, meal: str, total: int) -> None:
        self.__meal_treeview.tag_configure("even_row", background=EVEN_ROW_COLOR)
        self.__meal_treeview.tag_configure("odd_row", background=ODD_ROW_COLOR)

        meal = MealDb(self.__token).get_meal_by_name(meal)
        
        for _ in range(int(total)):
            if meal:
                self.__treeview_tag = "even_row" if self.__treeview_tag == "odd_row" else "odd_row"
                self.__meal_treeview.insert("", "end", values=meal, tags=self.__treeview_tag)
                
                self.__total_meal_stringvar.set(int(self.__total_meal_stringvar.get()) + 1)
                self.__sale_price_stringvar.set(f"{float(self.__sale_price_stringvar.get()) + float(meal[2]):.2f}")
        
        self.__total_spinbox.delete(0, "end")
        self.__total_spinbox.insert(0, 1)

    def __remove_from_list(self, parent: Toplevel) -> None:
        selected_meal : tuple = self.__selected_row(parent=parent)
        if not selected_meal:
            return
        
        self.__meal_treeview.delete(self.__meal_treeview.selection()[0])
        self.__total_meal_stringvar.set(int(self.__total_meal_stringvar.get()) - 1)
        self.__sale_price_stringvar.set(f"{float(self.__sale_price_stringvar.get()) - float(selected_meal[2]):.2f}")

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

    def __fn_delete_table(self, table_id: int) -> None:
        if TableDb(self.__token).delete_table(table_id):
            self._to_back()

    def __selected_row(self, parent: Toplevel) -> tuple:
        try:
            selected_meal = self.__meal_treeview.item(self.__meal_treeview.selection()[0], "values")
            return selected_meal
        except IndexError:
            messagebox.showerror(parent=parent, title=None, message="Please select a meal")

    def _to_back(self) -> None:
        self.__table_toplevel.destroy()
        clear_frames(self.__square_frame)
        self.__table_ui()
