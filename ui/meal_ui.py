import tkinter
from tkinter import ttk

import customtkinter

from utils.colors import *
from database import CategoryDb
from database import MealDb
from database.account_db import LoginDb
from utils import clear_frames

class MealUI:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self.__root = root
        self.__square_frame = square_frame
        self.__token = token

        clear_frames(self.__square_frame)
        self.__meal_ui()

    def __topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        self.__topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                                     font=("arial black", 25),
                                                     text_color=WHITE_COLOR, 
                                                     text="Meal")
        self.__topbar_label.place(x=20, y=5)

        self.__search_meals_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                           width=1227, height=35,
                                                           fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                           border_color=LIGHT_GRAY_COLOR, 
                                                           placeholder_text="Search by meal name",
                                                           font=("arial", 17), 
                                                           border_width=1)
        self.__search_meals_entry.place(x=174, y=8)

        self.__search_meals_button = customtkinter.CTkButton(master=topbar_frame,
                                                             width=230, height=32,
                                                             text_color=WHITE_COLOR,
                                                             fg_color=LIGHT_BLUE_COLOR, 
                                                             hover_color=LIGHT_BLUE_HOVER_COLOR,
                                                             corner_radius=4,
                                                             font=("arial", 15), 
                                                             text="Search",
                                                             command=lambda:self.__fn_search_meal(self.__search_meals_entry.get()))
        self.__search_meals_button.place(x=1425, y=9)

        self.__root.bind("<Return>", lambda _ : self.__search_meals_button.invoke())

    def __info_widgets(self) -> None:
        enabledmeals_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                    width=285, height=170,
                                                    corner_radius=8,
                                                    fg_color=GREEN_COLOR)
        enabledmeals_frame.place(x=20, y=70)
        enabledmeals_label = customtkinter.CTkLabel(master=enabledmeals_frame,
                                                    text_color=WHITE_COLOR, 
                                                    font=("Arial", 21, "italic"),
                                                    text="Total Enabled Meals")
        enabledmeals_label.place(x=20, y=15)
        totalenabled_label = customtkinter.CTkLabel(master=enabledmeals_frame,
                                                    text_color=WHITE_COLOR,
                                                    font=("arial black", 25),
                                                    text=f"{MealDb(self.__token).count_meals_by_status(status='Enabled'):^26}")
        totalenabled_label.place(x=30, y=72)


        disabledmeals_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                     fg_color=RED_COLOR,
                                                     width=285, height=170,
                                                     corner_radius=8)
        disabledmeals_frame.place(x=20, y=260)
        disabledmeals_label = customtkinter.CTkLabel(master=disabledmeals_frame,
                                                     text_color=WHITE_COLOR,
                                                     font=("Arial", 21, "italic"),
                                                     text="Total Disabled Meals")
        disabledmeals_label.place(x=20, y=15)
        totaldisabled_label = customtkinter.CTkLabel(master=disabledmeals_frame,
                                                     text_color=WHITE_COLOR,
                                                     font=("arial black", 25),
                                                     text=f"{MealDb(self.__token).count_meals_by_status(status='Disabled'):^26}")
        totaldisabled_label.place(x=30, y=72)


        totalmeals_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                  width=285, height=170,
                                                  fg_color=LIGHT_BLUE_COLOR,
                                                  corner_radius=8)
        totalmeals_frame.place(x=20, y=450)
        totalmeals_label = customtkinter.CTkLabel(master=totalmeals_frame,
                                                  text_color=WHITE_COLOR, 
                                                  font=("Arial", 21, "italic"),
                                                  text="Total Meals")
        totalmeals_label.place(x=20, y=15)
        total_label = customtkinter.CTkLabel(master=totalmeals_frame,
                                             text_color=WHITE_COLOR,
                                             font=("arial black", 25),
                                             text=f"{MealDb(self.__token).count_meals():^26}")
        total_label.place(x=30, y=72)

    def __meal_ui(self) -> None:
        self.__topbar()
        self.__info_widgets()

        # https://stackoverflow.com/questions/75492266/changing-font-style-of-rows-in-treeview
        style = ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground=BLACK_GRAY_COLOR)
        style.configure("Treeview", font=("Arial", 13), foreground=BLACK_GRAY_COLOR, rowheight=28)

        self.__meal_treeview = ttk.Treeview(master=self.__square_frame,
                                            height=28,
                                            style="style_treeview.Treeview",
                                            columns=("meal id", "meal name", "sale price", "category", "status"),
                                            show="headings")
        self.__meal_treeview.place(x=325, y=50)

        self.__meal_treeview.heading("#1", text="meal id", anchor="center")
        self.__meal_treeview.heading("#2", text="meal name", anchor="center")
        self.__meal_treeview.heading("#3", text="sale price", anchor="center")
        self.__meal_treeview.heading("#4", text="category", anchor="center")
        self.__meal_treeview.heading("#5", text="status", anchor="center")

        self.__meal_treeview.column("#1", minwidth=150, width=200, anchor="center")
        self.__meal_treeview.column("#2", minwidth=200, width=350, anchor="center")
        self.__meal_treeview.column("#3", minwidth=100, width=250, anchor="center")
        self.__meal_treeview.column("#4", minwidth=240, width=290, anchor="center")
        self.__meal_treeview.column("#5", minwidth=100, width=250, anchor="center")

        self.__treeview_scrollbar = tkinter.Scrollbar(self.__square_frame, orient=tkinter.VERTICAL, command=self.__meal_treeview.yview)
        self.__meal_treeview.configure(yscroll=self.__treeview_scrollbar.set)
        self.__treeview_scrollbar.place(x=1660, y=50, height=808)

        divider_frame = tkinter.Frame(master=self.__square_frame, 
                                      height=55, width=1678, 
                                      bg=LIGHT_GRAY_COLOR)
        divider_frame.place(x=0, y=860)

        del_meal_button = customtkinter.CTkButton(master=self.__square_frame,
                                                  width=230, height=32,
                                                  text_color=WHITE_COLOR,
                                                  fg_color=RED_COLOR,
                                                  hover_color=RED_HOVER_COLOR,
                                                  bg_color=LIGHT_GRAY_COLOR,
                                                  corner_radius=3,
                                                  font=("arial", 15),
                                                  text="Delete Meal",
                                                  command=self.__fn_delete_meal)
        del_meal_button.place(x=905, y=868)

        update_meal_button = customtkinter.CTkButton(master=self.__square_frame,
                                                     width=230, height=32,
                                                     fg_color=ORANGE_COLOR,
                                                     hover_color=ORANGE_HOVER_COLOR,
                                                     bg_color=LIGHT_GRAY_COLOR, 
                                                     text_color=WHITE_COLOR,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text="Update Meal",
                                                     command=self.__update_meal_ui)
        update_meal_button.place(x=1165, y=868)

        create_meal_button = customtkinter.CTkButton(master=self.__square_frame,
                                                     width=230, height=32,
                                                     fg_color=GREEN_COLOR,
                                                     hover_color=GREEN_HOVER_COLOR,
                                                     bg_color=LIGHT_GRAY_COLOR, 
                                                     text_color=WHITE_COLOR,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text="Add Meal",
                                                     command=self.__create_meal_ui)
        create_meal_button.place(x=1425, y=868)

        treeview_scrollbar = tkinter.Scrollbar(self.__square_frame, 
                                               orient=tkinter.VERTICAL, 
                                               command=self.__meal_treeview.yview)
        self.__meal_treeview.configure(yscroll=treeview_scrollbar.set)
        treeview_scrollbar.place(x=1660, y=50, height=808)

        self.__fn_read_meals()

    def __create_meal_ui(self) -> None:
        clear_frames(self.__square_frame)
        self.__topbar()
        
        self.__topbar_label.configure(text="Add Meal")
        self.__search_meals_entry.destroy()
        self.__search_meals_button.destroy()

        add_meal_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                width=1668, height=440,
                                                fg_color=WHITE_COLOR,
                                                corner_radius=10)
        add_meal_frame.place(x=5, y=55)

        meal_name_label = customtkinter.CTkLabel(master=add_meal_frame,
                                                 font=("arial bold", 17),
                                                 text_color=GRAY_TEXT_COLOR,
                                                 text="Meal Name:")
        meal_name_label.place(x=25, y=25)

        self.__meal_name_entry = customtkinter.CTkEntry(master=add_meal_frame,
                                                        width=1618, height=35,
                                                        border_color=LIGHT_GRAY_COLOR, 
                                                        corner_radius=3, 
                                                        font=("arial", 17), 
                                                        border_width=1)
        self.__meal_name_entry.place(x=25, y=62)

        sale_price_label = customtkinter.CTkLabel(master=add_meal_frame,
                                                  font=("arial bold", 17),
                                                  text_color=GRAY_TEXT_COLOR,
                                                  text="Sale Price:")
        sale_price_label.place(x=25, y=120)

        self.__sale_price_entry = customtkinter.CTkEntry(master=add_meal_frame,
                                                         width=1618, height=35,
                                                         border_color=LIGHT_GRAY_COLOR,
                                                         placeholder_text_color=GRAY_TEXT_COLOR,
                                                         corner_radius=3, 
                                                         font=("arial", 17), 
                                                         border_width=1)
        self.__sale_price_entry.place(x=25, y=160)
        
        category_label = customtkinter.CTkLabel(master=add_meal_frame,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial bold", 17),
                                                text="Category:")
        category_label.place(x=25, y=215)

        category_names : list[str] = CategoryDb(self.__token).get_category_names()
        self.__category_optionmenu = customtkinter.CTkOptionMenu(master=add_meal_frame,
            width=1618, height=35,
            fg_color=FG_OPTION_MENU_COLOR,
            text_color=GRAY_TEXT_COLOR,
            button_color=GRAY_COLOR,
            button_hover_color=GRAY_HOVER_COLOR,
            corner_radius=4,
            font=("arial", 17),
            dropdown_font=("arial", 15),
            values=category_names if category_names else ["No categories available"],
            state=tkinter.NORMAL if category_names else tkinter.DISABLED
        )
        self.__category_optionmenu.place(x=25, y=255)

        status_label = customtkinter.CTkLabel(master=add_meal_frame,
                                              text_color=GRAY_TEXT_COLOR,
                                              font=("arial bold", 17),
                                              text="Status:")
        status_label.place(x=25, y=310)

        self.__status_optionmenu = customtkinter.CTkOptionMenu(master=add_meal_frame,
                                                               width=1618, height=35,
                                                               fg_color=FG_OPTION_MENU_COLOR,
                                                               text_color=GRAY_TEXT_COLOR,
                                                               button_color=GRAY_COLOR,
                                                               button_hover_color=GRAY_HOVER_COLOR,
                                                               corner_radius=4,
                                                               font=("arial", 17),
                                                               dropdown_font=("arial", 15),
                                                               values=["Enabled", "Disabled"])
        self.__status_optionmenu.place(x=25, y=350)
        self.__status_optionmenu.set("Enabled")

        divider_frame = tkinter.Frame(master=self.__square_frame, 
                                      height=55, width=1678, 
                                      bg=LIGHT_GRAY_COLOR)
        divider_frame.place(x=0, y=860)

        add_meal_button = customtkinter.CTkButton(master=self.__square_frame,
                                                  width=230, height=32,
                                                  fg_color=GREEN_COLOR,
                                                  hover_color=GREEN_HOVER_COLOR,
                                                  bg_color=LIGHT_GRAY_COLOR, 
                                                  text_color=WHITE_COLOR,
                                                  corner_radius=3,
                                                  font=("arial", 15),
                                                  text="Add Meal",
                                                  command=self.__fn_create_meal)
        add_meal_button.place(x=1165, y=868)

        self.__root.bind("<Return>", lambda _ : add_meal_button.invoke())
    
        self.__cancel_button = customtkinter.CTkButton(master=self.__square_frame,
                                                       width=230, height=32,
                                                       text_color=WHITE_COLOR,
                                                       fg_color=GRAY_COLOR,
                                                       hover_color=GRAY_HOVER_COLOR,
                                                       bg_color=LIGHT_GRAY_COLOR, 
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text="Cancel",
                                                       command=self._to_back)
        self.__cancel_button.place(x=1425, y=868)

    def __update_meal_ui(self) -> None:
        data = self.__selected_row()
        if not data:
            return

        clear_frames(self.__square_frame) 
        self.__topbar()
        
        self.__topbar_label.configure(text="Update Meal")
        self.__search_meals_entry.destroy()
        self.__search_meals_button.destroy()

        update_meal_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                   width=1668, height=545,
                                                   fg_color=WHITE_COLOR,
                                                   corner_radius=10)
        update_meal_frame.place(x=5, y=55)

        meal_id_label = customtkinter.CTkLabel(master=update_meal_frame,
                                               font=("arial bold", 17),
                                               text_color=GRAY_TEXT_COLOR,
                                               text="ID:")
        meal_id_label.place(x=25, y=25)

        self.__meal_id_entry = customtkinter.CTkEntry(master=update_meal_frame,
                                                      width=1618, height=35,
                                                      border_color=LIGHT_GRAY_COLOR, 
                                                      corner_radius=3, 
                                                      font=("arial", 17), 
                                                      border_width=1)
        self.__meal_id_entry.place(x=25, y=62)

        meal_name_label = customtkinter.CTkLabel(master=update_meal_frame,
                                                 font=("arial bold", 17),
                                                 text_color=GRAY_TEXT_COLOR,
                                                 text="Meal Name:")
        meal_name_label.place(x=25, y=120)

        self.__meal_name_entry = customtkinter.CTkEntry(master=update_meal_frame,
                                                        width=1618, height=35,
                                                        border_color=LIGHT_GRAY_COLOR,
                                                        corner_radius=3, 
                                                        font=("arial", 17), 
                                                        border_width=1)
        self.__meal_name_entry.place(x=25, y=160)

        sale_price_label = customtkinter.CTkLabel(master=update_meal_frame,
                                                  font=("arial bold", 17),
                                                  text_color=GRAY_TEXT_COLOR,
                                                  text="Sale Price:")
        sale_price_label.place(x=25, y=215)

        self.__sale_price_entry = customtkinter.CTkEntry(master=update_meal_frame,
                                                         width=1618, height=35,
                                                         border_color=LIGHT_GRAY_COLOR,
                                                         corner_radius=3, 
                                                         font=("arial", 17),
                                                         border_width=1)
        self.__sale_price_entry.place(x=25, y=255)

        category_label = customtkinter.CTkLabel(master=update_meal_frame,
                                                font=("arial bold", 17),
                                                text_color=GRAY_TEXT_COLOR,
                                                text="Category:")
        category_label.place(x=25, y=310)

        self.__category_optionmenu = customtkinter.CTkOptionMenu(master=update_meal_frame,
                                                                 width=1618, height=35,
                                                                 fg_color=FG_OPTION_MENU_COLOR,
                                                                 text_color=GRAY_TEXT_COLOR,
                                                                 button_color=GRAY_COLOR,
                                                                 button_hover_color=GRAY_HOVER_COLOR,
                                                                 corner_radius=4,
                                                                 font=("arial", 17),
                                                                 dropdown_font=("arial", 15),
                                                                 values=CategoryDb(self.__token).get_category_names())
        self.__category_optionmenu.place(x=25, y=350)

        status_label = customtkinter.CTkLabel(master=update_meal_frame,
                                              text_color=GRAY_TEXT_COLOR,
                                              font=("arial bold", 17),
                                              text="Status:")
        status_label.place(x=25, y=405)

        self.__status_optionmenu = customtkinter.CTkOptionMenu(master=update_meal_frame,
                                                               width=1618, height=35,
                                                               fg_color=FG_OPTION_MENU_COLOR,
                                                               text_color=GRAY_TEXT_COLOR,
                                                               button_color=GRAY_COLOR,
                                                               button_hover_color=GRAY_HOVER_COLOR,
                                                               corner_radius=4,
                                                               font=("arial", 17),
                                                               dropdown_font=("arial", 15),
                                                               values=["Enabled", "Disabled"])
        self.__status_optionmenu.place(x=25, y=445)
        self.__status_optionmenu.set("Enabled")

        divider_frame = tkinter.Frame(master=self.__square_frame, 
                                      height=55, width=1678, 
                                      bg=LIGHT_GRAY_COLOR)
        divider_frame.place(x=0, y=860)

        update_meal_button = customtkinter.CTkButton(master=self.__square_frame,
                                                     width=230, height=32,
                                                     fg_color=GREEN_COLOR,
                                                     hover_color=GREEN_HOVER_COLOR,
                                                     bg_color=LIGHT_GRAY_COLOR,
                                                     text_color=WHITE_COLOR,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text="Save Changes",
                                                     command=self.__fn_update_meal)
        update_meal_button.place(x=1165, y=868)

        self.__root.bind("<Return>", lambda _ : update_meal_button.invoke())
    
        self.__cancel_button = customtkinter.CTkButton(master=self.__square_frame,
                                                       width=230, height=32,
                                                       text_color=WHITE_COLOR,
                                                       fg_color=GRAY_COLOR,
                                                       hover_color=GRAY_HOVER_COLOR,
                                                       bg_color=LIGHT_GRAY_COLOR, 
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text="Cancel",
                                                       command=self._to_back)
        self.__cancel_button.place(x=1425, y=868)
        
        list_entries = [self.__meal_id_entry, 
                        self.__meal_name_entry, 
                        self.__sale_price_entry]
        self.__insert_data_entries(data=data, list_entries=list_entries)

    def __fn_create_meal(self) -> None:
        if MealDb(self.__token).create_meal(meal_name=self.__meal_name_entry.get(),
                                            sale_price=self.__sale_price_entry.get(),
                                            category_category_id=CategoryDb(self.__token).get_category_id(self.__category_optionmenu.get()),
                                            status=self.__status_optionmenu.get()):
             self._to_back()
    
    def __fn_read_meals(self) -> None:
        self.__meal_treeview.delete(*self.__meal_treeview.get_children())

        all_meals = [i for i in MealDb(token=self.__token).read_meals()]

        self.__meal_treeview.tag_configure("even_row", background=EVEN_ROW_COLOR)
        self.__meal_treeview.tag_configure("odd_row", background=ODD_ROW_COLOR)
        
        tag = "even_row"
        for i in all_meals:
            tag = "even_row" if tag == "odd_row" else "odd_row"
            self.__meal_treeview.insert("", "end", values=i, tags=tag)

    def __fn_update_meal(self) -> None:
        if MealDb(token=self.__token).update_meal(meal_id=self.__meal_id_entry.get(),
                                                  meal_name=self.__meal_name_entry.get(),
                                                  sale_price=self.__sale_price_entry.get(),
                                                  category_category_id=CategoryDb(self.__token).get_category_id(self.__category_optionmenu.get()),
                                                  status=self.__status_optionmenu.get()):
              self._to_back()

    def __fn_delete_meal(self) -> None:
        data = self.__selected_row()
        if not data:
            return
          
        message = f"Are you sure you want to delete\nthis meal? {data[1]}."
        if tkinter.messagebox.askyesno(title="Delete Meal", 
                                       message=message, 
                                       icon=tkinter.messagebox.WARNING) == True:
            if MealDb(self.__token).delete_meal(meal_id=data[0]):
                self._to_back()

    def __fn_search_meal(self, typed: str) -> None:
        self.__meal_treeview.delete(*self.__meal_treeview.get_children())

        meal = MealDb(self.__token).search_meal(typed=typed)

        tag = "even_row"
        for i in meal:
            tag = "even_row" if tag == "odd_row" else "odd_row"
            self.__meal_treeview.insert("", "end", values=i, tags=tag)
            
    def __insert_data_entries(self, data: tuple, list_entries: list) -> None:
        for k, v in enumerate(list_entries):
            v.insert(0, data[k])
        
        self.__category_optionmenu.set(data[3])
        self.__status_optionmenu.set(data[4])

        self.__meal_id_entry.configure(state="disabled", fg_color=LIGHT_GRAY_COLOR, border_color=WHITE_COLOR)

    def __selected_row(self) -> tuple:
        try:
            selected_meal = self.__meal_treeview.item(self.__meal_treeview.selection()[0], "values")
            return selected_meal
        except IndexError:
            tkinter.messagebox.showerror(title=None, message="Please select a meal")
    
    def _to_back(self) -> None:
        clear_frames(self.__square_frame)
        self.__meal_ui()
