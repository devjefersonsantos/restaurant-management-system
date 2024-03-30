import customtkinter
from PIL import Image

class Ui_login(customtkinter.CTk):
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
        self.chefpil_image = Image.open("images/login_images/chef.png")
        self.chef_image = customtkinter.CTkImage(dark_image=self.chefpil_image,
                                                 light_image=self.chefpil_image, 
                                                 size=(480, 500))
    
        # https://pixabay.com/vectors/icons-icon-set-multimedia-icons-6726119/
        self.userpil_image = Image.open("images/login_images/user.png")
        self.user_image = customtkinter.CTkImage(dark_image=self.userpil_image,
                                                 light_image=self.userpil_image,
                                                 size=(32,32))

        self.passwordpil_image = Image.open("images/login_images/password.png")
        self.password_image = customtkinter.CTkImage(dark_image=self.passwordpil_image,
                                                     light_image=self.passwordpil_image,
                                                     size=(32,32))

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

        __password_entry = customtkinter.CTkEntry(master=self.frame_three,
                                                  width=400, height=40,
                                                  font=("arial", 17), 
                                                  fg_color="#EEEEEE", 
                                                  border_color="#e3e3e3", 
                                                  border_width=1,
                                                  show="*")
        __password_entry.place(x=27, y=197)

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
                                                         text="Setup Connection")
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
                                                   text="Sign up")
        createacc_button.place(x=27, y=141)
