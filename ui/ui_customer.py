import customtkinter
from utils.clear_frames import clear_frames
from database.db_login import DbLogin
import tkinter

class UiCustomer:
    @DbLogin.verify_token
    def __init__(self, root: customtkinter.CTk, square_frame: customtkinter.CTk, token: str):
        self.root = root
        self.square_frame = square_frame
        self.__token = token

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

        # https://stackoverflow.com/questions/75492266/changing-font-style-of-rows-in-treeview
        style = tkinter.ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        customer_treeview = tkinter.ttk.Treeview(master=self.square_frame,
                                                 height=28,
                                                 style="style_treeview.Treeview",
                                                 columns=("id customer", "name", "address", 
                                                          "cell phone", "email", "registration date"),
                                                 show="headings")
        customer_treeview.place(x=0, y=50)

        customer_treeview.heading("#1", text="id customer", anchor="center")
        customer_treeview.heading("#2", text="name", anchor="center")
        customer_treeview.heading("#3", text="address", anchor="center")
        customer_treeview.heading("#4", text="cell phone", anchor="center")
        customer_treeview.heading("#5", text="email", anchor="center")
        customer_treeview.heading("#6", text="registration date", anchor="center")

        customer_treeview.column("#1", minwidth=150, width=200, anchor="center")
        customer_treeview.column("#2", minwidth=150, width=300, anchor="center")
        customer_treeview.column("#3", minwidth=150, width=300, anchor="center")
        customer_treeview.column("#4", minwidth=150, width=300, anchor="center")
        customer_treeview.column("#5", minwidth=150, width=300, anchor="center")
        customer_treeview.column("#6", minwidth=262, width=262, anchor="center")

        delcustomer_button = customtkinter.CTkButton(master=self.square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Delete Customer",
                                                     fg_color="#d54a49", 
                                                     hover_color="#d1706f")
        delcustomer_button.place(x=905, y=868)

        updatecustomer_button = customtkinter.CTkButton(master=self.square_frame,
                                                        width=230, height=32,
                                                        corner_radius=3,
                                                        font=("arial", 15),
                                                        text_color="#ffffff",
                                                        text="Update Customer",
                                                        fg_color="#ec971f", 
                                                        hover_color="#f0b35d")
        updatecustomer_button.place(x=1165, y=868)

        addcustomer_button = customtkinter.CTkButton(master=self.square_frame,
                                                     width=230, height=32,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Add Customer",
                                                     fg_color="#4bb34b", 
                                                     hover_color="#7ebf7e")
        addcustomer_button.place(x=1425, y=868)

        treeview_scrollbar = tkinter.Scrollbar(self.square_frame, orient=tkinter.VERTICAL)
        treeview_scrollbar.place(x=1660, y=50, height=808)
