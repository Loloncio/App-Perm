# Esta vista nos presentará 3 listas, una con los permisos, otra con los grupos
# y otra con los protection level por defecto de android.
# Cuando pulsamos en un permiso, vemos a que grupo pertence pertence por defecto
# y su protection level.
# Cuando pulsamos en un grupo, obtenemos una lista de los permisos que contiene
# ese grupo.
# Cuando pulsamos en un protection level, vemos los permisos que tienen ese
# protection level.
# Autor: Alejandro de la Cruz Garijo
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)

import tkinter as tk
import customtkinter as ctk
from Controller.DefectoContr import ControladorDef

class defecto(ctk.CTkToplevel):
    # Algunas variables globales para los parametros que pasaremos a la siguiente vista,
    # la opción que se ha seleccionado y una etiqueta de errores
    HEIGHT = 720
    WIDTH = 1280
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")

        # Declaración e inicialización de variables
        frames, scrolls, permisos, grupos, protection, labels = [], [], [], [], [], []
        textoPermisos = [
            "Permiso1",
            "Permiso2",
            "Permiso3",
            "Permiso4",
            "Permiso5",
            "Permiso6",
            "Permiso7",
            "Permiso8",
            "Permiso9",
        ]
        textoGrupos = ControladorDef.getGrupos()
        textoProtection =[
            "Normal",
            "Dangerous",
            "Signature"
        ]

        # Fuente que usaremos en esta vista
        leftFont = ctk.CTkFont(family="Inter", size=25, weight="normal")
        rightFont = ctk.CTkFont(family="Inter", size=20, weight="normal")

        # Creación de los frames base para cada lista
        for i in range(3):
            frames.append(ctk.CTkFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.WIDTH-10))
        # Creación de scrollFrames donde se vera la lista de botones y
        # frames donde podremos la información correspondiente al pulsar un boton
        for i in range(3):
            scrolls.append(ctk.CTkScrollableFrame(master=frames[i],fg_color="#504F4F", corner_radius= 10, width = self.WIDTH/2-20))
        # Creación de los labels que se colocan a la derecha de las listas
        for i in range(3):
            labels.append(ctk.CTkLabel(frames[i], text="", text_color="white", fg_color="#504F4F",
                                corner_radius=10, justify="center", font=rightFont, width = self.WIDTH/2-20))
        # Creación de los botones para elegir permiso
        for i in textoPermisos:
            permisos.append(ctk.CTkButton(scrolls[0], text=i, text_color="white", fg_color="#504F4F",
                                          font=leftFont, corner_radius= 10,
                                          command=lambda permiso = i, label = labels[0]: self.permisoClick(permiso, label)))
        # Creación de los botones para elegir grupo
        for i in textoGrupos:
            grupos.append(ctk.CTkButton(scrolls[1], text=i, text_color="white", fg_color="#504F4F",
                                          font=leftFont, corner_radius= 10,
                                          command=lambda grupo = i, label = labels[1]: self.grupoClick(grupo,label)))
        # Creación de los botones para elegir nivel de protección
        for i in textoProtection:
            protection.append(ctk.CTkButton(scrolls[2], text=i, text_color="white", fg_color="#504F4F",
                                          font=leftFont, corner_radius= 10,
                                          command=lambda protection = i, label = labels[2]: self.protectionClick(protection,label)))
        # Creación del botón para volver al menu principal
        volver = ctk.CTkButton(scrolls[2], command=self.volver, text="Volver", font=leftFont, corner_radius=10,
                                fg_color="#1E1E1E", text_color="white", height=50)
        # Colocación de los frame base para las listas
        for i in range(3):
            frames[i].pack(padx=5, pady=5, fill="x",expand = True)
        # Colocación de los frames donde pondremos las listas de botones y el resultado de la elección
        for i, j in zip(scrolls, labels):
            i.grid(row = 0, column=0, padx = 5, sticky="e")
            j.grid(row = 0, column=1,padx = 5, sticky="nw")
        # Colocación de los permisos
        for permiso in permisos:
            permiso.pack(fill="x", padx = 3)
        # Colocación de los grupos
        for grupo in grupos:
            grupo.pack(fill="x", padx = 3)
        # Colocación de los niveles de potección
        for level in protection:
            level.pack(fill="x", padx = 3)
        # Colocación del botón de vuelta
        volver.pack(anchor = "w", side = "bottom")
        # Cuando se modifique el tamaño de la ventana se llama al método que reajusta los elementos
        self.bind("<Configure>", lambda event, frames = frames, scrolls = scrolls, labels= labels,
                  self=self: self.ajustarTamanos(self, frames, scrolls, labels))
    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        ControladorDef.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        ControladorDef.volver(self, self.parent)
    # Método para cuando se pulsa un permiso
    def permisoClick(self, permiso, label):
        label.configure(text=permiso)
        print(permiso)
        return
    # Método para cuando se pulas un grupo
    def grupoClick(self, grupo, label):
        permisosGrupo = ControladorDef.getPermisos(grupo)
        label.configure(text=permisosGrupo)
        return
    # Método para cuando se pulsa un nivel de protección
    def protectionClick(self, protection, label):
        label.configure(text=protection)
        print(protection)
        return
    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, frames, scrolls, labels):
        anchoVentana = self.winfo_width()
        altoVentana = self.winfo_height()
        # Si se ha generado un evento configure (como hacer scroll) pero no cambia el tamaño de pantalla,
        # no hacemos nada.
        if(self.HEIGHT != altoVentana or self.WIDTH != anchoVentana):
            self.HEIGHT = altoVentana
            self.WIDTH = anchoVentana

            for i in range(3):
                frames[i].configure(width = anchoVentana-10,height=altoVentana/3-10)
                labels[i].configure(width = anchoVentana-10,height=altoVentana/3-10)
                scrolls[i].configure(width = (anchoVentana/2)-20,height=altoVentana/3-10)
            # Actualiza la ventana
            self.update_idletasks()