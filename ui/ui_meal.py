from database import DbLogin
from utils import clear_frames
import tkinter
from tkinter import ttk
import customtkinter

class UiMeal:
    @DbLogin.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self._root = root
        self._square_frame = square_frame
        self.__token = token

        clear_frames(self._square_frame)
        self._ui_meal()

    def _topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        self._topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                                    font=("arial black", 25),
                                                    text_color="#ffffff", 
                                                    text="Meal")
        self._topbar_label.place(x=20, y=5)

        self._search_meals_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                          width=1227, height=35,
                                                          placeholder_text="Search by meal name",
                                                          font=("arial", 17), 
                                                          fg_color="#EEEEEE", 
                                                          border_color="#e3e3e3", 
                                                          border_width=1)
        self._search_meals_entry.place(x=174, y=8)

        self._search_meals_button = customtkinter.CTkButton(master=topbar_frame,
                                                            width=230, height=32,
                                                            corner_radius=4,
                                                            text_color="#ffffff",
                                                            font=("arial", 15), 
                                                            text="Search",
                                                            fg_color="#407ecf", 
                                                            hover_color="#6996d1")
        self._search_meals_button.place(x=1425, y=9)

    def _info_widgets(self) -> None:
        enabledmeals_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                    width=285, height=170,
                                                    corner_radius=8,
                                                    fg_color="#4bb34b")
        enabledmeals_frame.place(x=20, y=70)
        enabledmeals_label = customtkinter.CTkLabel(master=enabledmeals_frame,
                                                    font=("Arial", 21, "italic"),
                                                    text_color="#ffffff", 
                                                    text="Total Enabled Meals")
        enabledmeals_label.place(x=20, y=15)
        totalenabled_label = customtkinter.CTkLabel(master=enabledmeals_frame,
                                                    font=("arial black", 25),
                                                    text_color="#ffffff",
                                                    text=None)
        totalenabled_label.place(x=30, y=72)

        disabledmeals_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                     width=285, height=170,
                                                     corner_radius=8,
                                                     fg_color="#d64b4b")
        disabledmeals_frame.place(x=20, y=260)
        disabledmeals_label = customtkinter.CTkLabel(master=disabledmeals_frame,
                                                     font=("Arial", 21, "italic"),
                                                     text_color="#ffffff", 
                                                     text="Total Disabled Meals")
        disabledmeals_label.place(x=20, y=15)
        totaldisabled_label = customtkinter.CTkLabel(master=disabledmeals_frame,
                                                     font=("arial black", 25),
                                                     text_color="#ffffff",
                                                     text=None)
        totaldisabled_label.place(x=30, y=72)

        totalmeals_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                  width=285, height=170,
                                                  corner_radius=8,
                                                  fg_color="#407ecf")
        totalmeals_frame.place(x=20, y=450)
        totalmeals_label = customtkinter.CTkLabel(master=totalmeals_frame,
                                                  font=("Arial", 21, "italic"),
                                                  text_color="#ffffff", 
                                                  text="Total Meals")
        totalmeals_label.place(x=20, y=15)
        total_label = customtkinter.CTkLabel(master=totalmeals_frame,
                                             font=("arial black", 25),
                                             text_color="#ffffff",
                                             text=None)
        total_label.place(x=30, y=72)

    def _ui_meal(self) -> None:
        self._topbar()
        self._info_widgets()

        # https://stackoverflow.com/questions/75492266/changing-font-style-of-rows-in-treeview
        style = ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.__meal_treeview = ttk.Treeview(master=self._square_frame,
                                            height=28,
                                            style="style_treeview.Treeview",
                                            columns=("id meal", "meal name", "sale price", "category", "status"),
                                            show="headings")
        self.__meal_treeview.place(x=325, y=50)

        self.__meal_treeview.heading("#1", text="id meal", anchor="center")
        self.__meal_treeview.heading("#2", text="meal name", anchor="center")
        self.__meal_treeview.heading("#3", text="sale price", anchor="center")
        self.__meal_treeview.heading("#4", text="category", anchor="center")
        self.__meal_treeview.heading("#5", text="status", anchor="center")

        self.__meal_treeview.column("#1", minwidth=150, width=200, anchor="center")
        self.__meal_treeview.column("#2", minwidth=200, width=350, anchor="center")
        self.__meal_treeview.column("#3", minwidth=100, width=250, anchor="center")
        self.__meal_treeview.column("#4", minwidth=240, width=290, anchor="center")
        self.__meal_treeview.column("#5", minwidth=100, width=250, anchor="center")

        self.treeview_scrollbar = tkinter.Scrollbar(self._square_frame, orient=tkinter.VERTICAL, command=self.__meal_treeview.yview)
        self.__meal_treeview.configure(yscroll=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(x=1660, y=50, height=808)

        divider_frame = tkinter.Frame(master=self._square_frame, 
                                      height=55, width=1678, 
                                      bg="#b4b5b8")
        divider_frame.place(x=0, y=860)

        __del_meal_button = customtkinter.CTkButton(master=self._square_frame,
                                                    width=230, height=32,
                                                    corner_radius=3,
                                                    font=("arial", 15),
                                                    text_color="#ffffff",
                                                    text="Delete Meal",
                                                    fg_color="#d93030",
                                                    bg_color= "#b4b5b8",
                                                    hover_color="#f03535")
        __del_meal_button.place(x=905, y=868)

        update_meal_button = customtkinter.CTkButton(master=self._square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Update Meal",
                                                     fg_color="#f29818",
                                                     bg_color= "#b4b5b8", 
                                                     hover_color="#ffa626")
        update_meal_button.place(x=1165, y=868)

        create_meal_button = customtkinter.CTkButton(master=self._square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Add Meal",
                                                     fg_color="#37b837",
                                                     bg_color= "#b4b5b8", 
                                                     hover_color="#3bc43b")
        create_meal_button.place(x=1425, y=868)

        treeview_scrollbar = tkinter.Scrollbar(self._square_frame, 
                                               orient=tkinter.VERTICAL, 
                                               command=self.__meal_treeview.yview)
        self.__meal_treeview.configure(yscroll=treeview_scrollbar.set)
        treeview_scrollbar.place(x=1660, y=50, height=808)
