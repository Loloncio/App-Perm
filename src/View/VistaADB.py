import os
import sys
import ctypes

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)


import customtkinter as ctk
from Controller.ADBContr import ADBContr
import time

class VistaADB(ctk.CTkToplevel):
    controlador = ADBContr()
    def __init__(self, parent, geometry, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.height = 720
        self.width = 1280
        self.updated = time.time()
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0)/100
        self.geometry(""+str(geometry[0]//scale_factor)+"x"+str(geometry[1]//scale_factor)+"+"+str(geometry[2])+"+"+str(geometry[3]))
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Permisos del dispositivo")

        # Fuente que usaremos en esta vista
        tittleFont = ctk.CTkFont(family="Inter", size=30, weight="normal")
        textFont = ctk.CTkFont(family="Inter", size=20, weight="normal")

        titulo = ctk.CTkLabel(self, text="Permisos del dispositivo", text_color="white",
                                corner_radius=10, justify="center", font=tittleFont, height=100)
        frameTexto = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius= 10,width = self.width-40, height=self.height-200)
        frameInferior = ctk.CTkFrame(master=self, corner_radius=10, width = self.width-10, fg_color = "#1E1E1E", height=100)
        volver = ctk.CTkButton(frameInferior, command=self.volver, text="Menu", font=textFont, corner_radius=10,
                                fg_color="#504F4F", text_color="white", height=40)
        permisos = ctk.CTkLabel(frameTexto, text="", text_color="white", fg_color="#504F4F",
                                corner_radius=10, justify="center", font=textFont)
        ejecutar = ctk.CTkButton(frameInferior, command=lambda texto = permisos:
                                self.ejecutar(texto)
                                , text="Ejecutar adb", font=textFont, corner_radius=10,
                                fg_color="#504F4F", text_color="white", height=40)
        info = ctk.CTkLabel(frameInferior, corner_radius=10, justify="center", font=textFont, wraplength=self.width- 400,
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
            texto.configure(text=mensaje[0], anchor="w", text_color="white")
        else:
            texto.configure(text=mensaje[1], text_color="red")

    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, frame):
        if(time.time()- self.updated > 0.5 ):
            scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0)/100
            anchoVentana = self.winfo_width()//scale_factor  # Ancho de la ventana
            altoVentana = self.winfo_height()//scale_factor  # Alto de la ventana
            if(self.height != altoVentana or self.width != anchoVentana):
                self.height = altoVentana
                self.width = anchoVentana
                frame.configure(width = self.width-40, height=self.height-200)
            self.updated = time.time()