from database import Database
from database import DbSignup
from database import DbLogin
from ui import UiPanel
from utils import clear_frames
from PIL import Image
import json
from tkinter import messagebox
import customtkinter

class UiLogin(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.iconbitmap("images/global_images/icon.ico")
        self.title("Restaurant Management System")
        self.geometry("1050x625+425+199")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("light")

        self._main_frame = customtkinter.CTkFrame(master=self)
        self._main_frame.pack()

        self._frame_one = customtkinter.CTkFrame(master=self._main_frame, 
                                                 fg_color="#ffc83d",
                                                 bg_color="#ffc83d")
        self._frame_one.grid(row=0, column=0)

        self._frame_two = customtkinter.CTkFrame(master=self._main_frame,
                                                 width=526, height=626,
                                                 fg_color="#e3e3e3",
                                                 bg_color="#e3e3e3")
        self._frame_two.grid(row=0, column=1)

        self._frame_three = customtkinter.CTkFrame(master=self._frame_two,
                                                   width=458, height=350,
                                                   fg_color="#ffffff",
                                                   corner_radius=10)
        self._frame_three.place(x=33, y=18)

        self._frame_four = customtkinter.CTkFrame(master=self._frame_two,
                                                  width=458, height=220,  
                                                  fg_color="#ffffff",
                                                  corner_radius=10)
        self._frame_four.place(x=33, y=388)

        self._ui_images()
        self._ui_login()

        # INSERT INTO account (username, password, email)
        # VALUES ('dev', 'daeed6308874de11ec5ba896aff636aee60821b397f88164be3eae5cf6d276d8', 'dev');
        if __token := DbLogin(username="dev", password="dev").create_access_token():
            UiPanel(root=self, token=__token)
    
    def _ui_images(self) -> None:
        # https://pixabay.com/illustrations/chef-food-kitchen-restaurant-adult-2410818/
        chefpil_image = Image.open("images/login_images/chef.png")
        self._chef_image = customtkinter.CTkImage(dark_image=chefpil_image,
                                                  light_image=chefpil_image, 
                                                  size=(480, 500))
    
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        userpil_image = Image.open("images/login_images/user.png")
        self._user_image = customtkinter.CTkImage(dark_image=userpil_image,
                                                  light_image=userpil_image,
                                                  size=(32,32))

        passwordpil_image = Image.open("images/login_images/password.png")
        self._password_image = customtkinter.CTkImage(dark_image=passwordpil_image,
                                                      light_image=passwordpil_image,
                                                      size=(32,32))
        
        hostpil_image = Image.open("images/login_images/host.png")
        self._host_image = customtkinter.CTkImage(dark_image=hostpil_image,
                                                  light_image=hostpil_image,
                                                  size=(32,32))
        
        emailpil_image = Image.open("images/login_images/email.png")
        self._email_image = customtkinter.CTkImage(dark_image=emailpil_image,
                                                   light_image=emailpil_image,
                                                   size=(33,33))
        
        keypasswordpil_image = Image.open("images/login_images/keypassword.png")
        self._keypassword_image = customtkinter.CTkImage(dark_image=keypasswordpil_image,
                                                         light_image=keypasswordpil_image,
                                                         size=(32,32))
        
        portpil_image = Image.open("images/login_images/port.png")
        self._port_image = customtkinter.CTkImage(dark_image=portpil_image,
                                                  light_image=portpil_image,
                                                  size=(32,32))
        
        # https://pixabay.com/vectors/arrow-left-gray-back-computer-23255/
        arrowpil_image = Image.open("images/login_images/arrow.png")
        self._arrow_image = customtkinter.CTkImage(dark_image=arrowpil_image,
                                                   light_image=arrowpil_image,
                                                   size=(15,15))
        
        # https://pixabay.com/vectors/eye-see-viewing-icon-1103592/
        showpasswordpil_image = Image.open("images/login_images/showpassword.png")
        self._showpassword_image = customtkinter.CTkImage(dark_image=showpasswordpil_image,
                                                          light_image=showpasswordpil_image,
                                                          size=(25,15))

        hidepasswordpil_image = Image.open("images/login_images/hidepassword.png")
        self._hidepassword_image = customtkinter.CTkImage(dark_image=hidepasswordpil_image,
                                                          light_image=hidepasswordpil_image,
                                                          size=(25,15))

        # https://pixabay.com/vectors/ok-check-to-do-agenda-icon-symbol-1976099/
        loggedpil_image = Image.open("images/login_images/logged.png")
        self._logged_image = customtkinter.CTkImage(dark_image=loggedpil_image,
                                                    light_image=loggedpil_image,
                                                    size=(45,45))
        
        # https://pixabay.com/vectors/false-error-is-missing-absent-x-2061131/
        loggedoutpil_image = Image.open("images/login_images/loggedout.png")
        self._loggedout_image = customtkinter.CTkImage(dark_image=loggedoutpil_image,
                                                       light_image=loggedoutpil_image,
                                                       size=(45,45)) 

    def _ui_login(self) -> None:
        chef_label = customtkinter.CTkLabel(master=self._frame_one, 
                                            corner_radius=0,
                                            text="", 
                                            image=self._chef_image)
        chef_label.grid(row=0, column=0, padx=22, pady=64)

        username_label = customtkinter.CTkLabel(master=self._frame_three,
                                                font=("arial", 15),
                                                text="  Username:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self._user_image)
        username_label.place(x=27, y=35)

        __username_entry = customtkinter.CTkEntry(master=self._frame_three, 
                                                  width=400, height=40,
                                                  font=("arial", 17),
                                                  fg_color="#EEEEEE",
                                                  border_color="#e3e3e3",
                                                  border_width=1)
        __username_entry.place(x=27, y=85)

        password_label = customtkinter.CTkLabel(master=self._frame_three,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self._password_image)
        password_label.place(x=27, y=142)

        self.__password_entry = customtkinter.CTkEntry(master=self._frame_three,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=192)

        self.__status_password_button = customtkinter.CTkButton(master=self._frame_three,
                                                                width=1, height=1, 
                                                                image=self._hidepassword_image, 
                                                                fg_color="#EEEEEE",
                                                                bg_color="#EEEEEE",
                                                                hover_color="#EEEEEE", 
                                                                text=None,
                                                                command=self.__show_password)
        self.__status_password_button.place(x=380, y=200)

        self.__hide_password = True

        __login_button = customtkinter.CTkButton(master=self._frame_three,
                                                 width=400, height=40, 
                                                 fg_color="#2b8dfc", 
                                                 hover_color="#4da0ff",
                                                 text_color="#ffffff",
                                                 text="Log in",
                                                 command=lambda:self.__login(username=__username_entry.get(), 
                                                                             password=self.__password_entry.get()))
        __login_button.place(x=27, y=270)

        setup_connection_label = customtkinter.CTkLabel(master=self._frame_four,
                                                        font=("arial", 15),
                                                        text="PostgreSQL Connection:",
                                                        text_color="#2e2e2e")
        setup_connection_label.place(x=27, y=20)

        setup_connection_button = customtkinter.CTkButton(master=self._frame_four,
                                                          width=400, height=40, 
                                                          fg_color="#fa9725",
                                                          hover_color="#f5a447", 
                                                          text_color="#ffffff", 
                                                          text="Setup Connection",
                                                          command=self._ui_setup_connection)
        setup_connection_button.place(x=27, y=55)

        create_acc_label = customtkinter.CTkLabel(master=self._frame_four,
                                                  font=("arial", 15),
                                                  text="Don't have an account?",
                                                  text_color="#2e2e2e")
        create_acc_label.place(x=27, y=106)

        create_acc_button = customtkinter.CTkButton(master=self._frame_four,
                                                    width=400, height=40, 
                                                    fg_color="#4bb34b", 
                                                    hover_color="#61bc61",
                                                    text_color="#ffffff", 
                                                    text="Sign up",
                                                    command=self._ui_signup)
        create_acc_button.place(x=27, y=141)

    def _ui_setup_connection(self) -> None:
        clear_frames(self._frame_three)
        clear_frames(self._frame_four)

        self.after(10, lambda:self._frame_three.configure(width=458, height=488))
        self.after(10, lambda:self._frame_three.place(x=33, y=18))
        
        self.after(10, lambda:self._frame_four.configure(width=458, height=84))
        self.after(10, lambda:self._frame_four.place(x=33, y=524))

        if Database.database_status():
            self._database_status_image = customtkinter.CTkLabel(self._frame_three, text="", image=self._logged_image)
            self._database_status_image.place(x=400, y=10)
        else:
            self._database_status_image = customtkinter.CTkLabel(self._frame_three, text="", image=self._loggedout_image)
            self._database_status_image.place(x=400, y=10)

        username_label = customtkinter.CTkLabel(master=self._frame_three,
                                                font=("arial", 15),
                                                text="  User:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self._user_image)
        username_label.place(x=27, y=35)

        self.__user_entry = customtkinter.CTkEntry(master=self._frame_three, 
                                                   width=400, height=40,
                                                   font=("arial", 17),
                                                   fg_color="#EEEEEE",
                                                   border_color="#e3e3e3",
                                                   border_width=1)
        self.__user_entry.place(x=27, y=85)

        password_label = customtkinter.CTkLabel(master=self._frame_three,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self._password_image)
        password_label.place(x=27, y=142)

        self.__password_entry = customtkinter.CTkEntry(master=self._frame_three,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=192)

        self.__hide_password = True

        self.__status_password_button = customtkinter.CTkButton(master=self._frame_three,
                                                                width=1, height=1, 
                                                                image=self._hidepassword_image, 
                                                                fg_color="#EEEEEE",
                                                                bg_color="#EEEEEE",
                                                                hover_color="#EEEEEE", 
                                                                text="",
                                                                command=self.__show_password)
        self.__status_password_button.place(x=380, y=200)

        host_label = customtkinter.CTkLabel(master=self._frame_three,
                                            font=("arial", 15),
                                            text="  Host:",
                                            compound="left",
                                            text_color="#2e2e2e",
                                            image=self._host_image)
        host_label.place(x=27, y=249)

        self.__host_entry = customtkinter.CTkEntry(master=self._frame_three,
                                                   width=400, height=40,
                                                   font=("arial", 17), 
                                                   fg_color="#EEEEEE", 
                                                   border_color="#e3e3e3", 
                                                   border_width=1)
        self.__host_entry.place(x=27, y=299)

        port_label = customtkinter.CTkLabel(master=self._frame_three,
                                            font=("arial", 15),
                                            text="  Port:",
                                            compound="left",
                                            text_color="#2e2e2e",
                                            image=self._port_image)
        port_label.place(x=27, y=356)

        self.__port_entry = customtkinter.CTkEntry(master=self._frame_three,
                                                   width=400, height=40,
                                                   font=("arial", 17), 
                                                   fg_color="#EEEEEE", 
                                                   border_color="#e3e3e3", 
                                                   border_width=1)
        self.__port_entry.place(x=27, y=406)

        __save_changes_button = customtkinter.CTkButton(master=self._frame_four,
                                                        corner_radius=10,
                                                        width=192, height=40, 
                                                        fg_color="#0077ff", 
                                                        hover_color="#1f88ff",
                                                        text_color="#ffffff", 
                                                        text="Save Changes",
                                                        command=self.__save_connection_settings)
        __save_changes_button.place(x=27, y=22)

        to_back_button = customtkinter.CTkButton(master=self._frame_four,
                                                 corner_radius=10, 
                                                 width=192, height=40,
                                                 fg_color="#5c5c5c",
                                                 hover_color="#6e6e6e", 
                                                 text_color="#ffffff", 
                                                 text="Go back",
                                                 compound="left",
                                                 image=self._arrow_image,
                                                 command=self._go_back_loginscreen)
        to_back_button.place(x=236, y=22)

        try:
            with open("database/config.json") as file:
                __data = json.load(file)
                self.__host_entry.configure(placeholder_text=__data["host"])
                self.__user_entry.configure(placeholder_text=__data["user"])
                self.__password_entry.configure(placeholder_text= "*" * len(__data["password"]))
                self.__port_entry.configure(placeholder_text=__data["port"])
        except:
            self.__host_entry.configure(placeholder_text="")
            self.__user_entry.configure(placeholder_text="")
            self.__password_entry.configure(placeholder_text="")
            self.__port_entry.configure(placeholder_text="")
            
            config_messagebox = {"icon": "error","type": "yesno"}
            modal = messagebox.showerror("database/config.json", "Error in the database configuration file.\nRestore file?", **config_messagebox)
            
            if modal == "yes":
                __data = {"user": "postgres", "password": "admin", "host": "localhost", "port": "5432"}
                with open("database/config.json", "w") as __file:
                    json.dump(__data, __file, indent=4)
                    __file.write("\n")
                self._ui_setup_connection()

    def _ui_signup(self) -> None:
        clear_frames(self._frame_three)
        clear_frames(self._frame_four)

        self.after(10, lambda:self._frame_three.configure(width=458, height=450))
        self.after(10, lambda:self._frame_three.place(x=33, y=18))
        
        self.after(10, lambda:self._frame_four.configure(width=458, height=120))
        self.after(10, lambda:self._frame_four.place(x=33, y=488))

        username_label = customtkinter.CTkLabel(master=self._frame_three,
                                                font=("arial", 15),
                                                text="  Username:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self._user_image)
        username_label.place(x=27, y=35)
        
        __username_entry = customtkinter.CTkEntry(master=self._frame_three,
                                                  width=400, height=40,
                                                  font=("arial", 17), 
                                                  fg_color="#EEEEEE", 
                                                  border_color="#e3e3e3", 
                                                  border_width=1)
        __username_entry.place(x=27, y=85)
        
        password_label = customtkinter.CTkLabel(master=self._frame_three,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self._keypassword_image)
        password_label.place(x=27, y=142)

        self.__password_entry = customtkinter.CTkEntry(master=self._frame_three, 
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=192)

        self.__hide_password = True

        self.__status_password_button = customtkinter.CTkButton(master=self._frame_three,
                                                                width=1, height=1, 
                                                                image=self._hidepassword_image, 
                                                                fg_color="#EEEEEE",
                                                                bg_color="#EEEEEE",
                                                                hover_color="#EEEEEE", 
                                                                text="",
                                                                command=self.__show_password)
        self.__status_password_button.place(x=380, y=200)
   
        email_label = customtkinter.CTkLabel(master=self._frame_three,
                                             font=("arial", 15),
                                             text="  Email:",
                                             compound="left",
                                             text_color="#2e2e2e",
                                             image=self._email_image)
        email_label.place(x=27, y=249)

        __email_entry = customtkinter.CTkEntry(master=self._frame_three,
                                               width=400, height=40,
                                               font=("arial", 17), 
                                               fg_color="#EEEEEE", 
                                               border_color="#e3e3e3", 
                                               border_width=1)
        __email_entry.place(x=27, y=299)

        __signup_button = customtkinter.CTkButton(master=self._frame_three, 
                                                  width=400, height=40,
                                                  fg_color="#0077ff", 
                                                  hover_color="#1f88ff",
                                                  text_color="#ffffff",
                                                  text="Sign up",
                                                  command=lambda:DbSignup(username=__username_entry.get(),
                                                                          password=self.__password_entry.get(),
                                                                          email=__email_entry.get()))
        __signup_button.place(x=27, y=380)

        to_back_button = customtkinter.CTkButton(master=self._frame_four,
                                                 width=400, height=40, 
                                                 fg_color="#5c5c5c",
                                                 hover_color="#6e6e6e", 
                                                 text_color="#ffffff",
                                                 text="Go back",
                                                 compound="left",
                                                 image=self._arrow_image,
                                                 command=self._go_back_loginscreen)
        to_back_button.place(x=27, y=41)

        if not Database.database_status():
            __username_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            self.__password_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            __email_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            __signup_button.configure(state="disabled", fg_color="#429aff")
            self.__status_password_button.destroy()
            
            messagebox.showerror("Connection", "Can't register. Database connection failed.")

    def __show_password(self) -> None:
        if self.__hide_password:
            self.__status_password_button.configure(image=self._showpassword_image)
            self.__password_entry.configure(show="")
            self.__hide_password = False
        else:
            self.__status_password_button.configure(image=self._hidepassword_image)
            self.__password_entry.configure(show="*")
            self.__hide_password = True

    def __save_connection_settings(self) -> None:
        if self.__user_entry.get() != "": 
            try: 
                with open("database/config.json") as __file:
                    __data = json.load(__file)
                    __data["user"] = self.__user_entry.get()
                    __data["password"] = self.__password_entry.get()
                    __data["host"] = self.__host_entry.get()
                    __data["port"] = self.__port_entry.get()

                with open("database/config.json", "w") as __file:
                    json.dump(__data, __file, indent=4)
                    __file.write("\n")
            except FileNotFoundError as error:
                messagebox.showerror("Error!", f"file or directory does not exist:\ndatabase/config.json\n{error}")
            except Exception as error:
                messagebox.showerror("Error!", error)
            else:
                self._ui_setup_connection()
                Database().connect_to_database(database=None)

    def __login(self, username, password) -> None:
        if __token := DbLogin(username=username, password=password).create_access_token():
            UiPanel(root=self, token=__token)

    def _go_back_loginscreen(self) -> None:
        clear_frames(self._frame_three)
        clear_frames(self._frame_four)

        self.after(10, lambda:self._frame_three.configure(width=458, height=350))
        self.after(10, lambda:self._frame_three.place(x=33, y=18))
        
        self.after(10, lambda:self._frame_four.configure(width=458, height=220))
        self.after(10, lambda:self._frame_four.place(x=33, y=388))

        self._ui_login()
