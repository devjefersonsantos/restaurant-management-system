import customtkinter
from PIL import Image

from utils.colors import *
from database.account_db import LoginDb
from ui import AccountUi
from ui import CategoryUi
from ui import CustomerUi
from ui import HomeUi
from ui import MealUi
from ui import WaiterUi
from utils import clear_frames

class PanelUi:
    @LoginDb.verify_token
    def __init__(self, root: customtkinter.CTk, token: str) -> None:
        self._root = root
        self.__token = token

        clear_frames(self._root)        
        self._root.geometry("1920x1012-8-2")

        self._main_frame = customtkinter.CTkFrame(master=self._root, 
                                                  width=1920, height=1012,
                                                  corner_radius=0)
        self._main_frame.grid(row=0, column=0)

        self._banner_frame = customtkinter.CTkFrame(master=self._main_frame, 
                                                    width=1920, height=100,
                                                    fg_color=ORANGE_FRAME_COLOR,
                                                    corner_radius=0)
        self._banner_frame.grid(row=0, column=0, columnspan=2)

        self._sidebar_frame = customtkinter.CTkFrame(master=self._main_frame,
                                                     width=242, height=1012, 
                                                     fg_color=SIDEBAR_COLOR,
                                                     corner_radius=0)
        self._sidebar_frame.grid(row=1, column=0, sticky="w")

        self._square_frame = customtkinter.CTkFrame(master=self._main_frame,
                                                    width=1678, height=1012,
                                                    fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                    corner_radius=0)
        self._square_frame.place(x=242, y=100)

        self._images_ui()
        self._panel_ui()

        self._current_button: customtkinter.CTkButton = self._home_button
        self._button_selected(target_button=self._home_button)
        HomeUi(root=self._root, square_frame=self._square_frame, token=self.__token)

    def _images_ui(self) -> None:
        # https://pixabay.com/vectors/shop-supermarket-bakery-store-2891677/
        restaurantpil_image = Image.open("images/global_images/restaurant.png")
        self._restaurant_image = customtkinter.CTkImage(dark_image=restaurantpil_image,
                                                        light_image=restaurantpil_image, 
                                                        size=(85, 75))

    def _panel_ui(self) -> None:
        restaurant_label = customtkinter.CTkLabel(master=self._banner_frame, 
                                                  text=None, 
                                                  image=self._restaurant_image)
        restaurant_label.place(x=80, y=12)

        restaurant_label = customtkinter.CTkLabel(master=self._banner_frame, 
                                                  text=None, 
                                                  image=self._restaurant_image)
        restaurant_label.place(x=80, y=12)

        self._home_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                    width=242, height=37,
                                                    fg_color=SIDEBAR_COLOR,
                                                    hover_color=SIDEBAR_HOVER_COLOR,
                                                    corner_radius=0, 
                                                    text="Home",
                                                    font=("arial", 17),
                                                    command=self._home_interface)
        self._home_button.place(x=0, y=8)

        self._customer_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                        width=242, height=37,
                                                        fg_color=SIDEBAR_COLOR,
                                                        hover_color=SIDEBAR_HOVER_COLOR,
                                                        corner_radius=0, 
                                                        text="Customer",
                                                        font=("arial", 17),
                                                        command=self._customer_interface)
        self._customer_button.place(x=0, y=65)

        self._waiter_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                      width=242, height=37,
                                                      fg_color=SIDEBAR_COLOR,
                                                      hover_color=SIDEBAR_HOVER_COLOR,
                                                      corner_radius=0,
                                                      text="Waiter",
                                                      font=("arial", 17),
                                                      command=self._waiter_interface)
        self._waiter_button.place(x=0, y=122)

        self._category_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                        width=242, height=37,
                                                        fg_color=SIDEBAR_COLOR,
                                                        hover_color=SIDEBAR_HOVER_COLOR,
                                                        corner_radius=0, 
                                                        text="Category",
                                                        font=("arial", 17),
                                                        command=self._category_interface)
        self._category_button.place(x=0, y=179)

        self._meal_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                    width=242, height=37,
                                                    fg_color=SIDEBAR_COLOR,
                                                    hover_color=SIDEBAR_HOVER_COLOR,
                                                    corner_radius=0, 
                                                    text="Meal",
                                                    font=("arial", 17),
                                                    command=self._meal_interface)
        self._meal_button.place(x=0, y=236)

        tables_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                width=242, height=37,
                                                fg_color=SIDEBAR_COLOR,
                                                hover_color=SIDEBAR_HOVER_COLOR,
                                                corner_radius=0,
                                                text="Tables",
                                                font=("arial", 17))
        tables_button.place(x=0, y=293)

        self._account_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                       width=242, height=37,
                                                       fg_color=SIDEBAR_COLOR,
                                                       hover_color=SIDEBAR_HOVER_COLOR,
                                                       corner_radius=0,
                                                       text="Account",
                                                       font=("arial", 17),
                                                       command=self._account_interface)
        self._account_button.place(x=0, y=858)

    def _home_interface(self) -> None:
        HomeUi(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._home_button)

    def _customer_interface(self) -> None:
        CustomerUi(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._customer_button)

    def _waiter_interface(self) -> None:
        WaiterUi(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._waiter_button)

    def _category_interface(self) -> None:
        CategoryUi(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._category_button)

    def _meal_interface(self) -> None:
        MealUi(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._meal_button)

    def _account_interface(self) -> None:
        AccountUi(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._account_button)

    def _button_selected(self, target_button:customtkinter.CTkButton) -> None:
        self._current_button.configure(fg_color=SIDEBAR_COLOR)
        self._current_button = target_button
        self._current_button.configure(fg_color=SIDEBAR_SELECTED_COLOR)
