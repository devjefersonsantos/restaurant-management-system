import customtkinter
from PIL import Image
from utils.clear_frames import clear_frames
import json
from tkinter import messagebox
from database.database import Database
from database.db_signup import DbSignup

class UiLogin(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # https://pixabay.com/vectors/icon-smile-smilie-feedback-logo-4399618/
        self.iconbitmap("images/global_images/icon.ico")
        self.title("Restaurant Management System")
        self.geometry("1050x625+425+199")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("light")

        self.main_frame = customtkinter.CTkFrame(master=self)
        self.main_frame.pack()

        self.frame_one = customtkinter.CTkFrame(master=self.main_frame, 
                                                fg_color="#ffc83d",
                                                bg_color="#ffc83d")
        self.frame_one.grid(row=0, column=0)

        self.frame_two = customtkinter.CTkFrame(master=self.main_frame,
                                                width=526, height=626,
                                                fg_color="#e3e3e3",
                                                bg_color="#e3e3e3")
        self.frame_two.grid(row=0, column=1)

        self.frame_three = customtkinter.CTkFrame(master=self.frame_two,
                                                  width=458, height=350,
                                                  fg_color="#ffffff",
                                                  corner_radius=10)
        self.frame_three.place(x=33, y=18)

        self.frame_four = customtkinter.CTkFrame(master=self.frame_two,
                                                 width=458, height=220,  
                                                 fg_color="#ffffff",
                                                 corner_radius=10)
        self.frame_four.place(x=33, y=388)

        self.ui_images()
        self.ui_widgets()
    
    def ui_images(self):
        # https://pixabay.com/illustrations/chef-food-kitchen-restaurant-adult-2410818/
        chefpil_image = Image.open("images/login_images/chef.png")
        self.chef_image = customtkinter.CTkImage(dark_image=chefpil_image,
                                                 light_image=chefpil_image, 
                                                 size=(480, 500))
    
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        userpil_image = Image.open("images/login_images/user.png")
        self.user_image = customtkinter.CTkImage(dark_image=userpil_image,
                                                 light_image=userpil_image,
                                                 size=(32,32))

        passwordpil_image = Image.open("images/login_images/password.png")
        self.password_image = customtkinter.CTkImage(dark_image=passwordpil_image,
                                                     light_image=passwordpil_image,
                                                     size=(32,32))
        
        hostpil_image = Image.open("images/login_images/host.png")
        self.host_image = customtkinter.CTkImage(dark_image=hostpil_image,
                                                 light_image=hostpil_image,
                                                 size=(32,32))
        
        emailpil_image = Image.open("images/login_images/email.png")
        self.email_image = customtkinter.CTkImage(dark_image=emailpil_image,
                                                  light_image=emailpil_image,
                                                  size=(33,33))
        
        keypasswordpil_image = Image.open("images/login_images/keypassword.png")
        self.keypassword_image = customtkinter.CTkImage(dark_image=keypasswordpil_image,
                                                        light_image=keypasswordpil_image,
                                                        size=(32,32))
        
        # https://pixabay.com/vectors/arrow-left-gray-back-computer-23255/
        arrowpil_image = Image.open("images/login_images/arrow.png")
        self.arrow_image = customtkinter.CTkImage(dark_image=arrowpil_image,
                                                  light_image=arrowpil_image,
                                                  size=(15,15))
        
        # https://pixabay.com/vectors/eye-see-viewing-icon-1103592/
        showpasswordpil_image = Image.open("images/login_images/showpassword.png")
        self.showpassword_image = customtkinter.CTkImage(dark_image=showpasswordpil_image,
                                                         light_image=showpasswordpil_image,
                                                         size=(25,15))

        hidepasswordpil_image = Image.open("images/login_images/hidepassword.png")
        self.hidepassword_image = customtkinter.CTkImage(dark_image=hidepasswordpil_image,
                                                         light_image=hidepasswordpil_image,
                                                         size=(25,15))

        # https://pixabay.com/vectors/ok-check-to-do-agenda-icon-symbol-1976099/
        loggedpil_image = Image.open("images/login_images/logged.png")
        self.logged_image = customtkinter.CTkImage(dark_image=loggedpil_image,
                                                   light_image=loggedpil_image,
                                                   size=(45,45))
        
        # https://pixabay.com/vectors/false-error-is-missing-absent-x-2061131/
        loggedoutpil_image = Image.open("images/login_images/loggedout.png")
        self.loggedout_image = customtkinter.CTkImage(dark_image=loggedoutpil_image,
                                                      light_image=loggedoutpil_image,
                                                      size=(45,45)) 

    def ui_widgets(self):
        chef_label = customtkinter.CTkLabel(master=self.frame_one, 
                                            corner_radius=0,
                                            text="", 
                                            image=self.chef_image)
        chef_label.grid(row=0, column=0, padx=22, pady=64)

        username_label = customtkinter.CTkLabel(master=self.frame_three,
                                                font=("arial", 15),
                                                text="  Username:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self.user_image)
        username_label.place(x=27, y=40)

        __username_entry = customtkinter.CTkEntry(master=self.frame_three, 
                                                  width=400, height=40,
                                                  font=("arial", 17),
                                                  fg_color="#EEEEEE",
                                                  border_color="#e3e3e3",
                                                  border_width=1)
        __username_entry.place(x=27, y=90)

        password_label = customtkinter.CTkLabel(master=self.frame_three,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self.password_image)
        password_label.place(x=27, y=147)

        self.__password_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=197)

        self.statuspassword_button = customtkinter.CTkButton(master=self.frame_three,
                                                             width=1, height=1, 
                                                             image=self.hidepassword_image, 
                                                             fg_color="#EEEEEE",
                                                             bg_color="#EEEEEE",
                                                             hover_color="#EEEEEE", 
                                                             text=None,
                                                             command=self.show_password)
        self.statuspassword_button.place(x=380, y=205)

        self.__hide_password = True

        login_button = customtkinter.CTkButton(master=self.frame_three,
                                               width=400, height=40, 
                                               fg_color="#2b8dfc", 
                                               hover_color="#4da0ff",
                                               text_color="#ffffff",
                                               text="Log in")
        login_button.place(x=27, y=275)

        setupconnection_label = customtkinter.CTkLabel(master=self.frame_four,
                                                       font=("arial", 15),
                                                       text="MySQL Connection:",
                                                       text_color="#2e2e2e")
        setupconnection_label.place(x=27, y=20)

        setupconnection_button = customtkinter.CTkButton(master=self.frame_four,
                                                         width=400, height=40, 
                                                         fg_color="#fa9725",
                                                         hover_color="#f5a447", 
                                                         text_color="#ffffff", 
                                                         text="Setup Connection",
                                                         command=self.ui_setup_connection)
        setupconnection_button.place(x=27, y=55)

        createacc_label = customtkinter.CTkLabel(master=self.frame_four,
                                                 font=("arial", 15),
                                                 text="Don't have an account?",
                                                 text_color="#2e2e2e")
        createacc_label.place(x=27, y=106)

        createacc_button = customtkinter.CTkButton(master=self.frame_four,
                                                   width=400, height=40, 
                                                   fg_color="#4bb34b", 
                                                   hover_color="#61bc61",
                                                   text_color="#ffffff", 
                                                   text="Sign up",
                                                   command=self.ui_signup)
        createacc_button.place(x=27, y=141)

    def ui_setup_connection(self):
        clear_frames(self.frame_three)
        clear_frames(self.frame_four)

        self.after(10, lambda:self.frame_three.configure(width=458, height=450))
        self.after(10, lambda:self.frame_three.place(x=33, y=20))

        self.after(10, lambda:self.frame_four.configure(width=458, height=120))
        self.after(10, lambda:self.frame_four.place(x=33, y=488))

        if Database.db_status():
            self.databasestatus_image = customtkinter.CTkLabel(self.frame_three, text="", image=self.logged_image)
            self.databasestatus_image.place(x=400, y=10)
        else:
            self.databasestatus_image = customtkinter.CTkLabel(self.frame_three, text="", image=self.loggedout_image)
            self.databasestatus_image.place(x=400, y=10)

        host_label = customtkinter.CTkLabel(master=self.frame_three,
                                            font=("arial", 15),
                                            text="  Host:",
                                            compound="left",
                                            text_color="#2e2e2e",
                                            image=self.host_image)
        host_label.place(x=27, y=40)

        self.__host_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                   width=400, height=40,
                                                   font=("arial", 17), 
                                                   fg_color="#EEEEEE", 
                                                   border_color="#e3e3e3", 
                                                   border_width=1)
        self.__host_entry.place(x=27, y=90)

        username_label = customtkinter.CTkLabel(master=self.frame_three,
                                                font=("arial", 15),
                                                text="  User:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self.user_image)
        username_label.place(x=27, y=147)

        self.__username_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1)
        self.__username_entry.place(x=27, y=197)

        password_label = customtkinter.CTkLabel(master=self.frame_three,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self.keypassword_image)
        password_label.place(x=27, y=254)

        self.__password_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=304)

        self.__hide_password = True

        self.statuspassword_button = customtkinter.CTkButton(master=self.frame_three,
                                                             width=1, height=1, 
                                                             image=self.hidepassword_image, 
                                                             fg_color="#EEEEEE",
                                                             bg_color="#EEEEEE",
                                                             hover_color="#EEEEEE", 
                                                             text="",
                                                             command=self.show_password)
        self.statuspassword_button.place(x=380, y=312)

        savechanges_button = customtkinter.CTkButton(master=self.frame_three,
                                                     width=400, height=40, 
                                                     fg_color="#0077ff", 
                                                     hover_color="#1f88ff",
                                                     text_color="#ffffff", 
                                                     text="Save Changes",
                                                     command=self.save_connection_settings)
        savechanges_button.place(x=27, y=380)

        goback_button = customtkinter.CTkButton(master=self.frame_four, 
                                                width=400, height=40,
                                                fg_color="#5c5c5c",
                                                hover_color="#6e6e6e", 
                                                text_color="#ffffff", 
                                                text="Go back",
                                                compound="left",
                                                image=self.arrow_image,
                                                command=self.go_back_loginscreen)
        goback_button.place(x=27, y=41)

        try:
            with open("database/config.json") as file:
                __data = json.load(file)
                self.__host_entry.configure(placeholder_text=__data["host"])
                self.__username_entry.configure(placeholder_text=__data["user"])
                self.__password_entry.configure(placeholder_text= "*" * len(__data["password"]))
        except:
            self.__host_entry.configure(placeholder_text="")
            self.__username_entry.configure(placeholder_text="")
            self.__password_entry.configure(placeholder_text="")
            
            config_messagebox = {"icon": "error","type": "yesno"}
            modal = messagebox.showerror("database/config.json", "Error in the database configuration file.\nRestore file?", **config_messagebox)
            
            if modal == "yes":
                __data = {"host": "localhost","user": "root","password": ""}
                with open("database/config.json", "w") as __file:
                    json.dump(__data, __file, indent=4)
                    __file.write("\n")
                self.ui_setup_connection()

    def ui_signup(self):
        clear_frames(self.frame_three)
        clear_frames(self.frame_four)

        self.after(10, lambda:self.frame_three.configure(width=458, height=450))
        self.after(10, lambda:self.frame_three.place(x=33, y=20))
        
        self.after(10, lambda:self.frame_four.configure(width=458, height=120))
        self.after(10, lambda:self.frame_four.place(x=33, y=488))

        user_label = customtkinter.CTkLabel(master=self.frame_three,
                                            font=("arial", 15),
                                            text="  Username:",
                                            compound="left",
                                            text_color="#2e2e2e",
                                            image=self.user_image)
        user_label.place(x=27, y=40)
        
        __username_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                  width=400, height=40,
                                                  font=("arial", 17), 
                                                  fg_color="#EEEEEE", 
                                                  border_color="#e3e3e3", 
                                                  border_width=1)
        __username_entry.place(x=27, y=90)
        
        password_label = customtkinter.CTkLabel(master=self.frame_three,
                                                font=("arial", 15),
                                                text="  Password:",
                                                compound="left",
                                                text_color="#2e2e2e",
                                                image=self.keypassword_image)
        password_label.place(x=27, y=147)

        self.__password_entry = customtkinter.CTkEntry(master=self.frame_three, 
                                                       width=400, height=40,
                                                       font=("arial", 17), 
                                                       fg_color="#EEEEEE", 
                                                       border_color="#e3e3e3", 
                                                       border_width=1,
                                                       show="*")
        self.__password_entry.place(x=27, y=197)

        self.__hide_password = True

        self.statuspassword_button = customtkinter.CTkButton(master=self.frame_three,
                                                             width=1, height=1, 
                                                             image=self.hidepassword_image, 
                                                             fg_color="#EEEEEE",
                                                             bg_color="#EEEEEE",
                                                             hover_color="#EEEEEE", 
                                                             text="",
                                                             command=self.show_password)
        self.statuspassword_button.place(x=380, y=205)
   
        email_label = customtkinter.CTkLabel(master=self.frame_three,
                                             font=("arial", 15),
                                             text="  Email:",
                                             compound="left",
                                             text_color="#2e2e2e",
                                             image=self.email_image)
        email_label.place(x=27, y=254)

        __email_entry = customtkinter.CTkEntry(master=self.frame_three,
                                               width=400, height=40,
                                               font=("arial", 17), 
                                               fg_color="#EEEEEE", 
                                               border_color="#e3e3e3", 
                                               border_width=1)
        __email_entry.place(x=27, y=304)

        signup_button = customtkinter.CTkButton(master=self.frame_three, 
                                                width=400, height=40,
                                                fg_color="#0077ff", 
                                                hover_color="#1f88ff",
                                                text_color="#ffffff",
                                                text="Sign up",
                                                command=lambda:DbSignup(username=__username_entry.get(),
                                                                        password=self.__password_entry.get(),
                                                                        email=__email_entry.get()))
        signup_button.place(x=27, y=380)

        goback_button = customtkinter.CTkButton(master=self.frame_four,
                                                width=400, height=40, 
                                                fg_color="#5c5c5c",
                                                hover_color="#6e6e6e", 
                                                text_color="#ffffff",
                                                text="Go back",
                                                compound="left",
                                                image=self.arrow_image,
                                                command=self.go_back_loginscreen)
        goback_button.place(x=27, y=41)

        if not Database.db_status():
            __username_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            self.__password_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            __email_entry.configure(state="readonly", fg_color="#e3e3e3", border_color="#ffffff")
            signup_button.configure(state="disabled", fg_color="#429aff")
            self.statuspassword_button.destroy()
            
            messagebox.showerror("Connection", "Can't register. Database connection failed.")

    def show_password(self):
        if self.__hide_password:
            self.statuspassword_button.configure(image=self.showpassword_image)
            self.__password_entry.configure(show="")
            self.__hide_password = False
        else:
            self.statuspassword_button.configure(image=self.hidepassword_image)
            self.__password_entry.configure(show="*")
            self.__hide_password = True

    def save_connection_settings(self):
        if self.__username_entry.get() != "": 
            try: 
                with open("database/config.json") as __file:
                    __data = json.load(__file)
                    __data["host"] = self.__host_entry.get()
                    __data["user"] = self.__username_entry.get()
                    __data["password"] = self.__password_entry.get()

                with open("database/config.json", "w") as __file:
                    json.dump(__data, __file, indent=4)
                    __file.write("\n")
            except FileNotFoundError as error:
                messagebox.showerror("Error!", f"file or directory does not exist:\ndatabase/config.json\n {error}")
            except Exception as error:
                messagebox.showerror("Error!", error)
            else:
                self.ui_setup_connection()
                Database().connect_to_database()

    def go_back_loginscreen(self):
        clear_frames(self.frame_three)
        clear_frames(self.frame_four)

        self.after(10, lambda:self.frame_three.configure(width=458, height=350))
        self.after(10, lambda:self.frame_three.place(x=33, y=20))
        
        self.after(10, lambda:self.frame_four.configure(width=458, height=220))
        self.after(10, lambda:self.frame_four.place(x=33, y=388))

        self.ui_widgets()
