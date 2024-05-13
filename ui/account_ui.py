import tkinter

from PIL import Image
import customtkinter

from database import AccountDb
from database.account_db import LoginDb
from utils.colors import *
from utils import clear_frames
from utils import restart_software

class AccountUi:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self._root = root
        self._square_frame = square_frame
        self.__token = token

        clear_frames(self._square_frame)
        
        self._images_ui()
        self._account_ui()

    def _topbar(self) -> None:
        self.topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                   width=1678, height=50,
                                                   corner_radius=0)
        self.topbar_frame.place(x=0, y=0)
        
        _topbar_label = customtkinter.CTkLabel(master=self.topbar_frame, 
                                               font=("arial black", 25),
                                               text_color=WHITE_COLOR, 
                                               text="Account")
        _topbar_label.place(x=20, y=5)

    def _images_ui(self) -> None:
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        userpil_image = Image.open("images/account_images/user.png")
        self._user_image = customtkinter.CTkImage(dark_image=userpil_image,
                                                  light_image=userpil_image,
                                                  size=(52,52))
        
        creationdatepil_image = Image.open("images/account_images/creationdate.png")
        self.creationdate_image = customtkinter.CTkImage(dark_image=creationdatepil_image,
                                                         light_image=creationdatepil_image,
                                                         size=(52,52))
        
        lastloginpil_image = Image.open("images/account_images/lastlogin.png")
        self.lastlogin_image = customtkinter.CTkImage(dark_image=lastloginpil_image,
                                                      light_image=lastloginpil_image,
                                                      size=(52,52))

    def _account_ui(self) -> None:
        clear_frames(self._square_frame)

        self._topbar()

        square_status_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                     width=1658,
                                                     height=120,
                                                     fg_color="#ffffff")
        square_status_frame.place(x=10, y=60)

        log_out_button = customtkinter.CTkButton(master=self.topbar_frame,
                                                 width=230, height=32,
                                                 corner_radius=4,
                                                 text_color="#ffffff",
                                                 font=("arial", 15), 
                                                 text="Log out",
                                                 fg_color="#407ecf", 
                                                 hover_color="#6996d1",
                                                 command=restart_software)
        log_out_button.place(x=1425, y=9)

        
        ################################################### user information ##########################################################
        
        userimage_label = customtkinter.CTkLabel(master=square_status_frame,text="", image=self._user_image)
        userimage_label.place(x=50, y=32)
        user_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color="#383838", text="Username:")
        user_label.place(x=110, y=28)
        username_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color="#383838", text=AccountDb(self.__token).get_username())
        username_label.place(x=120, y=50)


        divider_frame = tkinter.Frame(master=square_status_frame, height=80, width=1)
        divider_frame.place(x=552, y=20)


        creationdateimage_label = customtkinter.CTkLabel(master=square_status_frame,text="", image=self.creationdate_image)
        creationdateimage_label.place(x=609, y=32)
        date_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color="#383838", text="Creation date:")
        date_label.place(x=669, y=28)
        creationdate_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color="#383838", text=AccountDb(self.__token).get_creation_date())
        creationdate_label.place(x=679, y=50)


        divider_frame2 = tkinter.Frame(master=square_status_frame, height=80, width=1)
        divider_frame2.place(x=1104, y=20)


        lastloginimage_label = customtkinter.CTkLabel(master=square_status_frame,text="", image=self.lastlogin_image)
        lastloginimage_label.place(x=1158, y=32)
        last_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color="#383838", text="Last login:")
        last_label.place(x=1218, y=28)
        lastlogin_label = customtkinter.CTkLabel(master=square_status_frame, font=("arial", 17), text_color="#383838", text=AccountDb(self.__token).get_last_login_date())
        lastlogin_label.place(x=1228, y=50)

        ###############################################################################################################################
