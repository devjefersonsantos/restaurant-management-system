import customtkinter
from database.db_login import DbLogin
from utils.clear_frames import clear_frames
import tkinter

class UiWaiter:
    @DbLogin.verify_token
    def __init__(self, root: customtkinter.CTk, square_frame: customtkinter.CTk, token: str):
        self.root = root
        self.square_frame = square_frame
        self.__token = token

        clear_frames(self.square_frame)
        self.ui_waiter()

    def topbar(self):
        topbar_frame = customtkinter.CTkFrame(master=self.square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                              font=("arial black", 25),
                                              text_color="#ffffff", 
                                              text="Waiter")
        topbar_label.place(x=20, y=5)

        search_waiters_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                      width=1227, height=35,
                                                      placeholder_text="Search by name",
                                                      font=("arial", 17), 
                                                      fg_color="#EEEEEE", 
                                                      border_color="#e3e3e3", 
                                                      border_width=1)
        search_waiters_entry.place(x=174, y=8)

        search_waiters_button = customtkinter.CTkButton(master=topbar_frame,
                                                        width=230, height=32,
                                                        corner_radius=4,
                                                        text_color="#ffffff",
                                                        font=("arial", 15), 
                                                        text="Search",
                                                        fg_color="#407ecf", 
                                                        hover_color="#6996d1")
        search_waiters_button.place(x=1425, y=9)

    def ui_waiter(self):
        clear_frames(self.square_frame)

        self.topbar()

        create_waiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                     width=350, height=260,
                                                     corner_radius=10,
                                                     fg_color="#ffffff")
        create_waiter_frame.place(x=10, y=58)

        waiter_name_label = customtkinter.CTkLabel(master=create_waiter_frame, 
                                                   font=("arial", 17), 
                                                   text_color="#383838", 
                                                   text="Name:")
        waiter_name_label.place(x=10, y=10)

        waiter_name_entry = customtkinter.CTkEntry(master=create_waiter_frame,
                                                   width=330, height=35,
                                                   corner_radius=3, 
                                                   font=("arial", 17), 
                                                   border_color="#e3e3e3", 
                                                   border_width=1)
        waiter_name_entry.place(x=10, y=45)

        waiter_cellphone_label = customtkinter.CTkLabel(master=create_waiter_frame, 
                                                        font=("arial", 17), 
                                                        text_color="#383838", 
                                                        text="Cell Phone:")
        waiter_cellphone_label.place(x=10, y=90)

        waiter_cellphone_entry = customtkinter.CTkEntry(master=create_waiter_frame,
                                                        width=330, height=35,
                                                        corner_radius=3, 
                                                        font=("arial", 17), 
                                                        border_color="#e3e3e3", 
                                                        border_width=1)
        waiter_cellphone_entry.place(x=10, y=135)

        create_waiter_button = customtkinter.CTkButton(master=create_waiter_frame,
                                                       width=330, height=35,
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text_color="#ffffff",
                                                       text="Add Waiter",
                                                       fg_color="#4bb34b", 
                                                       hover_color="#7ebf7e")
        create_waiter_button.place(x=10, y=200)

        update_waiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                     width=350, height=100,
                                                     corner_radius=10,
                                                     fg_color="#ffffff")
        update_waiter_frame.place(x=10, y=680)

        update_waiter_label = customtkinter.CTkLabel(master=update_waiter_frame, 
                                                     font=("arial", 17), 
                                                     text_color="#383838", 
                                                     text="Update selected waiter:")
        update_waiter_label.place(x=10, y=10)

        update_waiter_button = customtkinter.CTkButton(master=update_waiter_frame,
                                                       width=330, height=35,
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text_color="#ffffff",
                                                       text="Update Waiter",
                                                       fg_color="#ec971f", 
                                                       hover_color="#f0b35d")
        update_waiter_button.place(x=10, y=45)

        delete_waiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                     width=350, height=100,
                                                     corner_radius=10,
                                                     fg_color="#ffffff")
        delete_waiter_frame.place(x=10, y=795)

        delete_waiter_label = customtkinter.CTkLabel(master=delete_waiter_frame, 
                                                     font=("arial", 17), 
                                                     text_color="#383838", 
                                                     text="Delete selected waiter:")
        delete_waiter_label.place(x=10, y=10)

        delete_waiter_button = customtkinter.CTkButton(master=delete_waiter_frame,
                                                       width=330, height=35,
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text_color="#ffffff",
                                                       text="Delete Waiter",
                                                       fg_color="#d54a49", 
                                                       hover_color="#d1706f")
        delete_waiter_button.place(x=10, y=45)

        style = tkinter.ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        waiter_treeview = tkinter.ttk.Treeview(master=self.square_frame,
                                               height=29,
                                               style="style_treeview.Treeview",
                                               columns=("ID", "name", "cell phone"),
                                               show="headings")
        waiter_treeview.place(x=370, y=58)

        waiter_treeview.heading("#1", text="  ID", anchor="w")
        waiter_treeview.heading("#2", text=" name", anchor="w")
        waiter_treeview.heading("#3", text=" cell phone", anchor="w")

        waiter_treeview.column("#1", minwidth=100, width=150, anchor="center")
        waiter_treeview.column("#2", minwidth=250, width=400, anchor="w")
        waiter_treeview.column("#3", minwidth=500, width=750, anchor="w")

        treeview_scrollbar = tkinter.Scrollbar(self.square_frame, orient=tkinter.VERTICAL, command=waiter_treeview.yview)
        waiter_treeview.configure(yscroll=treeview_scrollbar.set)
        treeview_scrollbar.place(x=1660, y=58, height=837)
