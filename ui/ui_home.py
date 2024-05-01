from database import DbLogin
from utils import clear_frames
import customtkinter

class UiHome:
    @DbLogin.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk,
                 token: str) -> None:
        self._root = root
        self._square_frame = square_frame

        clear_frames(self._square_frame)
        self._ui_home()

    def _topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                              font=("arial black", 25),
                                              text_color="#ffffff", 
                                              text="Home")
        topbar_label.place(x=20, y=5)

    def _ui_home(self) -> None:
        self._topbar()

        frame_one = customtkinter.CTkFrame(master=self._square_frame,
                                           width=280, height=190,
                                           corner_radius=8,
                                           fg_color="#ffffff")
        frame_one.place(x=46, y=100)

        frame_two = customtkinter.CTkFrame(master=self._square_frame,
                                           width=280, height=190,
                                           corner_radius=8,
                                           fg_color="#ffffff")
        frame_two.place(x=372, y=100)

        frame_three = customtkinter.CTkFrame(master=self._square_frame,
                                             width=280, height=190,
                                             corner_radius=8,
                                             fg_color="#ffffff")
        frame_three.place(x=698, y=100)

        frame_four = customtkinter.CTkFrame(master=self._square_frame,
                                            width=280, height=190,
                                            corner_radius=8,
                                            fg_color="#ffffff")
        frame_four.place(x=1024, y=100)

        frame_five = customtkinter.CTkFrame(master=self._square_frame,
                                            width=280, height=190,
                                            corner_radius=8,
                                            fg_color="#ffffff")
        frame_five.place(x=1350, y=100)

        frame_six = customtkinter.CTkFrame(master=self._square_frame,
                                           width=280, height=190,
                                           corner_radius=8,
                                           fg_color="#ffffff")
        frame_six.place(x=46, y=345)

        frame_seven = customtkinter.CTkFrame(master=self._square_frame,
                                             width=280, height=190,
                                             corner_radius=8,
                                             fg_color="#ffffff")
        frame_seven.place(x=372, y=345)

        frame_eight = customtkinter.CTkFrame(master=self._square_frame,
                                             width=280, height=190,
                                             corner_radius=8,
                                             fg_color="#ffffff")
        frame_eight.place(x=698, y=345)

        frame_nine = customtkinter.CTkFrame(master=self._square_frame,
                                            width=280, height=190,
                                            corner_radius=8,
                                            fg_color="#ffffff")
        frame_nine.place(x=1024, y=345)

        frame_ten = customtkinter.CTkFrame(master=self._square_frame,
                                           width=280, height=190,
                                           corner_radius=8,
                                           fg_color="#ffffff")
        frame_ten.place(x=1350, y=345)

        frame_eleven = customtkinter.CTkFrame(master=self._square_frame,
                                              width=280, height=190,
                                              corner_radius=8,
                                              fg_color="#ffffff")
        frame_eleven.place(x=46, y=590)

        frame_twelve = customtkinter.CTkFrame(master=self._square_frame,
                                              width=280, height=190,
                                              corner_radius=8,
                                              fg_color="#ffffff")
        frame_twelve.place(x=372, y=590)

        frame_thirteen = customtkinter.CTkFrame(master=self._square_frame,
                                                width=280, height=190,
                                                corner_radius=8,
                                                fg_color="#ffffff")
        frame_thirteen.place(x=698, y=590)

        frame_fourteen = customtkinter.CTkFrame(master=self._square_frame,
                                                width=280, height=190,
                                                corner_radius=8,
                                                fg_color="#ffffff")
        frame_fourteen.place(x=1024, y=590)

        frame_fifteen = customtkinter.CTkFrame(master=self._square_frame,
                                               width=280, height=190,
                                               corner_radius=8,
                                               fg_color="#ffffff")
        frame_fifteen.place(x=1350, y=590)
