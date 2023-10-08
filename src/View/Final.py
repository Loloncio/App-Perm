# Última vista de App-Perm, aquí vemos el progreso de creación de AndroidManifest.xml
# su compilación, instalación y, finalmente, el resultado de dicha instlación.
# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import time
import sys
import threading
PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Controller.FinalContr import FinalContr

class final(ctk.CTkToplevel):
    DONE = False
    realizando = None
    controlador = FinalContr()
    def __init__(self, parent, opt, permiso, grupos, protection, *args, **kwargs):
        super().__init__(parent.parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.canvas = tk.Canvas(self, width=100, height=100,bg="#1E1E1E", highlightthickness=0)
        self.canvas.pack(anchor="center", pady = 100)
        self.update = self.draw().__next__
        self.after(100, self.update)

        titleFont = ctk.CTkFont(family="Inter", size=30, weight="normal")
        textFont = ctk.CTkFont(family="Inter", size=20, weight="normal")

        opt = int(opt)
        permiso = str(permiso)
        self.realizando = ctk.CTkLabel(self,text_color="white", font= titleFont, corner_radius=10)
        self.realizando.configure(text="Creando archivo AndroidManifest.xml...")
        self.realizando.pack(pady = 50, padx = 30)
        thread = threading.Thread(target=self.compila)

        if(opt == 1):
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            thread.start()
        elif opt == 2:
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            thread.start()
        elif opt == 3:
            protection = str(protection)
            self.creaManifestProtection(permiso, protection)
            thread.start()
        elif opt == 4:
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            thread.start()
        elif opt == 5:
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            thread.start()

        frameBotones = ctk.CTkFrame(self, fg_color="#1E1E1E")
        botonAbrir = ctk.CTkButton(frameBotones, text = "Abrir ruta a apk", command = self.motrarApk, font= textFont, fg_color="#D9D9D9", text_color="black",width = 150, height=60)
        botonInstalar = ctk.CTkButton(frameBotones, text = "Instalar apk",command = self.instalaApk, font = textFont, fg_color="#D9D9D9", text_color="black", width=150, height=60)
        botonVolver = ctk.CTkButton(frameBotones, text="Menu", command = self.volver, font = textFont, fg_color="#D9D9D9", text_color="black", width=150, height=60)
        self.resultado = ctk.CTkLabel(self,text_color="white", text="", font= titleFont, corner_radius=10)

        frameBotones.pack(pady = 10, padx = 10)
        botonVolver.grid(row = 0, column = 0, padx = 10, pady =10)
        botonAbrir.grid(row = 0, column = 1, padx = 10, pady =10)
        botonInstalar.grid(row = 0, column = 2, padx = 10, pady =10)
        self.resultado.pack(pady = 50, padx = 30)
    def cerrar(self):
        self.parent.parent.destroy()
    def volver(self):
        self.parent.aMenu()
        self.destroy()

    def creaManifestGrupos(self, permisso, grupos):
        self.controlador.creaManifestGrupo(permisso, grupos)
        return
    def creaManifestProtection(self, permiso, protection):
        self.controlador.creaManifestProtection(permiso, protection)
        return
    def compila(self):
        self.realizando.configure(text="Compilando apk...")
        self.controlador.compilar()
        self.DONE = True
        self.realizando.configure(text="Apk creada")
        self.canvas.destroy()
        return
    def motrarApk(self):
        self.controlador.abrirExplorador()
    def instalaApk(self):
        salida = self.controlador.instalaApk()
        print(salida)
        if salida[0] != "":
            self.resultado.configure(text = salida[0])
            
        else:
            self.resultado.configure(text = salida[1], text_color="red")
    def draw(self):
        imagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../assets/cargando.png")
        image = Image.open(imagePath)
        image = image.resize([100,100])
        angle = 0
        while not self.DONE:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(50, 50
                , image=tkimage)
            self.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle -= 10
            angle %= 360
            time.sleep(0.02)