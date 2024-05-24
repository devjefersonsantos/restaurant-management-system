import tkinter

from PIL import Image
import customtkinter

from database import AccountDb
from database.account_db import LoginDb
from utils.colors import *
from utils import clear_frames
from utils import restart_software

class AccountUI:
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
        self.__account_ui()

    def __topbar(self) -> None:
        self.__topbar_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                     width=1678, height=50,
                                                     corner_radius=0)
        self.__topbar_frame.place(x=0, y=0)
        
        topbar_label = customtkinter.CTkLabel(master=self.__topbar_frame, 
                                              font=("arial black", 25),
                                              text_color=WHITE_COLOR, 
                                              text="Account")
        topbar_label.place(x=20, y=5)

    def __images_ui(self) -> None:
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        userpil_image = Image.open("./images/account_images/user.png")
        self.__user_image = customtkinter.CTkImage(dark_image=userpil_image,
                                                   light_image=userpil_image,
                                                   size=(52,52))
        
        creationdatepil_image = Image.open("./images/account_images/creationdate.png")
        self.__creationdate_image = customtkinter.CTkImage(dark_image=creationdatepil_image,
                                                           light_image=creationdatepil_image,
                                                           size=(52,52))
        
        lastloginpil_image = Image.open("./images/account_images/lastlogin.png")
        self.__lastlogin_image = customtkinter.CTkImage(dark_image=lastloginpil_image,
                                                        light_image=lastloginpil_image,
                                                        size=(52,52))
        
    def __account_ui(self) -> None:
        self.__topbar()

        square_status_frame = customtkinter.CTkFrame(master=self.__square_frame,
                                                     width=1658,
                                                     fg_color=WHITE_COLOR,
                                                     height=120)
        square_status_frame.place(x=10, y=60)

        log_out_button = customtkinter.CTkButton(master=self.__topbar_frame,
                                                 width=230, height=32,
                                                 text_color=WHITE_COLOR,
                                                 fg_color=LIGHT_BLUE_COLOR, 
                                                 hover_color=LIGHT_BLUE_HOVER_COLOR,
                                                 corner_radius=4,
                                                 font=("arial", 15), 
                                                 text="Log out",
                                                 command=restart_software)
        log_out_button.place(x=1425, y=9)

        
        ################################################### user information ##########################################################
        
        userimage_label = customtkinter.CTkLabel(master=square_status_frame,text="", image=self.__user_image)
        userimage_label.place(x=50, y=32)
        user_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color=GRAY_TEXT_COLOR, text="Username:")
        user_label.place(x=110, y=28)
        username_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color=GRAY_TEXT_COLOR, text=AccountDb(self.__token).get_username())
        username_label.place(x=120, y=50)


        divider_frame = tkinter.Frame(master=square_status_frame, height=80, width=1)
        divider_frame.place(x=552, y=20)


        creationdateimage_label = customtkinter.CTkLabel(master=square_status_frame,text="", image=self.__creationdate_image)
        creationdateimage_label.place(x=609, y=32)
        date_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color=GRAY_TEXT_COLOR, text="Creation date:")
        date_label.place(x=669, y=28)
        creationdate_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color=GRAY_TEXT_COLOR, text=AccountDb(self.__token).get_creation_date())
        creationdate_label.place(x=679, y=50)


        divider_frame2 = tkinter.Frame(master=square_status_frame, height=80, width=1)
        divider_frame2.place(x=1104, y=20)


        lastloginimage_label = customtkinter.CTkLabel(master=square_status_frame,text="", image=self.__lastlogin_image)
        lastloginimage_label.place(x=1158, y=32)
        last_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color=GRAY_TEXT_COLOR, text="Last login:")
        last_label.place(x=1218, y=28)
        lastlogin_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color=GRAY_TEXT_COLOR, text=AccountDb(self.__token).get_last_login_date())
        lastlogin_label.place(x=1228, y=50)

        ###############################################################################################################################
