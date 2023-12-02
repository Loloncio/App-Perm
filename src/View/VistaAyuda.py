# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Controller.AyudaContr import AyudaContr

class VistaAyuda(ctk.CTkToplevel):
    controlador = AyudaContr()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.height = 720
        self.width = 1280
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Ayuda")

        # Fuente que se usará en la app, tamaños para título y texto
        tittleFont = ctk.CTkFont(family="Inter", size=40, weight="bold")
        headerFont = ctk.CTkFont(family="Inter", size=25, weight="bold")
        textFont = ctk.CTkFont(family="Inter", size=15, weight="normal")

        titulo = ctk.CTkLabel(self, text="Ayuda", text_color="white", font=tittleFont, pady=40)
        frameMain = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius= 10,
                                           width = ((self.width)-40), height=(self.height-200));

        elementos = self.controlador.getTutorial()
        labels = []
        images = []
        for elemento in elementos:
            tipo = elemento[1]
            if tipo == 1:
                labels.append(ctk.CTkLabel(frameMain, text=elemento[0], text_color="white", font=textFont,
                                           wraplength=self.width-50, anchor="w", justify="left"))
                labels[-1].pack(fill="x")
            elif tipo == 2:
                labels.append(ctk.CTkLabel(frameMain, text=elemento[0], text_color="white", font=headerFont,
                                           wraplength=self.width-50, anchor="w", justify="left"))
                labels[-1].pack(fill="x")
            elif tipo == 3:
                imagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../assets/"+elemento[0][:-1:])
                my_image = ctk.CTkImage(light_image=Image.open(imagePath),
                                  size=(711, 400))
                images.append(my_image)
                ctk.CTkLabel(frameMain, image=my_image, text="").pack()
                continue

        titulo.pack()
        frameMain.pack(padx=10)
        volver = ctk.CTkButton(self, command=self.volver, text="Volver", font=textFont, corner_radius=10,
                                fg_color="#D9D9D9", text_color="black", height=40)
        volver.pack(anchor = "w", side="left", padx = 10, pady = 10)
        self.bind("<Configure>", lambda event, self=self, mainFrame=frameMain, labels = labels, imagenes = images: self.ajustarTamanos(self,mainFrame, labels, imagenes))

    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)
    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, mainFrame, labels, images):
        anchoVentana = self.winfo_width()
        altoVentana = self.winfo_height()
        print("ancho: ", anchoVentana)
        print("alto: ", altoVentana)
        # Si se ha generado un evento configure (como hacer scroll) pero no cambia el tamaño de pantalla,
        # no hacemos nada.
        if(self.height != altoVentana or self.width != anchoVentana):
            self.height = altoVentana
            self.width = anchoVentana
            mainFrame.configure(height=self.height-300, width=self.width-40)
            for label in labels:
                label.configure(wraplength=self.width-50)
            for imagen in images:
                h = self.height-320
                w = h*1.77777
                imagen.configure(size = (w, h))
            # Actualiza la ventana
            self.update_idletasks()