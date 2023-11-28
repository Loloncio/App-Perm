# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Controller.FirmadasContr import FirmadasContr

class VistaFirmadas(ctk.CTkToplevel):
    controlador = FirmadasContr()

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
        self.title("Apps firmadas")

        # Fuente que usaremos en esta vista
        tittleFont = ctk.CTkFont(family="Inter", size=30, weight="normal")
        buttonFont = ctk.CTkFont(family="Inter", size=20, weight="normal")
        infoFont = ctk.CTkFont(family="Inter", size=15, weight="normal")

        titulo = ctk.CTkLabel(self, text="Apps firmadas", text_color="white", font=tittleFont, pady=40)

        frameBotonesUp = ctk.CTkFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.width-10, height=40);
        frameBotonesDown = ctk.CTkFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.width-10, height=40);
        frameSalida = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius= 10,width = ((self.width)-40),height=self.height-300);
        self.salida = ctk.CTkLabel(frameSalida, text="", text_color="white", font=infoFont, pady=60)
        # Creación del botón para volver al menu principal
        instDang = ctk.CTkButton(frameBotonesUp, command=self.instalaDangerous, text="Instalar apps firmadas dangerous", font=buttonFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)
        # Creación del botón para volver al menu principal
        isntSign = ctk.CTkButton(frameBotonesUp, command=self.instalaSignature, text="Instalar apps firmadas signature", font=buttonFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)
        # Creación del botón para volver al menu principal
        testFirma = ctk.CTkButton(frameBotonesDown, command=self.testFirma, text="Comprobar firmas", font=buttonFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)
        # Creación del botón para volver al menu principal
        volver = ctk.CTkButton(frameBotonesDown, command=self.volver, text="Volver", font=buttonFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)
        # Cuando se modifique el tamaño de la ventana se llama al método que reajusta los elementos
        self.bind("<Configure>", lambda event, self=self, textFrame=frameSalida, botonFirmas=testFirma: self.ajustarTamanos(self,textFrame, botonFirmas))
        titulo.pack()
        frameBotonesUp.pack()
        instDang.grid(column = 0, row = 0,pady= 10, padx=50,sticky="W")
        isntSign.grid(column=1, row = 0,pady= 10, padx=50,sticky="E")
        frameSalida.pack(pady=20)
        self.salida.pack()
        frameBotonesDown.pack(fill="x")
        volver.grid(column = 0, row = 0,pady= 10, padx=20, sticky="W")
        testFirma.grid(column = 1, row = 0,pady= 10,padx=self.width-380, sticky="E")

    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)

    def instalaDangerous(self):
        salida = self.controlador.instalaDangerous()
        if salida[1] != "":
            self.salida.configure(text = salida[1], text_color="red")
        else:
            self.salida.configure(text = salida[0], text_color="white")
        return
    def instalaSignature(self):
        salida = self.controlador.isntalaSignature()
        if salida[1] != "":
            self.salida.configure(text = salida[1], text_color="red")
        else:
            self.salida.configure(text = salida[0], text_color="white")
    def testFirma(self):
        salida = self.controlador.testFirmadas()
        if salida[1] != "":
            self.salida.configure(text = salida[1], text_color="red")
        else:
            self.salida.configure(text = salida[0], text_color="white")
        return
    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, textFrame, botonFirmas):
        anchoVentana = self.winfo_width()
        altoVentana = self.winfo_height()
        # Si se ha generado un evento configure (como hacer scroll) pero no cambia el tamaño de pantalla,
        # no hacemos nada.
        if(self.height != altoVentana or self.width != anchoVentana):
            self.height = altoVentana
            self.width = anchoVentana
            textFrame.configure(width = ((self.width)-40),height=self.height-300)
            botonFirmas.grid(column = 1, row = 0,pady= 10, sticky="E",padx=self.width-380)
            # Actualiza la ventana
            self.update_idletasks()