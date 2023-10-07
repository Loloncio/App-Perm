# Última vista de App-Perm, aquí vemos el progreso de creación de AndroidManifest.xml
# su compilación, instalación y, finalmente, el resultado de dicha instlación.
# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import time
import sys
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
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#4B4B4B")
        self.canvas = tk.Canvas(self, width=100, height=100,bg="#4B4B4B", highlightthickness=0)
        self.canvas.pack(anchor="center", pady = 200)
        self.update = self.draw().__next__
        self.after(100, self.update)
        
        textFont = ctk.CTkFont(family="Inter", size=15, weight="normal")
        
        opt = int(opt)
        permiso = str(permiso)
        self.realizando = ctk.CTkLabel(self,text_color="white", font= textFont, corner_radius=10)
        self.realizando.configure(text="Creando archivo AndroidManifest.xml...")
        self.realizando.pack(pady= 10)
        if(opt == 1):
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            self.compila()
        elif opt == 2:
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            self.compila()
        elif opt == 3:
            protection = str(protection)
            self.creaManifestProtection(permiso, protection)
            self.compila()
        elif opt == 4:
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            self.compila()
        elif opt == 5:
            grupos = list(grupos)
            self.creaManifestGrupos(permiso, grupos)
            self.compila()

    def cerrar(self):
        self.parent.destroy()

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
        self.realizando.configure(text="Apk creada, puedes encontrarla en XXXXX")
        return

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