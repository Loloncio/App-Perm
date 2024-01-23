# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Controller.ComparaContr import ComparaContr

class VistaFirmadas(ctk.CTkToplevel):
    controlador = ComparaContr()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.height = 720
        self.width = 1280
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Comparar grupos")

        # Fuente que usaremos en esta vista
        tittleFont = ctk.CTkFont(family="Inter", size=30, weight="normal")
        buttonFont = ctk.CTkFont(family="Inter", size=20, weight="normal")
        infoFont = ctk.CTkFont(family="Inter", size=15, weight="normal")

        titulo = ctk.CTkLabel(self, text="Apps firmadas", text_color="white", font=tittleFont, pady=40)

        frameBotonesDown = ctk.CTkFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.width-10, height=40);
        frameSalida = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius= 10,width = ((self.width)-40),height=self.height-300);
        self.salida = ctk.CTkLabel(frameSalida, text="", text_color="white", font=infoFont, pady=60)
        # Creación del botón para comparar permisos
        compruebaPermisos = ctk.CTkButton(frameBotonesDown, command=self.comparaGrupos, text="Comprobar firmas", font=buttonFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)
        # Creación del botón para volver al menu principal
        volver = ctk.CTkButton(frameBotonesDown, command=self.volver, text="Volver", font=buttonFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)

        titulo.pack()
        frameSalida.pack(pady=20)
        self.salida.pack()
        frameBotonesDown.pack(fill="x")
        volver.grid(column = 0, row = 0,pady= 10, padx=20, sticky="W")
        compruebaPermisos.grid(column = 1, row = 0,pady= 10,padx=self.width-380, sticky="E")

    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)
    def descargaCSV(self):
        self.controlador.getCSV()
    def comparaGrupos(self):
        comparacion = self.controlador.comparaGrupos()
        if comparacion[1] != "":
            self.salida.configure(text = comparacion[1], text_color="red")
        else:
            self.salida.configure(text = comparacion[0], text_color="white")
        return