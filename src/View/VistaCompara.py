# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
import os
import sys
import time
import ctypes

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Controller.ComparaContr import ComparaContr

class VistaCompara(ctk.CTkToplevel):
    controlador = ComparaContr()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.height = 720
        self.width = 1280
        self.updated = time.time()
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Comparar grupos")

        instrucciones = 'Para comparar los permisos y grupos de permisos del dispositivo con los de la lista oficial, instale app-perm en su dispositivo, pulse la opción "Permisos" y despues pulse el botón "Compara grupos"'
        # Fuente que usaremos en esta vista
        tittleFont = ctk.CTkFont(family="Inter", size=30, weight="normal")
        buttonFont = ctk.CTkFont(family="Inter", size=20, weight="normal")
        infoFont = ctk.CTkFont(family="Inter", size=15, weight="normal")

        titulo = ctk.CTkLabel(self, text="Compara grupos de permisos", text_color="white", font=tittleFont, pady=40)

        frameBotonesDown = ctk.CTkFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.width-10, height=40);
        frameSalida = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius= 10,width = ((self.width)-40),height=self.height-300);
        self.salida = ctk.CTkLabel(frameSalida, text="", justify="left", wraplength=((self.width)-40), text_color="white", font=infoFont, pady=60)
        # Creación del botón para comparar permisos
        compruebaPermisos = ctk.CTkButton(frameBotonesDown, command=self.comparaGrupos, text="Compara grupos", font=buttonFont, corner_radius=10,
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
        # Cuando se modifique el tamaño de la ventana se llama al método que reajusta los elementos
        self.bind("<Configure>", lambda event, frame = frameSalida, boton = compruebaPermisos,
                  self=self: self.ajustarTamanos(self, frame, boton))

    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)

    def comparaGrupos(self):
        comparacion = self.controlador.comparaGrupos()
        self.salida.configure(text = comparacion, text_color="white")

    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, frame, boton):
        if(time.time()- self.updated > 0.5 ):
            scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0)/100
            anchoVentana = self.winfo_width()//scale_factor  # Ancho de la ventana
            altoVentana = self.winfo_height()//scale_factor  # Alto de la ventana
            # Si se ha generado un evento configure (como hacer scroll) pero no cambia el tamaño de pantalla,
            # no hacemos nada.
            if(self.height != altoVentana or self.width != anchoVentana):
                self.height = altoVentana
                self.width = anchoVentana
                frame.configure(width = ((self.width)-40),height=self.height-300)
                self.salida.configure(wraplength=((self.width)-40))
                boton.grid(column = 1, row = 0,pady= 10,padx=self.width-380, sticky="E")
            self.updated = time.time()