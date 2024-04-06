import customtkinter
from utils.clear_frames import clear_frames

class Ui_panel:
    def __init__(self, root: customtkinter.CTk):
        self.root = root
        
        clear_frames(self.root)        
        self.root.geometry("1920x1012-8-2")
