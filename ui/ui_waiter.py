import customtkinter
from database.db_login import DbLogin
from utils.clear_frames import clear_frames
import tkinter
from database.db_waiter import DbWaiter

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
        
        self.topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                                   font=("arial black", 25),
                                                   text_color="#ffffff", 
                                                   text="Waiter")
        self.topbar_label.place(x=20, y=5)

        self.search_waiters_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                           width=1227, height=35,
                                                           placeholder_text="Search by name",
                                                           font=("arial", 17), 
                                                           fg_color="#EEEEEE", 
                                                           border_color="#e3e3e3", 
                                                           border_width=1)
        self.search_waiters_entry.place(x=174, y=8)

        self.search_waiters_button = customtkinter.CTkButton(master=topbar_frame,
                                                             width=230, height=32,
                                                             corner_radius=4,
                                                             text_color="#ffffff",
                                                             font=("arial", 15), 
                                                             text="Search",
                                                             fg_color="#407ecf", 
                                                             hover_color="#6996d1")
        self.search_waiters_button.place(x=1425, y=9)

    def ui_waiter(self):
        clear_frames(self.square_frame)

        self.topbar()

        self.create_waiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                          width=350, height=240,
                                                          corner_radius=10,
                                                          fg_color="#ffffff")
        self.create_waiter_frame.place(x=10, y=58)

        waiter_name_label = customtkinter.CTkLabel(master=self.create_waiter_frame, 
                                                   font=("arial", 17), 
                                                   text_color="#383838", 
                                                   text="Name:")
        waiter_name_label.place(x=10, y=10)

        self.waiter_name_entry = customtkinter.CTkEntry(master=self.create_waiter_frame,
                                                        width=330, height=35,
                                                        corner_radius=3, 
                                                        font=("arial", 17), 
                                                        border_color="#e3e3e3", 
                                                        border_width=1)
        self.waiter_name_entry.place(x=10, y=45)

        waiter_cellphone_label = customtkinter.CTkLabel(master=self.create_waiter_frame, 
                                                        font=("arial", 17), 
                                                        text_color="#383838", 
                                                        text="Cell Phone:")
        waiter_cellphone_label.place(x=10, y=90)

        self.waiter_cellphone_entry = customtkinter.CTkEntry(master=self.create_waiter_frame,
                                                             width=330, height=35,
                                                             corner_radius=3, 
                                                             font=("arial", 17), 
                                                             border_color="#e3e3e3", 
                                                             border_width=1)
        self.waiter_cellphone_entry.place(x=10, y=125)

        self.create_waiter_button = customtkinter.CTkButton(master=self.create_waiter_frame,
                                                            width=330, height=35,
                                                            corner_radius=3,
                                                            font=("arial", 15),
                                                            text_color="#ffffff",
                                                            text="Add Waiter",
                                                            fg_color="#4bb34b", 
                                                            hover_color="#7ebf7e",
                                                            command=self.fn_create_waiter)
        self.create_waiter_button.place(x=10, y=185)

        self.update_waiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                          width=350, height=100,
                                                          corner_radius=10,
                                                          fg_color="#ffffff")
        self.update_waiter_frame.place(x=10, y=680)

        update_waiter_label = customtkinter.CTkLabel(master=self.update_waiter_frame, 
                                                     font=("arial", 17), 
                                                     text_color="#383838", 
                                                     text="Update selected waiter:")
        update_waiter_label.place(x=10, y=10)

        update_waiter_button = customtkinter.CTkButton(master=self.update_waiter_frame,
                                                       width=330, height=35,
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text_color="#ffffff",
                                                       text="Update Waiter",
                                                       fg_color="#ec971f", 
                                                       hover_color="#f0b35d",
                                                       command=self.ui_update_waiter)
        update_waiter_button.place(x=10, y=45)

        self.delete_waiter_frame = customtkinter.CTkFrame(master=self.square_frame,
                                                          width=350, height=100,
                                                          corner_radius=10,
                                                          fg_color="#ffffff")
        self.delete_waiter_frame.place(x=10, y=795)

        delete_waiter_label = customtkinter.CTkLabel(master=self.delete_waiter_frame, 
                                                     font=("arial", 17), 
                                                     text_color="#383838", 
                                                     text="Delete selected waiter:")
        delete_waiter_label.place(x=10, y=10)

        delete_waiter_button = customtkinter.CTkButton(master=self.delete_waiter_frame,
                                                       width=330, height=35,
                                                       corner_radius=3,
                                                       font=("arial", 15),
                                                       text_color="#ffffff",
                                                       text="Delete Waiter",
                                                       fg_color="#d54a49", 
                                                       hover_color="#d1706f",
                                                       command=self.fn_delete_waiter)
        delete_waiter_button.place(x=10, y=45)

        style = tkinter.ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.waiter_treeview = tkinter.ttk.Treeview(master=self.square_frame,
                                                    height=29,
                                                    style="style_treeview.Treeview",
                                                    columns=("ID", "name", "cell phone", "registration date"),
                                                    show="headings")
        self.waiter_treeview.place(x=370, y=58)

        self.waiter_treeview.heading("#1", text="ID", anchor="center")
        self.waiter_treeview.heading("#2", text="name", anchor="center")
        self.waiter_treeview.heading("#3", text="cell phone", anchor="center")
        self.waiter_treeview.heading("#4", text="registration date", anchor="center")

        self.waiter_treeview.column("#1", minwidth=100, width=150, anchor="center")
        self.waiter_treeview.column("#2", minwidth=200, width=350, anchor="center")
        self.waiter_treeview.column("#3", minwidth=250, width=375, anchor="center")
        self.waiter_treeview.column("#4", minwidth=300, width=425, anchor="center")

        treeview_scrollbar = tkinter.Scrollbar(self.square_frame, orient=tkinter.VERTICAL, command=self.waiter_treeview.yview)
        self.waiter_treeview.configure(yscroll=treeview_scrollbar.set)
        treeview_scrollbar.place(x=1660, y=58, height=837)

        self.fn_read_waiters()

    def ui_update_waiter(self):
        self.data = self.selected_row()
        if not self.data:
            return
        
        self.topbar_label.configure(text="Update Waiter")
        self.search_waiters_entry.destroy()
        self.search_waiters_button.destroy()
        
        self.update_waiter_frame.destroy()
        self.delete_waiter_frame.destroy()

        self.waiter_name_entry.delete(0, "end")
        self.waiter_cellphone_entry.delete(0, "end")

        self.create_waiter_frame.configure(height=300)
        self.create_waiter_button.configure(text="Save Changes", 
                                            command=self.fn_update_waiter)

        self.cancel_button = customtkinter.CTkButton(master=self.create_waiter_frame,
                                                     width=330, height=35,
                                                     corner_radius=3,
                                                     font=("arial", 15),
                                                     text_color="#ffffff",
                                                     text="Cancel",
                                                     fg_color="#5c5c5c", 
                                                     hover_color="#6e6e6e",
                                                     command=self.ui_waiter)
        self.cancel_button.place(x=10, y=240)

        self.waiter_name_entry.insert(0, self.data[1])
        self.waiter_cellphone_entry.insert(0, self.data[2])

    def fn_create_waiter(self):
        if DbWaiter(token=self.__token).create_waiter(name=self.waiter_name_entry.get(),
                                                      cellphone=self.waiter_cellphone_entry.get()):
            self.clear_entries()
            self.fn_read_waiters()

    def fn_read_waiters(self):
        self.waiter_treeview.delete(*self.waiter_treeview.get_children())

        __all_waiters = [(i[0], i[1], i[2], i[3].replace(microsecond=0))
                         for i in DbWaiter(token=self.__token).read_waiters()]

        self.waiter_treeview.tag_configure("hexgray", background="#ededed")
        self.waiter_treeview.tag_configure("hexwhite", background="#fafbfc")
        
        tag = "hexwhite"
        for i in __all_waiters:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.waiter_treeview.insert("", "end", values=i, tags=tag)
    
    def fn_update_waiter(self):
        self.data = self.selected_row()
        if not self.data:
            return
        
        updated_waiter = DbWaiter(self.__token).update_waiter(new_name=self.waiter_name_entry.get(),
                                                              new_cellphone=self.waiter_cellphone_entry.get(),
                                                              id_waiter=self.data[0])
        
        if updated_waiter:
            self.ui_waiter()

    def fn_delete_waiter(self):
        self.data = self.selected_row()
        if not self.data:
            return
        
        message = f"Are you sure you want to delete\nthis waiter? {self.data[1]}."
        if tkinter.messagebox.askyesno(title="Delete Waiter", 
                                       message=message, 
                                       icon=tkinter.messagebox.WARNING) == True:
            DbWaiter(self.__token).delete_waiter(id_waiter=self.data[0])
            self.fn_read_waiters()

    def selected_row(self) -> tuple:
        try:
            selected_waiter = self.waiter_treeview.item(self.waiter_treeview.selection()[0], "values")
            return selected_waiter
        except IndexError:
            tkinter.messagebox.showerror(title=None, message="Please select a waiter")

    def clear_entries(self):
        self.waiter_name_entry.delete(0, "end")
        self.waiter_cellphone_entry.delete(0, "end")
        self.root.focus()
