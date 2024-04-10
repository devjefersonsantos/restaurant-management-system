import customtkinter
from database.db_login import DbLogin
from utils.clear_frames import clear_frames

class UiCustomer:
    def __init__(self, root: customtkinter.CTk, square_frame: customtkinter.CTk, token: str):
        self.root = root
        self.square_frame = square_frame
        self.__token = token
        DbLogin.verify_token(self.__token)

        clear_frames(self.square_frame)
        self.ui_customer()

    def topbar(self):
        topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                              font=("arial black", 25),
                                              text_color="#ffffff", 
                                              text="Customer")
        topbar_label.place(x=20, y=5)

        searchcustomers_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                       width=1227, height=35,
                                                       placeholder_text="Search by name",
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1)
        searchcustomers_entry.place(x=174, y=8)

        searchcustomers_button = customtkinter.CTkButton(master=topbar_frame,
                                                         width=230, height=32,
                                                         corner_radius=4,
                                                         text_color="#ffffff",
                                                         font=("arial", 15), 
                                                         text="Search",
                                                         fg_color="#407ecf", 
                                                         hover_color="#6996d1")
        searchcustomers_button.place(x=1425, y=9)

    def ui_customer(self):
        self.topbar()
