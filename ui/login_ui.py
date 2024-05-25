import json
from tkinter import messagebox

from PIL import Image
import customtkinter

from utils.colors import *
from database import Database 
from database.account_db import SignupDb
from database.account_db import LoginDb
from ui import SidebarUI
from utils import clear_frames

class LoginUI(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.iconbitmap("./images/global_images/icon.ico")
        self.title("Restaurant Management System")
        self.geometry("1050x625+425+199")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("light")

        self.__main_frame = customtkinter.CTkFrame(master=self)
        self.__main_frame.pack()

        self.__frame_one = customtkinter.CTkFrame(master=self.__main_frame, 
                                                  fg_color=ORANGE_FRAME_COLOR,
                                                  bg_color=ORANGE_FRAME_COLOR)
        self.__frame_one.grid(row=0, column=0)

        self.__frame_two = customtkinter.CTkFrame(master=self.__main_frame,
                                                  width=526, height=626,
                                                  fg_color=LIGHT_GRAY_COLOR,
                                                  bg_color=LIGHT_GRAY_COLOR)
        self.__frame_two.grid(row=0, column=1)

        self.__frame_three = customtkinter.CTkFrame(master=self.__frame_two,
                                                    width=458, height=350,
                                                    fg_color=WHITE_COLOR,
                                                    corner_radius=10)
        self.__frame_three.place(x=33, y=18)

        self.__frame_four = customtkinter.CTkFrame(master=self.__frame_two,
                                                   width=458, height=220,  
                                                   fg_color=WHITE_COLOR,
                                                   corner_radius=10)
        self.__frame_four.place(x=33, y=388)

        self.__images_ui()
        self.__login_ui()

        # INSERT INTO account (username, password, email)
        # VALUES ('dev', 'daeed6308874de11ec5ba896aff636aee60821b397f88164be3eae5cf6d276d8', 'dev');
        if token := LoginDb(username="dev", password="dev").process_login():
            SidebarUI(root=self, token=token)
    
    def __images_ui(self) -> None:
        # https://pixabay.com/illustrations/chef-food-kitchen-restaurant-adult-2410818/
        chefpil_image = Image.open("./images/login_images/chef.png")
        self.__chef_image = customtkinter.CTkImage(dark_image=chefpil_image,
                                                   light_image=chefpil_image, 
                                                   size=(480, 500))
    
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        userpil_image = Image.open("./images/login_images/user.png")
        self.__user_image = customtkinter.CTkImage(dark_image=userpil_image,
                                                   light_image=userpil_image,
                                                   size=(32,32))

        passwordpil_image = Image.open("./images/login_images/password.png")
        self.__password_image = customtkinter.CTkImage(dark_image=passwordpil_image,
                                                       light_image=passwordpil_image,
                                                       size=(32,32))
        
        hostpil_image = Image.open("./images/login_images/host.png")
        self.__host_image = customtkinter.CTkImage(dark_image=hostpil_image,
                                                   light_image=hostpil_image,
                                                   size=(32,32))
        
        emailpil_image = Image.open("./images/login_images/email.png")
        self.__email_image = customtkinter.CTkImage(dark_image=emailpil_image,
                                                    light_image=emailpil_image,
                                                    size=(33,33))
        
        keypasswordpil_image = Image.open("./images/login_images/keypassword.png")
        self.__keypassword_image = customtkinter.CTkImage(dark_image=keypasswordpil_image,
                                                          light_image=keypasswordpil_image,
                                                          size=(32,32))
        
        portpil_image = Image.open("./images/login_images/port.png")
        self.__port_image = customtkinter.CTkImage(dark_image=portpil_image,
                                                   light_image=portpil_image,
                                                   size=(32,32))
        
        # https://pixabay.com/vectors/arrow-left-gray-back-computer-23255/
        arrowpil_image = Image.open("./images/login_images/arrow.png")
        self.__arrow_image = customtkinter.CTkImage(dark_image=arrowpil_image,
                                                    light_image=arrowpil_image,
                                                    size=(15,15))
        
        # https://pixabay.com/vectors/eye-see-viewing-icon-1103592/
        showpasswordpil_image = Image.open("./images/login_images/showpassword.png")
        self.__showpassword_image = customtkinter.CTkImage(dark_image=showpasswordpil_image,
                                                           light_image=showpasswordpil_image,
                                                           size=(25,15))

        hidepasswordpil_image = Image.open("./images/login_images/hidepassword.png")
        self.__hidepassword_image = customtkinter.CTkImage(dark_image=hidepasswordpil_image,
                                                           light_image=hidepasswordpil_image,
                                                           size=(25,15))

        # https://pixabay.com/vectors/ok-check-to-do-agenda-icon-symbol-1976099/
        loggedpil_image = Image.open("./images/login_images/logged.png")
        self.__logged_image = customtkinter.CTkImage(dark_image=loggedpil_image,
                                                     light_image=loggedpil_image,
                                                     size=(45,45))
        
        # https://pixabay.com/vectors/false-error-is-missing-absent-x-2061131/
        loggedoutpil_image = Image.open("./images/login_images/loggedout.png")
        self.__loggedout_image = customtkinter.CTkImage(dark_image=loggedoutpil_image,
                                                        light_image=loggedoutpil_image,
                                                        size=(45,45)) 

    def __login_ui(self) -> None:
        chef_label = customtkinter.CTkLabel(master=self.__frame_one, 
                                            corner_radius=0,
                                            text="", 
                                            image=self.__chef_image)
        chef_label.grid(row=0, column=0, padx=22, pady=64)

        username_label = customtkinter.CTkLabel(master=self.__frame_three,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 15),
                                                text="  Username:",
                                                compound="left",
                                                image=self.__user_image)
        username_label.place(x=27, y=35)

        username_entry = customtkinter.CTkEntry(master=self.__frame_three, 
                                                width=400, height=40,
                                                border_color=LIGHT_GRAY_COLOR,
                                                fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                font=("arial", 17),
                                                border_width=1)
        username_entry.place(x=27, y=85)

        password_label = customtkinter.CTkLabel(master=self.__frame_three,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                image=self.__password_image)
        password_label.place(x=27, y=142)

        self.__password_entry = customtkinter.CTkEntry(master=self.__frame_three,
                                                       width=400, height=40,
                                                       fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                       border_color=LIGHT_GRAY_COLOR, 
                                                       font=("arial", 17), 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=192)

        self.__status_password_button = customtkinter.CTkButton(master=self.__frame_three,
                                                                width=1, height=1, 
                                                                fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                bg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                hover_color=LIGHT_GRAY_HOVER_COLOR, 
                                                                image=self.__hidepassword_image, 
                                                                text=None,
                                                                command=self.__show_password)
        self.__status_password_button.place(x=380, y=200)

        self.__hide_password = True

        login_button = customtkinter.CTkButton(master=self.__frame_three,
                                               width=400, height=40, 
                                               fg_color=LIGHT_BLUE_COLOR, 
                                               hover_color=LIGHT_BLUE_HOVER_COLOR,
                                               text_color=WHITE_COLOR,
                                               text="Log in",
                                               command=lambda:self.__login(username=username_entry.get(), 
                                                                           password=self.__password_entry.get()))
        login_button.place(x=27, y=270)

        self.bind("<Return>", lambda _ : login_button.invoke())

        setup_connection_label = customtkinter.CTkLabel(master=self.__frame_four,
                                                        font=("arial", 15),
                                                        text_color=GRAY_TEXT_COLOR,
                                                        text="PostgreSQL Connection:")
        setup_connection_label.place(x=27, y=20)

        setup_connection_button = customtkinter.CTkButton(master=self.__frame_four,
                                                          width=400, height=40, 
                                                          fg_color=ORANGE_COLOR,
                                                          hover_color=ORANGE_HOVER_COLOR, 
                                                          text_color=WHITE_COLOR, 
                                                          text="Setup Connection",
                                                          command=self.__setup_connection_ui)
        setup_connection_button.place(x=27, y=55)

        create_acc_label = customtkinter.CTkLabel(master=self.__frame_four,
                                                  font=("arial", 15),
                                                  text_color=GRAY_TEXT_COLOR,
                                                  text="Don't have an account?")
        create_acc_label.place(x=27, y=106)

        create_acc_button = customtkinter.CTkButton(master=self.__frame_four,
                                                    width=400, height=40, 
                                                    fg_color=GREEN_COLOR, 
                                                    hover_color=GREEN_HOVER_COLOR,
                                                    text_color=WHITE_COLOR, 
                                                    text="Sign up",
                                                    command=self.__signup_ui)
        create_acc_button.place(x=27, y=141)

    def __setup_connection_ui(self) -> None:
        clear_frames(self.__frame_three)
        clear_frames(self.__frame_four)

        self.after(10, lambda:self.__frame_three.configure(width=458, height=488))
        self.after(10, lambda:self.__frame_three.place(x=33, y=18))
        
        self.after(10, lambda:self.__frame_four.configure(width=458, height=84))
        self.after(10, lambda:self.__frame_four.place(x=33, y=524))

        if Database.database_status():
            database_status_image = customtkinter.CTkLabel(self.__frame_three, text="", image=self.__logged_image)
            database_status_image.place(x=400, y=10)
        else:
            database_status_image = customtkinter.CTkLabel(self.__frame_three, text="", image=self.__loggedout_image)
            database_status_image.place(x=400, y=10)

        username_label = customtkinter.CTkLabel(master=self.__frame_three,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 15),
                                                text="  User:",
                                                compound="left",
                                                image=self.__user_image)
        username_label.place(x=27, y=35)

        self.__user_entry = customtkinter.CTkEntry(master=self.__frame_three, 
                                                   width=400, height=40,
                                                   fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                   border_color=LIGHT_GRAY_COLOR,
                                                   font=("arial", 17),
                                                   border_width=1)
        self.__user_entry.place(x=27, y=85)

        password_label = customtkinter.CTkLabel(master=self.__frame_three,
                                                font=("arial", 15),
                                                text_color=GRAY_TEXT_COLOR,
                                                text="  Password:",
                                                compound="left",
                                                image=self.__password_image)
        password_label.place(x=27, y=142)

        self.__password_entry = customtkinter.CTkEntry(master=self.__frame_three,
                                                       width=400, height=40,
                                                       fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                       border_color=LIGHT_GRAY_COLOR, 
                                                       font=("arial", 17), 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=192)

        self.__hide_password = True

        self.__status_password_button = customtkinter.CTkButton(master=self.__frame_three,
                                                                width=1, height=1, 
                                                                fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                bg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                hover_color=LIGHT_GRAY_HOVER_COLOR, 
                                                                image=self.__hidepassword_image, 
                                                                text="",
                                                                command=self.__show_password)
        self.__status_password_button.place(x=380, y=200)

        host_label = customtkinter.CTkLabel(master=self.__frame_three,
                                            font=("arial", 15),
                                            text_color=GRAY_TEXT_COLOR,
                                            text="  Host:",
                                            compound="left",
                                            image=self.__host_image)
        host_label.place(x=27, y=249)

        self.__host_entry = customtkinter.CTkEntry(master=self.__frame_three,
                                                   width=400, height=40,
                                                   fg_color=LIGHT_GRAY_HOVER_COLOR, 
                                                   border_color=LIGHT_GRAY_COLOR, 
                                                   font=("arial", 17), 
                                                   border_width=1)
        self.__host_entry.place(x=27, y=299)

        port_label = customtkinter.CTkLabel(master=self.__frame_three,
                                            font=("arial", 15),
                                            text_color=GRAY_TEXT_COLOR,
                                            text="  Port:",
                                            compound="left",
                                            image=self.__port_image)
        port_label.place(x=27, y=356)

        self.__port_entry = customtkinter.CTkEntry(master=self.__frame_three,
                                                   width=400, height=40,
                                                   fg_color=LIGHT_GRAY_HOVER_COLOR, 
                                                   border_color=LIGHT_GRAY_COLOR, 
                                                   font=("arial", 17), 
                                                   border_width=1)
        self.__port_entry.place(x=27, y=406)

        save_changes_button = customtkinter.CTkButton(master=self.__frame_four,
                                                      width=192, height=40, 
                                                      fg_color=LIGHT_BLUE_COLOR, 
                                                      hover_color=LIGHT_BLUE_HOVER_COLOR,
                                                      text_color=WHITE_COLOR, 
                                                      corner_radius=10,
                                                      text="Save Changes",
                                                      command=self.__save_connection_settings)
        save_changes_button.place(x=27, y=22)

        self.bind("<Return>", lambda _ : save_changes_button.invoke())

        to_back_button = customtkinter.CTkButton(master=self.__frame_four,
                                                 width=192, height=40,
                                                 fg_color=GRAY_COLOR,
                                                 hover_color=GRAY_HOVER_COLOR, 
                                                 text_color=WHITE_COLOR, 
                                                 corner_radius=10, 
                                                 text="Go back",
                                                 compound="left",
                                                 image=self.__arrow_image,
                                                 command=self.__go_back_loginscreen)
        to_back_button.place(x=236, y=22)

        try:
            with open("./database/config.json") as file:
                data = json.load(file)
                self.__host_entry.configure(placeholder_text=data["host"])
                self.__user_entry.configure(placeholder_text=data["user"])
                self.__password_entry.configure(placeholder_text= "*" * len(data["password"]))
                self.__port_entry.configure(placeholder_text=data["port"])
        except:
            self.__host_entry.configure(placeholder_text="")
            self.__user_entry.configure(placeholder_text="")
            self.__password_entry.configure(placeholder_text="")
            self.__port_entry.configure(placeholder_text="")
            
            config_messagebox = {"icon": "error","type": "yesno"}
            modal = messagebox.showerror("./database/config.json", "Error in the database configuration file.\nRestore file?", **config_messagebox)
            
            if modal == "yes":
                data = {"user": "postgres", "password": "admin", "host": "localhost", "port": "5432"}
                with open("./database/config.json", "w") as file:
                    json.dump(data, file, indent=4)
                    file.write("\n")
                self.__setup_connection_ui()

    def __signup_ui(self) -> None:
        clear_frames(self.__frame_three)
        clear_frames(self.__frame_four)

        self.after(10, lambda:self.__frame_three.configure(width=458, height=450))
        self.after(10, lambda:self.__frame_three.place(x=33, y=18))
        
        self.after(10, lambda:self.__frame_four.configure(width=458, height=120))
        self.after(10, lambda:self.__frame_four.place(x=33, y=488))

        username_label = customtkinter.CTkLabel(master=self.__frame_three,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 15),
                                                text="  Username:",
                                                compound="left",
                                                image=self.__user_image)
        username_label.place(x=27, y=35)
        
        username_entry = customtkinter.CTkEntry(master=self.__frame_three,
                                                width=400, height=40,
                                                fg_color=LIGHT_GRAY_HOVER_COLOR, 
                                                border_color=LIGHT_GRAY_COLOR, 
                                                font=("arial", 17), 
                                                border_width=1)
        username_entry.place(x=27, y=85)
        
        password_label = customtkinter.CTkLabel(master=self.__frame_three,
                                                text_color=GRAY_TEXT_COLOR,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                image=self.__keypassword_image)
        password_label.place(x=27, y=142)

        self.__password_entry = customtkinter.CTkEntry(master=self.__frame_three, 
                                                       width=400, height=40,
                                                       fg_color=LIGHT_GRAY_HOVER_COLOR, 
                                                       border_color=LIGHT_GRAY_COLOR, 
                                                       font=("arial", 17), 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=192)

        self.__hide_password = True

        self.__status_password_button = customtkinter.CTkButton(master=self.__frame_three,
                                                                width=1, height=1, 
                                                                fg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                bg_color=LIGHT_GRAY_HOVER_COLOR,
                                                                hover_color=LIGHT_GRAY_HOVER_COLOR, 
                                                                image=self.__hidepassword_image, 
                                                                text="",
                                                                command=self.__show_password)
        self.__status_password_button.place(x=380, y=200)
   
        email_label = customtkinter.CTkLabel(master=self.__frame_three,
                                             text_color=GRAY_TEXT_COLOR,
                                             font=("arial", 15),
                                             text="  Email:",
                                             compound="left",
                                             image=self.__email_image)
        email_label.place(x=27, y=249)

        email_entry = customtkinter.CTkEntry(master=self.__frame_three,
                                             width=400, height=40,
                                             fg_color=LIGHT_GRAY_HOVER_COLOR,
                                             border_color=LIGHT_GRAY_COLOR, 
                                             font=("arial", 17), 
                                             border_width=1)
        email_entry.place(x=27, y=299)

        signup_button = customtkinter.CTkButton(master=self.__frame_three, 
                                                width=400, height=40,
                                                fg_color=LIGHT_BLUE_COLOR, 
                                                hover_color=LIGHT_BLUE_HOVER_COLOR,
                                                text_color=WHITE_COLOR,
                                                text="Sign up",
                                                command=lambda:SignupDb(username=username_entry.get(),
                                                                        password=self.__password_entry.get(),
                                                                        email=email_entry.get()))
        signup_button.place(x=27, y=380)

        self.bind("<Return>", lambda _ : signup_button.invoke())

        to_back_button = customtkinter.CTkButton(master=self.__frame_four,
                                                 width=400, height=40, 
                                                 fg_color=GRAY_COLOR,
                                                 hover_color=GRAY_HOVER_COLOR, 
                                                 text_color=WHITE_COLOR,
                                                 text="Go back",
                                                 compound="left",
                                                 image=self.__arrow_image,
                                                 command=self.__go_back_loginscreen)
        to_back_button.place(x=27, y=41)

        if not Database.database_status():
            username_entry.configure(state="readonly", fg_color=LIGHT_GRAY_COLOR, border_color=WHITE_COLOR)
            self.__password_entry.configure(state="readonly", fg_color=LIGHT_GRAY_COLOR, border_color=WHITE_COLOR)
            email_entry.configure(state="readonly", fg_color=LIGHT_GRAY_COLOR, border_color=WHITE_COLOR)
            signup_button.configure(state="disabled", fg_color=LIGHT_BLUE_COLOR)
            self.__status_password_button.destroy()
            
            messagebox.showerror("Connection", "Can't register. Database connection failed.")

    def __show_password(self) -> None:
        if self.__hide_password:
            self.__status_password_button.configure(image=self.__showpassword_image)
            self.__password_entry.configure(show="")
            self.__hide_password = False
        else:
            self.__status_password_button.configure(image=self.__hidepassword_image)
            self.__password_entry.configure(show="*")
            self.__hide_password = True

    def __save_connection_settings(self) -> None:
        if self.__user_entry.get() != "": 
            try: 
                with open("./database/config.json") as file:
                    data = json.load(file)
                    data["user"] = self.__user_entry.get()
                    data["password"] = self.__password_entry.get()
                    data["host"] = self.__host_entry.get()
                    data["port"] = self.__port_entry.get()

                with open("./database/config.json", "w") as file:
                    json.dump(data, file, indent=4)
                    file.write("\n")
            except FileNotFoundError as error:
                messagebox.showerror("Error!", f"file or directory does not exist:\ndatabase/config.json\n{error}")
            except Exception as error:
                messagebox.showerror("Error!", error)
            else:
                self.__setup_connection_ui()
                Database().connect_to_database(database=None)

    def __login(self, username, password) -> None:
        if token := LoginDb(username=username, password=password).process_login():
            SidebarUI(root=self, token=token)

    def __go_back_loginscreen(self) -> None:
        clear_frames(self.__frame_three)
        clear_frames(self.__frame_four)

        self.after(10, lambda:self.__frame_three.configure(width=458, height=350))
        self.after(10, lambda:self.__frame_three.place(x=33, y=18))
        
        self.after(10, lambda:self.__frame_four.configure(width=458, height=220))
        self.after(10, lambda:self.__frame_four.place(x=33, y=388))

        self.__login_ui()
