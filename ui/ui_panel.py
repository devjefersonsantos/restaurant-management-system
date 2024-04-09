import customtkinter
from utils.clear_frames import clear_frames
from database.db_login import DbLogin
from ui.ui_home import UiHome
from ui.ui_customer import UiCustomer
from PIL import Image

class UiPanel:
    def __init__(self, root: customtkinter.CTk, token: str):
        self.root = root
        self.__token = token
        DbLogin.verify_token(self.__token)

        clear_frames(self.root)        
        self.root.geometry("1920x1012-8-2")

        self.main_frame = customtkinter.CTkFrame(master=self.root, 
                                                 width=1920, height=1012,
                                                 corner_radius=0)
        self.main_frame.grid(row=0, column=0)

        self.banner_frame = customtkinter.CTkFrame(master=self.main_frame, 
                                                   width=1920, height=100,
                                                   corner_radius=0,
                                                   fg_color="#ffc83d")
        self.banner_frame.grid(row=0, column=0, columnspan=2)

        self.sidebar_frame = customtkinter.CTkFrame(master=self.main_frame,
                                                    width=242, height=1012, 
                                                    corner_radius=0,
                                                    fg_color="#313338")
        self.sidebar_frame.grid(row=1, column=0, sticky="w")

        self.square_frame = customtkinter.CTkFrame(master=self.main_frame,
                                                   width=1678, height=1012,
                                                   corner_radius=0,
                                                   fg_color="#edeef0")
        self.square_frame.place(x=242, y=100)

        self.ui_images()
        self.ui_panel()

        self.current_button: customtkinter.CTkButton = self.home_button
        self.button_selected(target_button=self.home_button)
        UiHome(root=self.root, square_frame=self.square_frame, token=self.__token)

    def ui_images(self):
        # https://pixabay.com/vectors/shop-supermarket-bakery-store-2891677/
        restaurantpil_image = Image.open("images/global_images/restaurant.png")
        self.restaurant_image = customtkinter.CTkImage(dark_image=restaurantpil_image,
                                                       light_image=restaurantpil_image, 
                                                       size=(85, 75))

    def ui_panel(self):
        restaurant_label = customtkinter.CTkLabel(master=self.banner_frame, 
                                                  text=None, 
                                                  image=self.restaurant_image)
        restaurant_label.place(x=80, y=12)

        restaurant_label = customtkinter.CTkLabel(master=self.banner_frame, 
                                                  text=None, 
                                                  image=self.restaurant_image)
        restaurant_label.place(x=80, y=12)

        self.home_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                   width=242, height=37,
                                                   corner_radius=0, 
                                                   fg_color="#313338",
                                                   hover_color="#21222c",
                                                   text="Home",
                                                   font=("arial", 17),
                                                   command=self.home_interface)
        self.home_button.place(x=0, y=8)

        self.customer_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                       width=242, height=37,
                                                       corner_radius=0, 
                                                       fg_color="#313338",
                                                       hover_color="#21222c",
                                                       text="Customer",
                                                       font=("arial", 17),
                                                       command=self.customer_interface)
        self.customer_button.place(x=0, y=65)

        waiter_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                width=242, height=37,
                                                corner_radius=0,
                                                fg_color="#313338",
                                                hover_color="#21222c",
                                                text="Waiter",
                                                font=("arial", 17))
        waiter_button.place(x=0, y=122)

        category_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                  width=242, height=37,
                                                  corner_radius=0, 
                                                  fg_color="#313338",
                                                  hover_color="#21222c",
                                                  text="Category",
                                                  font=("arial", 17))
        category_button.place(x=0, y=179)

        meal_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                              width=242, height=37,
                                              corner_radius=0, 
                                              fg_color="#313338",
                                              hover_color="#21222c",
                                              text="Meal",
                                              font=("arial", 17))
        meal_button.place(x=0, y=236)

        tables_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                width=242, height=37,
                                                corner_radius=0,
                                                fg_color="#313338",
                                                hover_color="#21222c",
                                                text="Tables",
                                                font=("arial", 17))
        tables_button.place(x=0, y=293)

        account_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                 width=242, height=37,
                                                 corner_radius=0,
                                                 fg_color="#313338",
                                                 hover_color="#21222c",
                                                 text="Account",
                                                 font=("arial", 17))
        account_button.place(x=0, y=858)

    def home_interface(self):
        UiHome(root=self.root, square_frame=self.square_frame, token=self.__token)
        self.button_selected(target_button=self.home_button)

    def customer_interface(self):
        UiCustomer(root=self.root, square_frame=self.square_frame, token=self.__token)
        self.button_selected(target_button=self.customer_button)

    def button_selected(self, target_button:customtkinter.CTkButton):
        self.current_button.configure(fg_color="#313338")
        self.current_button = target_button
        self.current_button.configure(fg_color="#292a33")
