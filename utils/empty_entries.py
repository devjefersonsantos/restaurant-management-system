from tkinter import messagebox

def empty_entries(**kwargs) -> bool:
    total_emptyentries = [key for key, value in kwargs.items() if not value]
    
    if len(total_emptyentries) == 1:
        messagebox.showerror(title=None, message=f"These fields are required: {', '.join(total_emptyentries)}.")
        return True
    elif total_emptyentries:
        messagebox.showerror(title=None, message=f"Please fill out all required\nfields: {', '.join(total_emptyentries)}.")
        return True
