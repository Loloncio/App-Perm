# Última vista de App-Perm, aquí vemos el progreso de creación de AndroidManifest.xml
# su compilación, instalación y, finalmente, el resultado de dicha instlación.
# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk

class final(ctk.CTkToplevel):

    def __init__(self, parent, opt, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)