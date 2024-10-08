from tkinter import messagebox

def empty_entries(**kwargs) -> bool:
    total_emptyentries = [key for key, value in kwargs.items() if not value]
    
    if len(total_emptyentries) == 1:
        messagebox.showerror(title="Required Field", message=f"Please fill out this field: {total_emptyentries[0].strip()}.")

    elif total_emptyentries:
        messagebox.showerror(title="Required Fields", message=f"Please fill in all required\nfields: {', '.join(total_emptyentries).strip()}.")

    return bool(total_emptyentries)
