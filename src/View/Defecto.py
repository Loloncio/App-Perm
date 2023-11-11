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
    controlador = ControladorDef()
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Permisos y grupos por defecto")

        # Declaración e inicialización de variables
        frames, scrolls, permisos, grupos, protection, labels = [], [], [], [], [], []
        textoPermisos = self.controlador.getPermisos()
        textoGrupos = self.controlador.getGrupos()
        textoProtection =[
            "Normal",
            "Dangerous",
            "Signature"
        ]

        # Fuente que usaremos en esta vista
        leftFont = ctk.CTkFont(family="Inter", size=20, weight="normal")
        rightFont = ctk.CTkFont(family="Inter", size=15, weight="normal")

        # Creación de los frames base para cada lista
        for i in range(3):
            frames.append(ctk.CTkFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.WIDTH-10, height=self.HEIGHT/3-46))
        # Creación de scrollFrames donde se vera la lista de botones y
        # frames donde podremos la información correspondiente al pulsar un boton
        for i in range(6):
            scrolls.append(ctk.CTkScrollableFrame(master=frames[i%3],fg_color="#504F4F", corner_radius= 10,width = ((self.WIDTH/2)-40)))
        # Creación de los labels que se colocan a la derecha de las listas
        for i in range(3):
            labels.append(ctk.CTkLabel(scrolls[i+3], text="", text_color="white", fg_color="#504F4F",
                                corner_radius=10, justify="center", font=rightFont,wraplength=((self.WIDTH/2)-45), height=self.HEIGHT/3-46))
        # Creación de los botones para elegir permiso
        for i in textoPermisos:
            permiso = ctk.CTkLabel(scrolls[0], text=i, text_color="white", fg_color="#504F4F",
                                          font=leftFont, corner_radius= 10, wraplength=self.WIDTH/2-20, justify= "center"
                                          )
            permiso.bind("<Button-1>",lambda event, permiso = i, label = labels[0]: self.permisoClick(self, permiso, label))
            permiso.bind("<Enter>", lambda event, permiso = permiso: self.onEnter(self, permiso))
            permiso.bind("<Leave>", lambda event, permiso = permiso: self.onExit(self, permiso))
            permisos.append(permiso)
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
        volver = ctk.CTkButton(self, command=self.volver, text="Volver", font=leftFont, corner_radius=10,
                                fg_color="#1E1E1E", text_color="white", height=40)
        # Colocación de los frame base para las listas
        for i in range(3):
            frames[i].grid(column= 0, row = i, columnspan=2, padx=3, pady=3,)
        # Colocación del botón de vuelta
        volver.grid(column = 0, row = 3, pady = 3, padx = 20, sticky="w")
        # Colocación de los frames donde pondremos las listas de botones y el resultado de la elección
        for i in range(3):
            scrolls[i].grid(row = 0, column=0, padx = 5)
            scrolls[i+3].grid(row = 0, column=1, padx = 5)
        for i in labels:
            i.pack(fill = "both",side="top", anchor="center")
        # Colocación de los permisos
        for permiso in permisos:
            permiso.pack(fill="x")
        # Colocación de los grupos
        for grupo in grupos:
            grupo.pack(fill="x" )
        # Colocación de los niveles de potección
        for level in protection:
            level.pack(fill="x")
        # Cuando se modifique el tamaño de la ventana se llama al método que reajusta los elementos
        self.bind("<Configure>", lambda event, frames = frames, scrolls = scrolls, labels= labels,
                  self=self: self.ajustarTamanos(self, frames, scrolls, labels))

    # Método para cerrar toda la app al pulsar la x
    def cerrar(self):
        self.controlador.cerrar(self.parent)
    # Método para vovler al menú principal
    def volver(self):
        self.controlador.volver(self, self.parent)
    # Método para cuando se pulsa un permiso
    def permisoClick(self, event, permiso, label):
        label.configure(text=self.controlador.getInfoPermiso(permiso))
        return
    # Método para cuando se pulas un grupo
    def grupoClick(self, grupo, label):
        permisosGrupo = self.controlador.getPermisosGrupo(grupo)
        label.configure(text=permisosGrupo)
        return
    # Método para cuando se pulsa un nivel de protección
    def protectionClick(self, protection, label):
        if protection == "Normal":
            label.configure(text=self.controlador.getPermisosNormales())
        elif protection == "Dangerous":
            label.configure(text=self.controlador.getPermisosDangerous())
        elif protection == "Signature":
            label.configure(text=self.controlador.getPermisosSignature())
        return
    # Método para que cambie de color un widget al pasar el ratón por encima
    def onEnter(self, event, permiso):
        permiso.configure(fg_color = "#36719f")
    # Método para que cambie de color un widget al quitar el ratón de encima
    def onExit(self,event, permiso):
        permiso.configure(fg_color = "#504F4F")

    def instalaApp(self):
        self.controlador.isntalaApp()

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
                labels[i].configure(width = (anchoVentana/2)-20,height=altoVentana/3-46)
                scrolls[i].configure(width = (anchoVentana/2)-40,height=altoVentana/3-46)
                scrolls[i+3].configure(width = (anchoVentana/2)-40,height=altoVentana/3-46)
            # Actualiza la ventana
            self.update_idletasks()