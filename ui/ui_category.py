import customtkinter
from database.db_login import DbLogin
from utils.clear_frames import clear_frames
import tkinter
from tkinter import ttk
from database.db_category import DbCategory

class UiCategory:
    @DbLogin.verify_token
    def __init__(self, 
                 root: customtkinter.CTk, 
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
                                                                 hover_color="#6996d1",
                                                                 command=lambda:self.__fn_search_category(self._search_categories_entry.get()))
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
                                                                hover_color="#7ebf7e",
                                                                command=self.__fn_create_category)
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
                                                         hover_color="#f0b35d",
                                                         command=self._ui_update_category)
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
                                                           hover_color="#d1706f",
                                                           command=self.__fn_delete_category)
        __delete_category_button.place(x=10, y=45)

        style = ttk.Style()
        style.layout("style_treeview.Treeview", [("style_treeview.Treeview.treearea", {"sticky": "nswe"})])
        style.configure("Treeview.Heading", font=("Arial", 13), foreground="#1c1c1c")
        style.configure("Treeview", font=("Arial", 13), foreground="#1c1c1c", rowheight=28)

        self.__category_treeview = ttk.Treeview(master=self._square_frame,
                                                height=29,
                                                style="style_treeview.Treeview",
                                                columns=("id category", "category name", "description"),
                                                show="headings")
        self.__category_treeview.place(x=370, y=58)

        self.__category_treeview.heading("#1", text="id category", anchor="center")
        self.__category_treeview.heading("#2", text="category name", anchor="center")
        self.__category_treeview.heading("#3", text="  description", anchor="w")

        self.__category_treeview.column("#1", minwidth=150, width=225, anchor="center")
        self.__category_treeview.column("#2", minwidth=150, width=375, anchor="center")
        self.__category_treeview.column("#3", minwidth=150, width=700, anchor="w")

        _treeview_scrollbar = tkinter.Scrollbar(self._square_frame, orient=tkinter.VERTICAL, command=self.__category_treeview.yview)
        self.__category_treeview.configure(yscroll=_treeview_scrollbar.set)
        _treeview_scrollbar.place(x=1660, y=58, height=837)

        self.__fn_read_categories()

    def _ui_update_category(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
        
        self._topbar_label.configure(text="Update Category")
        self._search_categories_entry.destroy()
        self._search_categories_button.destroy()
        
        self._update_category_frame.destroy()
        self._delete_category_frame.destroy()

        self.__category_name_entry.delete(0, "end")
        self.__description_textbox.delete("1.0", "end")

        self._create_category_frame.configure(height=365)
        self.__create_category_button.configure(text="Save Changes",
                                                command=self.__fn_update_category)

        self._cancel_button = customtkinter.CTkButton(master=self._create_category_frame,
                                                      width=330, height=35,
                                                      corner_radius=3,
                                                      font=("arial", 15),
                                                      text_color="#ffffff",
                                                      text="Cancel",
                                                      fg_color="#5c5c5c", 
                                                      hover_color="#6e6e6e",
                                                      command=self._ui_category)
        self._cancel_button.place(x=10, y=310)

        self.__category_name_entry.insert(0, self.__data[1])
        self.__description_textbox.insert("0.0", self.__data[2])

    def __fn_create_category(self) -> None:
        if DbCategory(token=self.__token).create_category(name=self.__category_name_entry.get(),
                                                          description=self.__description_textbox.get("1.0","end").strip()):
            self._clear_entries()
            self.__fn_read_categories()

    def __fn_read_categories(self) -> None:
        self.__category_treeview.delete(*self.__category_treeview.get_children())

        __all_categories = [i for i in DbCategory(token=self.__token).read_categories()]

        self.__category_treeview.tag_configure("hexgray", background="#ededed")
        self.__category_treeview.tag_configure("hexwhite", background="#fafbfc")
        
        tag = "hexwhite"
        for i in __all_categories:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.__category_treeview.insert("", "end", values=i, tags=tag)
    
    def __fn_update_category(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
        
        updated_category = DbCategory(self.__token).update_category(new_name=self.__category_name_entry.get(),
                                                                    new_description=self.__description_textbox.get("1.0", "end").strip(),
                                                                    id_category=self.__data[0])
        
        if updated_category:
            self._ui_category()

    def __fn_delete_category(self) -> None:
        self.__data = self.__selected_row()
        if not self.__data:
            return
        
        message = f"Are you sure you want to delete\nthis category? {self.__data[1]}."
        if tkinter.messagebox.askyesno(title="Delete Category", 
                                       message=message, 
                                       icon=tkinter.messagebox.WARNING) == True:
            DbCategory(self.__token).delete_category(id_category=self.__data[0])
            self.__fn_read_categories()

    def __fn_search_category(self, typed: str) -> None:
        self.__category_treeview.delete(*self.__category_treeview.get_children())

        __category = DbCategory(self.__token).search_category(typed=typed)

        tag = "hexwhite"
        for i in __category:
            tag = "hexgray" if tag == "hexwhite" else "hexwhite"
            self.__category_treeview.insert("", "end", values=i, tags=tag)

    def __selected_row(self) -> tuple:
        try:
            selected_category = self.__category_treeview.item(self.__category_treeview.selection()[0], "values")
            return selected_category
        except IndexError:
            tkinter.messagebox.showerror(title=None, message="Please select a category")

    def _clear_entries(self) -> None:
        self.__category_name_entry.delete(0, "end")
        self.__description_textbox.delete("1.0","end")
        self._root.focus()
