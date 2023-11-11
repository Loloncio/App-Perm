# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Controller.AyudaContr import AyudaContr

class ayuda(ctk.CTkToplevel):
    HEIGHT = 720
    WIDTH = 1280
    controlador = AyudaContr()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Apps firmadas")

        secciones = {"Permisos según la web":"En esta sección..."
                     ,"Modificación de permisos":"x",
                     "Permisos del dispositivo":"x",
                     "Aplicaciones firmadas":"x"}
        seccionesKeys = list(secciones.keys())
        # Fuente que usaremos en esta vista
        tittleFont = ctk.CTkFont(family="Inter", size=40, weight="normal")
        sectionFont = ctk.CTkFont(family="Inter", size=25, weight="normal")
        textFont = ctk.CTkFont(family="Inter", size=20, weight="normal")

        titulo = ctk.CTkLabel(self, text="Apps firmadas", text_color="white", font=tittleFont, pady=20)
        frameMain = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.WIDTH-10, height=self.HEIGHT-180);
        for i in range(4):
            frameSeccion = ctk.CTkFrame(frameMain,fg_color="#D9D9D9", corner_radius= 10,width = ((self.WIDTH)-40),height=self.HEIGHT-300);
            tituloSeccion = ctk.CTkLabel(frameSeccion, text=seccionesKeys[i], corner_radius= 10,text_color="black", font=sectionFont, pady=10, anchor="center")
            textoSeccion = ctk.CTkLabel(frameSeccion, text=secciones.get(seccionesKeys[i]), corner_radius= 10,text_color="black", font=textFont, pady=10)
            secciones[seccionesKeys[i]]=[frameSeccion, tituloSeccion, textoSeccion]

        # Creación del botón para volver al menu principal
        volver = ctk.CTkButton(self, command=self.volver, text="Volver", font=textFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)
        titulo.pack()
        frameMain.pack(pady=10)
        for i in range(4):
            print(seccionesKeys[i])
            elementos = secciones.get(seccionesKeys[i])
            elementos[0].pack(fill="x", padx=20, pady=10)
            elementos[1].grid(column=0,row = 0, pady=5,padx=5,sticky="we")
            elementos[2].grid(column=0,row=1, padx=5, sticky="nw")
        volver.pack(padx=10,pady=10,side="left")
        # Cuando se modifique el tamaño de la ventana se llama al método que reajusta los elementos
        self.bind("<Configure>", lambda event, self=self, mainFrame=frameMain:
            self.ajustarTamanos(self,mainFrame))

    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)
    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, mainFrame):
        anchoVentana = self.winfo_width()
        altoVentana = self.winfo_height()
        # Si se ha generado un evento configure (como hacer scroll) pero no cambia el tamaño de pantalla,
        # no hacemos nada.
        if(self.HEIGHT != altoVentana or self.WIDTH != anchoVentana):
            self.HEIGHT = altoVentana
            self.WIDTH = anchoVentana
            mainFrame.configure(height=self.HEIGHT-180, width=self.WIDTH-10)
            # Actualiza la ventana
            self.update_idletasks()