import customtkinter
from PIL import Image

from ui import *
from utils.colors import *
from database.account_db import LoginDb
from utils import clear_frames

class SidebarUI:
    @LoginDb.verify_token
    def __init__(self, root: customtkinter.CTk, token: str) -> None:
        self.__root = root
        self.__token = token

        clear_frames(self.__root)        
        self.__root.geometry("1920x1012-8-2")

        self.__main_frame = customtkinter.CTkFrame(master=self.__root, 
                                                   width=1920, height=1012,
                                                   corner_radius=0)
        self.__main_frame.grid(row=0, column=0)

        self.__banner_frame = customtkinter.CTkFrame(master=self.__main_frame, 
                                                     width=1920, height=100,
                                                     fg_color=ORANGE_FRAME_COLOR,
                                                     corner_radius=0)
        self.__banner_frame.grid(row=0, column=0, columnspan=2)

        self.__sidebar_frame = customtkinter.CTkFrame(master=self.__main_frame,
                                                      width=242, height=1012, 
                                                      fg_color=SIDEBAR_COLOR,
                                                      corner_radius=0)
        self.__sidebar_frame.grid(row=1, column=0, sticky="w")

        self.__square_frame = customtkinter.CTkFrame(master=self.__main_frame,
                                                     width=1678, height=1012,
                                                     fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                     corner_radius=0)
        self.__square_frame.place(x=242, y=100)

        self.__images_ui()
        self.__panel_ui()

        self.__current_button: customtkinter.CTkButton = self.__home_button
        self.__button_selected(target_button=self.__home_button)
        HomeUI(root=self.__root, square_frame=self.__square_frame, token=self.__token)

    def __images_ui(self) -> None:
        # https://pixabay.com/vectors/shop-supermarket-bakery-store-2891677/
        restaurantpil_image = Image.open("./images/global_images/restaurant.png")
        self.__restaurant_image = customtkinter.CTkImage(dark_image=restaurantpil_image,
                                                         light_image=restaurantpil_image, 
                                                         size=(85, 75))

    def __panel_ui(self) -> None:
        restaurant_label = customtkinter.CTkLabel(master=self.__banner_frame, 
                                                  text=None, 
                                                  image=self.__restaurant_image)
        restaurant_label.place(x=80, y=12)

        restaurant_label = customtkinter.CTkLabel(master=self.__banner_frame, 
                                                  text=None, 
                                                  image=self.__restaurant_image)
        restaurant_label.place(x=80, y=12)

        self.__home_button = customtkinter.CTkButton(master=self.__sidebar_frame,
                                                     width=242, height=37,
                                                     fg_color=SIDEBAR_COLOR,
                                                     hover_color=SIDEBAR_HOVER_COLOR,
                                                     corner_radius=0, 
                                                     text="Home",
                                                     font=("arial", 17),
                                                     command=self.__home_interface)
        self.__home_button.place(x=0, y=8)

        self.__customer_button = customtkinter.CTkButton(master=self.__sidebar_frame,
                                                         width=242, height=37,
                                                         fg_color=SIDEBAR_COLOR,
                                                         hover_color=SIDEBAR_HOVER_COLOR,
                                                         corner_radius=0, 
                                                         text="Customer",
                                                         font=("arial", 17),
                                                         command=self.__customer_interface)
        self.__customer_button.place(x=0, y=65)

        self.__waiter_button = customtkinter.CTkButton(master=self.__sidebar_frame,
                                                       width=242, height=37,
                                                       fg_color=SIDEBAR_COLOR,
                                                       hover_color=SIDEBAR_HOVER_COLOR,
                                                       corner_radius=0,
                                                       text="Waiter",
                                                       font=("arial", 17),
                                                       command=self.__waiter_interface)
        self.__waiter_button.place(x=0, y=122)

        self.__category_button = customtkinter.CTkButton(master=self.__sidebar_frame,
                                                         width=242, height=37,
                                                         fg_color=SIDEBAR_COLOR,
                                                         hover_color=SIDEBAR_HOVER_COLOR,
                                                         corner_radius=0, 
                                                         text="Category",
                                                         font=("arial", 17),
                                                         command=self.__category_interface)
        self.__category_button.place(x=0, y=179)

        self.__meal_button = customtkinter.CTkButton(master=self.__sidebar_frame,
                                                     width=242, height=37,
                                                     fg_color=SIDEBAR_COLOR,
                                                     hover_color=SIDEBAR_HOVER_COLOR,
                                                     corner_radius=0, 
                                                     text="Meal",
                                                     font=("arial", 17),
                                                     command=self.__meal_interface)
        self.__meal_button.place(x=0, y=236)

        self.__table_button = customtkinter.CTkButton(master=self.__sidebar_frame,
                                                      width=242, height=37,
                                                      fg_color=SIDEBAR_COLOR,
                                                      hover_color=SIDEBAR_HOVER_COLOR,
                                                      corner_radius=0,
                                                      text="Table",
                                                      font=("arial", 17),
                                                      command=self.__table_interface)
        self.__table_button.place(x=0, y=293)

        self.__account_button = customtkinter.CTkButton(master=self.__sidebar_frame,
                                                        width=242, height=37,
                                                        fg_color=SIDEBAR_COLOR,
                                                        hover_color=SIDEBAR_HOVER_COLOR,
                                                        corner_radius=0,
                                                        text="Account",
                                                        font=("arial", 17),
                                                        command=self.__account_interface)
        self.__account_button.place(x=0, y=858)

    def __home_interface(self) -> None:
        HomeUI(root=self.__root, square_frame=self.__square_frame, token=self.__token)
        self.__button_selected(target_button=self.__home_button)

    def __customer_interface(self) -> None:
        CustomerUI(root=self.__root, square_frame=self.__square_frame, token=self.__token)
        self.__button_selected(target_button=self.__customer_button)

    def __waiter_interface(self) -> None:
        WaiterUI(root=self.__root, square_frame=self.__square_frame, token=self.__token)
        self.__button_selected(target_button=self.__waiter_button)

    def __category_interface(self) -> None:
        CategoryUi(root=self.__root, square_frame=self.__square_frame, token=self.__token)
        self.__button_selected(target_button=self.__category_button)

    def __meal_interface(self) -> None:
        MealUI(root=self.__root, square_frame=self.__square_frame, token=self.__token)
        self.__button_selected(target_button=self.__meal_button)

    def __account_interface(self) -> None:
        AccountUI(root=self.__root, square_frame=self.__square_frame, token=self.__token)
        self.__button_selected(target_button=self.__account_button)

    def __table_interface(self) -> None:
        TableUI(root=self.__root, square_frame=self.__square_frame, token=self.__token)
        self.__button_selected(target_button=self.__table_button)

    def __button_selected(self, target_button:customtkinter.CTkButton) -> None:
        self.__current_button.configure(fg_color=SIDEBAR_COLOR)
        self.__current_button = target_button
        self.__current_button.configure(fg_color=SIDEBAR_SELECTED_COLOR)
