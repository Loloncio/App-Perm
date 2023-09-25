import tkinter as tk
import customtkinter as ctk
from Menu import mainWindow


if __name__ == "__main__":
    # Creación de ventana principal
    root = ctk.CTk()
    root.geometry("1280x720")
    root.minsize(width=1280,height=720)
    root.title("App-Perm")
    mainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()