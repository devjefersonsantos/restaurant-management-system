import customtkinter
from PIL import Image
from utils.clear_frames import clear_frames
from database.db_login import DbLogin
from ui.ui_home import UiHome
from ui.ui_customer import UiCustomer
from ui.ui_waiter import UiWaiter
from ui.ui_category import UiCategory
from ui.ui_meal import UiMeal

class UiPanel:
    @DbLogin.verify_token
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
                                                    corner_radius=0,
                                                    fg_color="#ffc83d")
        self._banner_frame.grid(row=0, column=0, columnspan=2)

        self._sidebar_frame = customtkinter.CTkFrame(master=self._main_frame,
                                                     width=242, height=1012, 
                                                     corner_radius=0,
                                                     fg_color="#313338")
        self._sidebar_frame.grid(row=1, column=0, sticky="w")

        self._square_frame = customtkinter.CTkFrame(master=self._main_frame,
                                                    width=1678, height=1012,
                                                    corner_radius=0,
                                                    fg_color="#edeef0")
        self._square_frame.place(x=242, y=100)

        self._ui_images()
        self._ui_panel()

        self._current_button: customtkinter.CTkButton = self._home_button
        self._button_selected(target_button=self._home_button)
        UiHome(root=self._root, square_frame=self._square_frame, token=self.__token)

    def _ui_images(self) -> None:
        # https://pixabay.com/vectors/shop-supermarket-bakery-store-2891677/
        restaurantpil_image = Image.open("images/global_images/restaurant.png")
        self._restaurant_image = customtkinter.CTkImage(dark_image=restaurantpil_image,
                                                        light_image=restaurantpil_image, 
                                                        size=(85, 75))

    def _ui_panel(self) -> None:
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
                                                    corner_radius=0, 
                                                    fg_color="#313338",
                                                    hover_color="#21222c",
                                                    text="Home",
                                                    font=("arial", 17),
                                                    command=self._home_interface)
        self._home_button.place(x=0, y=8)

        self._customer_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                        width=242, height=37,
                                                        corner_radius=0, 
                                                        fg_color="#313338",
                                                        hover_color="#21222c",
                                                        text="Customer",
                                                        font=("arial", 17),
                                                        command=self._customer_interface)
        self._customer_button.place(x=0, y=65)

        self._waiter_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                      width=242, height=37,
                                                      corner_radius=0,
                                                      fg_color="#313338",
                                                      hover_color="#21222c",
                                                      text="Waiter",
                                                      font=("arial", 17),
                                                      command=self._waiter_interface)
        self._waiter_button.place(x=0, y=122)

        self._category_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                        width=242, height=37,
                                                        corner_radius=0, 
                                                        fg_color="#313338",
                                                        hover_color="#21222c",
                                                        text="Category",
                                                        font=("arial", 17),
                                                        command=self._category_interface)
        self._category_button.place(x=0, y=179)

        self._meal_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                    width=242, height=37,
                                                    corner_radius=0, 
                                                    fg_color="#313338",
                                                    hover_color="#21222c",
                                                    text="Meal",
                                                    font=("arial", 17),
                                                    command=self._meal_interface)
        self._meal_button.place(x=0, y=236)

        tables_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                width=242, height=37,
                                                corner_radius=0,
                                                fg_color="#313338",
                                                hover_color="#21222c",
                                                text="Tables",
                                                font=("arial", 17))
        tables_button.place(x=0, y=293)

        account_button = customtkinter.CTkButton(master=self._sidebar_frame,
                                                 width=242, height=37,
                                                 corner_radius=0,
                                                 fg_color="#313338",
                                                 hover_color="#21222c",
                                                 text="Account",
                                                 font=("arial", 17))
        account_button.place(x=0, y=858)

    def _home_interface(self) -> None:
        UiHome(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._home_button)

    def _customer_interface(self) -> None:
        UiCustomer(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._customer_button)

    def _waiter_interface(self) -> None:
        UiWaiter(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._waiter_button)

    def _category_interface(self) -> None:
        UiCategory(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._category_button)

    def _meal_interface(self) -> None:
        UiMeal(root=self._root, square_frame=self._square_frame, token=self.__token)
        self._button_selected(target_button=self._meal_button)

    def _button_selected(self, target_button:customtkinter.CTkButton) -> None:
        self._current_button.configure(fg_color="#313338")
        self._current_button = target_button
        self._current_button.configure(fg_color="#292a33")
