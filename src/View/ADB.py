import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)

import tkinter as tk
import customtkinter as ctk
from Controller.DefectoContr import ControladorDef

class defecto(ctk.CTkToplevel):
    # Algunas variables globales para los parametros que pasaremos a la siguiente vista,
    # la opción que se ha seleccionado y una etiqueta de errores
    HEIGHT = 720
    WIDTH = 1280
    controlador = ControladorDef()
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Permisos del dispositivo")

        # Fuente que usaremos en esta vista
        leftFont = ctk.CTkFont(family="Inter", size=20, weight="normal")
        rightFont = ctk.CTkFont(family="Inter", size=15, weight="normal")
        
    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)