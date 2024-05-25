import customtkinter

from utils.colors import *
from database.account_db import LoginDb
from utils import clear_frames

class HomeUI:
    @LoginDb.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk,
                 token: str) -> None:
        self.__root = root
        self.__square_frame = square_frame

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

    def __home_ui(self) -> None:
        self.__topbar()

        frame_one = customtkinter.CTkFrame(master=self.__square_frame,
                                           width=280, height=190,
                                           fg_color=WHITE_COLOR,
                                           corner_radius=8)
        frame_one.place(x=46, y=100)

        frame_two = customtkinter.CTkFrame(master=self.__square_frame,
                                           width=280, height=190,
                                           fg_color=WHITE_COLOR,
                                           corner_radius=8)
        frame_two.place(x=372, y=100)

        frame_three = customtkinter.CTkFrame(master=self.__square_frame,
                                             width=280, height=190,
                                             fg_color=WHITE_COLOR,
                                             corner_radius=8)
        frame_three.place(x=698, y=100)

        frame_four = customtkinter.CTkFrame(master=self.__square_frame,
                                            width=280, height=190,
                                            fg_color=WHITE_COLOR,
                                            corner_radius=8)
        frame_four.place(x=1024, y=100)

        frame_five = customtkinter.CTkFrame(master=self.__square_frame,
                                            width=280, height=190,
                                            fg_color=WHITE_COLOR,
                                            corner_radius=8)
        frame_five.place(x=1350, y=100)

        frame_six = customtkinter.CTkFrame(master=self.__square_frame,
                                           width=280, height=190,
                                           fg_color=WHITE_COLOR,
                                           corner_radius=8)
        frame_six.place(x=46, y=345)

        frame_seven = customtkinter.CTkFrame(master=self.__square_frame,
                                             width=280, height=190,
                                             fg_color=WHITE_COLOR,
                                             corner_radius=8)
        frame_seven.place(x=372, y=345)

        frame_eight = customtkinter.CTkFrame(master=self.__square_frame,
                                             width=280, height=190,
                                             fg_color=WHITE_COLOR,
                                             corner_radius=8)
        frame_eight.place(x=698, y=345)

        frame_nine = customtkinter.CTkFrame(master=self.__square_frame,
                                            width=280, height=190,
                                            fg_color=WHITE_COLOR,
                                            corner_radius=8)
        frame_nine.place(x=1024, y=345)

        frame_ten = customtkinter.CTkFrame(master=self.__square_frame,
                                           width=280, height=190,
                                           fg_color=WHITE_COLOR,
                                           corner_radius=8)
        frame_ten.place(x=1350, y=345)

        frame_eleven = customtkinter.CTkFrame(master=self.__square_frame,
                                              width=280, height=190,
                                              fg_color=WHITE_COLOR,
                                              corner_radius=8)
        frame_eleven.place(x=46, y=590)

        frame_twelve = customtkinter.CTkFrame(master=self.__square_frame,
                                              width=280, height=190,
                                              fg_color=WHITE_COLOR,
                                              corner_radius=8)
        frame_twelve.place(x=372, y=590)

        frame_thirteen = customtkinter.CTkFrame(master=self.__square_frame,
                                                width=280, height=190,
                                                fg_color=WHITE_COLOR,
                                                corner_radius=8)
        frame_thirteen.place(x=698, y=590)

        frame_fourteen = customtkinter.CTkFrame(master=self.__square_frame,
                                                width=280, height=190,
                                                fg_color=WHITE_COLOR,
                                                corner_radius=8)
        frame_fourteen.place(x=1024, y=590)

        frame_fifteen = customtkinter.CTkFrame(master=self.__square_frame,
                                               width=280, height=190,
                                               fg_color=WHITE_COLOR,
                                               corner_radius=8)
        frame_fifteen.place(x=1350, y=590)
