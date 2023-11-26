# Prueba de App-Perm, nos permite ver 3 listas, una con todos los permisos,
# otra con todos los grupos de permisos y otra con los protection level.
# En función de quien lo llame, mostrara unas listas u otras y hará unas
# cosas u otras
# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Controller.ListasContr import ListasContr

class Listas(ctk.CTkToplevel):
    # Algunas variables globales para los parametros que pasaremos a la siguiente vista,
    # la opción que se ha seleccionado y una etiqueta de errores
    PERMISO = ""
    GRUPO = []
    PROTECTION = ""
    OPT = 0
    ERRORES = None
    HEIGHT = None
    WIDTH = None
    controlador = ListasContr()
    def __init__(self, parent, opt, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")
        self.title("Modificar permisos")
        self.OPT = int(opt)
        self.GRUPO.clear()

        # Variables necesarias
        listas, etiquetas, permisos, grupos, protection = [], [], [], [], []
        textoEtiquetas = [
            "Permisos",
            "Grupos de permisos",
            "Protection level"
        ]
        textoPermisos = self.controlador.getPermisos(opt)
        textoGrupos = self.controlador.getGrupos()
        textoProtection =[
            "Normal",
            "Dangerous",
            "Signature"
        ]
        valoresSticky = ["w","n","e"]
        check_var = ctk.StringVar(value="on")

        # Fuentes de texto
        headersFont = ctk.CTkFont(family="Inter", size=40, weight="bold")
        textFont = ctk.CTkFont(family="Inter", size=15, weight="normal")
        errorFont = ctk.CTkFont(family="Inter", size=15, weight="normal")

        # Creación de frames para las listas
        for i in range(0,3):
            listas.append(ctk.CTkScrollableFrame(master=self,fg_color="#504F4F"))
        # Creación de etiquetas para las cabeceras
        for i in textoEtiquetas:
            etiquetas.append(ctk.CTkLabel(self, text=i, text_color="white", fg_color="#504F4F",
                                corner_radius=10, font=headersFont,height=100))
        # Creación de checkboxes para los permisos
        for i in textoPermisos:
            permisos.append(ctk.CTkCheckBox(listas[0], text=i, text_color="white", font= textFont,
                                command=lambda check_var=check_var, permisos=permisos, textoPermisos= textoPermisos:
                                self.checkboxPermisos(check_var, permisos, textoPermisos),
                                variable=check_var, onvalue="Perm"+i, offvalue="!"+i))
        # Creación de checkboxes para los grupos
        for i in textoGrupos:
            grupos.append(ctk.CTkCheckBox(listas[1], text=i, text_color="white", font= textFont,
                                command=lambda check_var=check_var, grupos=grupos, textoGrupos= textoGrupos:
                                self.checkboxGrupo(check_var, grupos, textoGrupos),
                                variable=check_var, onvalue=i, offvalue="!"+i))
        # Creación de checkboxes para los protection level
        for i in textoProtection:
            protection.append(ctk.CTkCheckBox(listas[2], text=i, text_color="white", font= textFont,
                                command=lambda check_var=check_var, protection=protection, textoProtection= textoProtection:
                                self.checkboxProtection(check_var, protection, textoProtection),
                                variable=check_var, onvalue=i, offvalue="!"+i))

        # Creación de botones para confirmar o volver al menú
        confirmacion = ctk.CTkButton(self, command=self.confirmar, text="Siguiente", font=textFont,
                                corner_radius=10, fg_color="#504F4F", text_color="white", height=50)
        volver = ctk.CTkButton(self, command=self.volver, text="Volver", font=textFont, corner_radius=10,
                                fg_color="#504F4F", text_color="white", height=50)

        # Creación de etiqueta para mostrar errores
        self.ERRORES = ctk.CTkLabel(self,text_color="red", text = "", font= errorFont, corner_radius=10)

        # Desactivamos los checkboxes que no se puedan usar en el caso en el que estemos
        if(self.OPT == 1 or self.OPT == 2 or self.OPT == 4 or self.OPT == 5):
            for checkbox in protection:
                checkbox.configure(state="disabled")
        elif self.OPT == 3:
            for checkbox in grupos:
                checkbox.configure(state="disabled")

        # Colocación las etiquetas en la ventana utilizando grid
        for i, j in zip(range(3), valoresSticky):
            etiquetas[i].grid(row=0, column=i, sticky=j,padx=3, pady=3)
        # Colocar los frames en la ventana utilizando grid
        for i, j in zip(range(3), valoresSticky):
                listas[i].grid(row=1, column=i, padx=3, pady=3, sticky=j)
        # Colocación de los permisos en su lista
        for i in permisos:
            i.grid(pady=3,sticky="w")
        # Colocación de los grupos en su lista
        for i in grupos:
            i.grid(pady=3,sticky="w")
        # Colocación de los protection level en su lista
        for i in protection:
            i.grid(pady=3,sticky="w")
        # Colocación de los botones en su sitio
        confirmacion.grid(row=2, column=2, padx=3, pady=3)
        volver.grid(row=2, column=0, padx=3, pady=3)
        # Evento que se ejecuta al mover o redimensionar la ventana
        self.bind("<Configure>", lambda event, etiquetas=etiquetas, listas=listas, confirmacion= confirmacion,
                                volver=volver, self=self: self.ajustarTamanos(self, etiquetas, listas,
                                confirmacion, volver))

    def cerrar(self):
        self.parent.destroy()

    def volver(self):
        self.parent.deiconify()
        self.destroy()

    def confirmar(self):
        if self.PERMISO == "":
            self.ERRORES.configure(text="Debes seleccionar un permiso.")
            self.ERRORES.grid(row = 2, column = 1, padx=3, pady=3)
            return
        if self.OPT == 1:
            if len(self.GRUPO) != 1:
                self.ERRORES.configure(text="Debes seleccionar un grupo de permisos.")
                self.ERRORES.grid(row = 2, column = 1, padx=3, pady=3)
                return
            else:
                error = self.controlador.aFinal(self,self.PERMISO,self.GRUPO,None, self.OPT)
        elif self.OPT == 2:
            if len(self.GRUPO) != 2:
                self.ERRORES.configure(text="Debes seleccionar 2 grupos de permisos.")
                self.ERRORES.grid(row = 2, column = 1, padx=3, pady=3)
                return
            else:
                error = self.controlador.aFinal(self,self.PERMISO,self.GRUPO,None, self.OPT)
        elif self.OPT == 3:
            if self.PROTECTION == "":
                self.ERRORES.configure(text="Debes seleccionar un protection level.")
                self.ERRORES.grid(row = 2, column = 1, padx=3, pady=3)
                return
            else:
                error = self.controlador.aFinal(self,self.PERMISO,None,self.PROTECTION, self.OPT)
        elif self.OPT == 4:
            if len(self.GRUPO) != 1:
                self.ERRORES.configure(text="Debes seleccionar un grupo de permisos.")
                self.ERRORES.grid(row = 2, column = 1, padx=3, pady=3)
                return
            else:
                error = self.controlador.aFinal(self,self.PERMISO,self.GRUPO,None, self.OPT)
        elif self.OPT == 5:
            if len(self.GRUPO) != 1:
                self.ERRORES.configure(text="Debes seleccionar un grupo de permisos.")
                self.ERRORES.grid(row = 2, column = 1, padx=3, pady=3)
                return
            else:
                error = self.controlador.aFinal(self,self.PERMISO,self.GRUPO,None, self.OPT)
        if error != "OK":
            self.ERRORES.configure(text=error)
            self.ERRORES.grid(row = 2, column = 1, padx=3, pady=3)
        return

    def checkboxPermisos(self, check_var, permisos, textoPermisos):
        if(check_var.get()[0] != "!"):
            clickedCheckbox = permisos[textoPermisos.index(check_var.get()[4::])]
            self.PERMISO = check_var.get()[4::]
            for checkbox in permisos:
                if checkbox != clickedCheckbox:
                    checkbox.deselect()

    def checkboxGrupo(self, check_var, grupos, textoGrupos):
        if(check_var.get()[0] != "!"):
            clickedCheckbox = grupos[textoGrupos.index(check_var.get())]
            self.GRUPO.append(check_var.get())
            if(self.OPT != 2):
                if len(self.GRUPO) > 1:
                    self.GRUPO.pop(0)
                for checkbox in grupos:
                    if checkbox != clickedCheckbox:
                        checkbox.deselect()
            elif len(self.GRUPO) > 2:
                self.GRUPO.pop(0)
                for checkbox in grupos:
                    if checkbox != grupos[textoGrupos.index(self.GRUPO[0])] and checkbox != grupos[textoGrupos.index(self.GRUPO[1])]:
                        checkbox.deselect()
        elif self.OPT != 2:
            self.GRUPO.clear()
        else:
            self.GRUPO.pop(self.GRUPO.index(check_var.get()[1::]))

    def checkboxProtection(self, check_var, protection, textoProtection):
        if(check_var.get()[0] != "!"):
            clickedCheckbox = protection[textoProtection.index(check_var.get())]
            self.PROTECTION = check_var.get()
            for checkbox in protection:
                if checkbox != clickedCheckbox:
                    checkbox.deselect()
    def aMenu(self):
        self.parent.deiconify()
        self.destroy()
    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, etiquetas, listas, confirmacion, volver):
        anchoVentana = self.winfo_width()  # Ancho de la ventana
        altoVentana = self.winfo_height()  # Alto de la ventana
        if(self.HEIGHT != altoVentana or self.WIDTH != anchoVentana):
            self.HEIGHT = altoVentana
            self.WIDTH = anchoVentana
            for i, j in zip(etiquetas, listas):
                i.configure(width=max(100, anchoVentana // 3 - 6))
                j.configure(width=max(100, anchoVentana // 3 - 30))
                j.configure(height=altoVentana - 180)
                confirmacion.configure(width=max(50, (anchoVentana // 3 - 6) // 2))
                volver.configure(width=max(50, (anchoVentana // 3 - 6) // 2))
            # Actualiza la ventana
            self.update_idletasks()
