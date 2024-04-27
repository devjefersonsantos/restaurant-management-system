import customtkinter
from database.db_login import DbLogin
from utils.clear_frames import clear_frames
import tkinter

class UiCategory:
    @DbLogin.verify_token
    def __init__(self, root: customtkinter.CTk, 
                 square_frame: customtkinter.CTk, 
                 token: str) -> None:
        self._root = root
        self._square_frame = square_frame
        self.__token = token

        clear_frames(self._square_frame)
        self._ui_category()

    def _topbar(self) -> None:
        topbar_frame = customtkinter.CTkFrame(master=self._square_frame,
                                              width=1678, height=50,
                                              corner_radius=0)
        topbar_frame.place(x=0, y=0)
        
        self._topbar_label = customtkinter.CTkLabel(master=topbar_frame, 
                                                    font=("arial black", 25),
                                                    text_color="#ffffff", 
                                                    text="Category")
        self._topbar_label.place(x=20, y=5)

        self._search_categories_entry = customtkinter.CTkEntry(master=topbar_frame,
                                                               width=1227, height=35,
                                                               placeholder_text="Search by category name",
                                                               font=("arial", 17), 
                                                               fg_color="#EEEEEE", 
                                                               border_color="#e3e3e3", 
                                                               border_width=1)
        self._search_categories_entry.place(x=174, y=8)

        self._search_categories_button = customtkinter.CTkButton(master=topbar_frame,
                                                                 width=230, height=32,
                                                                 corner_radius=4,
                                                                 text_color="#ffffff",
                                                                 font=("arial", 15), 
                                                                 text="Search",
                                                                 fg_color="#407ecf", 
                                                                 hover_color="#6996d1")
        self._search_categories_button.place(x=1425, y=9)

    def _ui_category(self) -> None:
        clear_frames(self._square_frame)

        self._topbar()

        self._create_category_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                             width=350, height=316,
                                                             corner_radius=10,
                                                             fg_color="#ffffff")
        self._create_category_frame.place(x=10, y=58)

        category_name_label = customtkinter.CTkLabel(master=self._create_category_frame, 
                                                     font=("arial", 17), 
                                                     text_color="#383838", 
                                                     text="Category name:")
        category_name_label.place(x=10, y=10)

        self.__category_name_entry = customtkinter.CTkEntry(master=self._create_category_frame,
                                                            width=330, height=35,
                                                            corner_radius=3, 
                                                            font=("arial", 17), 
                                                            border_color="#e3e3e3", 
                                                            border_width=1)
        self.__category_name_entry.place(x=10, y=45)

        description_label = customtkinter.CTkLabel(master=self._create_category_frame, 
                                                   font=("arial", 17), 
                                                   text_color="#383838", 
                                                   text="Description:")
        description_label.place(x=10, y=90)

        self.__description_textbox = customtkinter.CTkTextbox(master=self._create_category_frame,
                                                              width=330, height=110,
                                                              corner_radius=3, 
                                                              font=("arial", 17), 
                                                              border_color="#e3e3e3", 
                                                              border_width=1)
        self.__description_textbox.place(x=10, y=125)

        self.__create_category_button = customtkinter.CTkButton(master=self._create_category_frame,
                                                                width=330, height=35,
                                                                corner_radius=3,
                                                                font=("arial", 15),
                                                                text_color="#ffffff",
                                                                text="Add Category",
                                                                fg_color="#4bb34b", 
                                                                hover_color="#7ebf7e")
        self.__create_category_button.place(x=10, y=260)

        self._update_category_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                             width=350, height=100,
                                                             corner_radius=10,
                                                             fg_color="#ffffff")
        self._update_category_frame.place(x=10, y=680)

        update_category_label = customtkinter.CTkLabel(master=self._update_category_frame, 
                                                       font=("arial", 17), 
                                                       text_color="#383838", 
                                                       text="Update selected category:")
        update_category_label.place(x=10, y=10)

        update_category_button = customtkinter.CTkButton(master=self._update_category_frame,
                                                         width=330, height=35,
                                                         corner_radius=3,
                                                         font=("arial", 15),
                                                         text_color="#ffffff",
                                                         text="Update Category",
                                                         fg_color="#ec971f", 
                                                         hover_color="#f0b35d")
        update_category_button.place(x=10, y=45)

        self._delete_category_frame = customtkinter.CTkFrame(master=self._square_frame,
                                                             width=350, height=100,
                                                             corner_radius=10,
                                                             fg_color="#ffffff")
        self._delete_category_frame.place(x=10, y=795)

        delete_category_label = customtkinter.CTkLabel(master=self._delete_category_frame, 
                                                       font=("arial", 17), 
                                                       text_color="#383838", 
                                                       text="Delete selected category:")
        delete_category_label.place(x=10, y=10)

        __delete_category_button = customtkinter.CTkButton(master=self._delete_category_frame,
                                                           width=330, height=35,
                                                           corner_radius=3,
                                                           font=("arial", 15),
                                                           text_color="#ffffff",
                                                           text="Delete Category",
                                                           fg_color="#d54a49", 
                                                           hover_color="#d1706f")
        __delete_category_button.place(x=10, y=45)

        style = tkinter.ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.__category_treeview = tkinter.ttk.Treeview(master=self._square_frame,
                                                        height=29,
                                                        style="style_treeview.Treeview",
                                                        columns=("id category", "category name", "description"),
                                                        show="headings")
        self.__category_treeview.place(x=370, y=58)

        self.__category_treeview.heading("#1", text="id category", anchor="center")
        self.__category_treeview.heading("#2", text="category name", anchor="center")
        self.__category_treeview.heading("#3", text="description", anchor="center")

        self.__category_treeview.column("#1", minwidth=150, width=225, anchor="center")
        self.__category_treeview.column("#2", minwidth=150, width=375, anchor="center")
        self.__category_treeview.column("#3", minwidth=150, width=700, anchor="center")

        _treeview_scrollbar = tkinter.Scrollbar(self._square_frame, orient=tkinter.VERTICAL, command=self.__category_treeview.yview)
        self.__category_treeview.configure(yscroll=_treeview_scrollbar.set)
        _treeview_scrollbar.place(x=1660, y=58, height=837)
