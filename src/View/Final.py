# Última vista de App-Perm, aquí vemos el progreso de creación de AndroidManifest.xml
# su compilación, instalación y, finalmente, el resultado de dicha instlación.
# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import time

class final(ctk.CTkToplevel):
    DONE = False
    def __init__(self, parent, opt, *args, **kwargs):
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
    def cerrar(self):
        self.parent.destroy()