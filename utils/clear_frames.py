import customtkinter

def clear_frames(frames:customtkinter.CTkFrame) -> None: 
    for frame in frames.winfo_children():
        frame.destroy()
