import tkinter

import customtkinter

from utils.colors import *
from database.account_db import LoginDb
from database import CustomerDb
from database import WaiterDb
from database import CategoryDb
from database import MealDb
from database import TableDb
from database import OrderDb
from utils import clear_frames

class HomeUI:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk,
                 token: str) -> None:
        self.__root = root
        self.__square_frame = square_frame
        self.__token = token

        self.__root.unbind("<Return>")
        clear_frames(self.__square_frame)
        self.__home_ui()
        

    def __topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                              font=("arial black", 25),
                                              text_color=WHITE_COLOR, 
                                              text="Home")
        topbar_label.place(x=20, y=5)

    def __info_widgets(self) -> None:
        total_customers_frame = customtkinter.CTkFrame(master=self.__home_screen_frame,
                                                       width=235, height=140,
                                                       corner_radius=8,
                                                       fg_color=GREEN_COLOR)
        total_customers_frame.grid(row=0, column=0, padx=38, pady=30)
        customers_label = customtkinter.CTkLabel(master=total_customers_frame,
                                                 text_color=WHITE_COLOR, 
                                                 font=("Arial", 21, "italic"),
                                                 text="Total Customers")
        customers_label.place(x=30, y=12)
        total_customers_label = customtkinter.CTkLabel(master=total_customers_frame,
                                                       text_color=WHITE_COLOR,
                                                       font=("arial black", 25),
                                                       text=f"{CustomerDb(self.__token).count_customers():^18}")
        total_customers_label.place(x=30, y=64)


        total_waiters_frame = customtkinter.CTkFrame(master=self.__home_screen_frame,
                                                     width=235, height=140,
                                                     fg_color=PURPLE_COLOR,
                                                     corner_radius=8)
        total_waiters_frame.grid(row=0, column=1, padx=0, pady=0)
        waiters_label = customtkinter.CTkLabel(master=total_waiters_frame,
                                               text_color=WHITE_COLOR,
                                               font=("Arial", 21, "italic"),
                                               text="Total Waiters")
        waiters_label.place(x=30, y=12)
        total_waiters_label = customtkinter.CTkLabel(master=total_waiters_frame,
                                                     text_color=WHITE_COLOR,
                                                     font=("arial black", 25),
                                                     text=f"{WaiterDb(self.__token).count_waiters():^18}")
        total_waiters_label.place(x=30, y=64)


        total_categories_frame = customtkinter.CTkFrame(master=self.__home_screen_frame,
                                                        width=235, height=140,
                                                        fg_color=LIGHT_BLUE_COLOR,
                                                        corner_radius=8)
        total_categories_frame.grid(row=0, column=2, padx=38, pady=30)
        categories_label = customtkinter.CTkLabel(master=total_categories_frame,
                                                  text_color=WHITE_COLOR, 
                                                  font=("Arial", 21, "italic"),
                                                  text="Total Categories")
        categories_label.place(x=30, y=12)
        total_categories_label = customtkinter.CTkLabel(master=total_categories_frame,
                                                        text_color=WHITE_COLOR,
                                                        font=("arial black", 25),
                                                        text=f"{CategoryDb(self.__token).count_categories():^18}")
        total_categories_label.place(x=30, y=64)


        total_meals_frame = customtkinter.CTkFrame(master=self.__home_screen_frame,
                                                   width=235, height=140,
                                                   corner_radius=8,
                                                   fg_color=ORANGE_COLOR)
        total_meals_frame.grid(row=0, column=3, padx=0, pady=0)
        meals_label = customtkinter.CTkLabel(master=total_meals_frame,
                                             text_color=WHITE_COLOR, 
                                             font=("Arial", 21, "italic"),
                                             text="Total Meals")
        meals_label.place(x=30, y=12)
        total_meals_label = customtkinter.CTkLabel(master=total_meals_frame,
                                                   text_color=WHITE_COLOR,
                                                   font=("arial black", 25),
                                                   text=f"{MealDb(self.__token).count_meals():^18}")
        total_meals_label.place(x=30, y=64)


        total_tables_frame = customtkinter.CTkFrame(master=self.__home_screen_frame,
                                                    width=235, height=140,
                                                    corner_radius=8,
                                                    fg_color=GREEN_COLOR)
        total_tables_frame.grid(row=0, column=4, padx=38, pady=30)
        tables_label = customtkinter.CTkLabel(master=total_tables_frame,
                                              text_color=WHITE_COLOR, 
                                              font=("Arial", 21, "italic"),
                                              text="Total Tables")
        tables_label.place(x=30, y=12)
        total_tables_label = customtkinter.CTkLabel(master=total_tables_frame,
                                                    text_color=WHITE_COLOR,
                                                    font=("arial black", 25),
                                                    text=f"{TableDb(self.__token).count_tables():^18}")
        total_tables_label.place(x=30, y=64)


        total_occupied_tables_frame = customtkinter.CTkFrame(master=self.__home_screen_frame,
                                                             width=235, height=140,
                                                             corner_radius=8,
                                                             fg_color=RED_COLOR)
        total_occupied_tables_frame.grid(row=0, column=5, padx=0, pady=30)
        occupied_tables_label = customtkinter.CTkLabel(master=total_occupied_tables_frame,
                                                       text_color=WHITE_COLOR, 
                                                       font=("Arial", 21, "italic"),
                                                       text="Occupied Tables")
        occupied_tables_label.place(x=30, y=12)
        total_occupied_tables_label = customtkinter.CTkLabel(master=total_occupied_tables_frame,
                                                             text_color=WHITE_COLOR,
                                                             font=("arial black", 25),
                                                             text=f"{TableDb(self.__token).count_occupied_tables():^19}")
        total_occupied_tables_label.place(x=30, y=64)

    def __home_ui(self) -> None:
        self.__topbar()

        self.__home_screen_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                          fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                          corner_radius=0)
        self.__home_screen_frame.place(x=0, y=50)

        self.__info_widgets()
        
        bar_chart_canvas = tkinter.Canvas(master=self.__home_screen_frame, 
                                          width=990, height=600,
                                          bg=WHITE_COLOR)
        bar_chart_canvas.grid(row=1, column=0, columnspan=4, pady=15)

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        sales = OrderDb(self.__token).get_monthly_sales()
        max_sales = max(sales)

        for i, sale in enumerate(sales):
            bar_height = (sale / max_sales) * (550 - 50)
            x0 = 30 + i * (50 + 30)
            y0 = 550 - bar_height
            x1 = x0 + 50
            y1 = 550
            
            bar_chart_canvas.create_rectangle(x0, y0, x1, y1, fill=LIGHT_BLUE_HOVER_COLOR)
            bar_chart_canvas.create_text((x0 + x1) / 2, 550 + 10, text=months[i], anchor="n")
            bar_chart_canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(sale), anchor="s")
