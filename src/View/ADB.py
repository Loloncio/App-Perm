import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)

import tkinter as tk
import customtkinter as ctk
from Controller.ADBContr import ControladorADB

class adb(ctk.CTkToplevel):
    # Algunas variables globales para los parametros que pasaremos a la siguiente vista,
    # la opción que se ha seleccionado y una etiqueta de errores
    HEIGHT = 720
    WIDTH = 1280
    controlador = ControladorADB()
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
        tittleFont = ctk.CTkFont(family="Inter", size=30, weight="normal")
        textFont = ctk.CTkFont(family="Inter", size=20, weight="normal")

        titulo = ctk.CTkLabel(self, text="Permisos del dispositivo", text_color="white",
                                corner_radius=10, justify="center", font=tittleFont, height=100)
        frameTexto = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius= 10,width = self.WIDTH-40, height=self.HEIGHT-200)
        frameInferior = ctk.CTkFrame(master=self, corner_radius=10, width = self.WIDTH-10, fg_color = "#1E1E1E", height=100)
        volver = ctk.CTkButton(frameInferior, command=self.volver, text="Menu", font=textFont, corner_radius=10,
                                fg_color="#504F4F", text_color="white", height=40)
        permisos = ctk.CTkLabel(frameTexto, text="", text_color="white", fg_color="#504F4F",
                                corner_radius=10, justify="center", font=textFont)
        ejecutar = ctk.CTkButton(frameInferior, command=lambda texto = permisos:
                                self.ejecutar(texto)
                                , text="Ejecutar adb", font=textFont, corner_radius=10,
                                fg_color="#504F4F", text_color="white", height=40)
        info = ctk.CTkLabel(frameInferior, corner_radius=10, justify="center", font=textFont, wraplength=self.WIDTH- 400,
                            text="Conecta un dispositivo con depuración USB activada y pulsa el boton para ver los permisos disponibles en el dispositivo", text_color="white",
                            )
        titulo.pack()
        frameTexto.pack(padx = 20)
        frameInferior.pack(pady = 10)
        volver.grid(column=0, row=0, padx = 5)
        ejecutar.grid(column=3, row=0, padx = 5)
        info.grid(column=2, row=0, padx = 5)
        permisos.pack(anchor="nw", pady=10)

        self.bind("<Configure>", lambda event, frame=frameTexto, self=self: self.ajustarTamanos(self, frame))

    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)

    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)

    def ejecutar(self, texto):
        mensaje = self.controlador.ejecutar()
        if mensaje[1] == "":
            texto.configure(text=mensaje[0], anchor="nw")
        else:
            texto.configure(text=mensaje[1], text_color="red")

    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, frame):
        anchoVentana = self.winfo_width()  # Ancho de la ventana
        altoVentana = self.winfo_height()  # Alto de la ventana
        if(self.HEIGHT != altoVentana or self.WIDTH != anchoVentana):
            self.HEIGHT = altoVentana
            self.WIDTH = anchoVentana
            frame.configure(width = self.WIDTH-40, height=self.HEIGHT-200)
            # Actualiza la ventana
            self.update_idletasks()