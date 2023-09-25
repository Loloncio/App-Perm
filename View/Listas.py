# Prueba de App-Perm, nos permite ver 3 listas, una con todos los permisos,
# otra con todos los grupos de permisos y otra con los protection level.
# En función de quien lo llame, mostrara unas listas u otras y hará unas
# cosas u otras
# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk

class listas(ctk.CTkToplevel):
    def confirmar():
        return

    def __init__(self, parent, vent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # Ajustes de ventana principal
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.parent.withdraw()
        self.geometry("1280x720")
        self.minsize(width=1280,height=720)
        self.configure(fg_color = "#1E1E1E")

        # Variables necesarias
        listas, etiquetas, permisos, grupos, protection = [], [], [], [], []
        textoEtiquetas = [
            "Permisos",
            "Grupos de permisos",
            "Protection level"
        ]
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
        valoresSticky = ["w","n","e"]
        check_var = ctk.StringVar(value="on")

        # Fuentes de texto
        headersFont = ctk.CTkFont(family="Inter", size=35, weight="bold")
        textFont = ctk.CTkFont(family="Inter", size=20, weight="normal")

        # Creación de frames para las listas
        for i in range(0,3):
            listas.append(ctk.CTkScrollableFrame(master=self,fg_color="#504F4F"))
        # Creación de etiquetas para las cabeceras
        for i in textoEtiquetas:
            etiquetas.append(ctk.CTkLabel(self, text=i, text_color="white", fg_color="#504F4F",
                                corner_radius=10, font=headersFont,height=100))
        # Creación de chechboxes para los permisos
        for i in textoPermisos:
            permisos.append(ctk.CTkCheckBox(listas[0], text=i, text_color="white", font= textFont,
                                command=lambda check_var=check_var: self.checkboxPermisos(check_var),
                                variable=check_var, onvalue=i, offvalue="not"+i))

        # Creación de botones para confirmar o volver al menú
        confirmacion = ctk.CTkButton(self, command=self.confirmar, text="Siguiente", font=textFont,
                                corner_radius=10, fg_color="#504F4F", text_color="white", height=50)
        volver = ctk.CTkButton(self, command=self.volver, text="Volver", font=textFont, corner_radius=10,
                                fg_color="#504F4F", text_color="white", height=50)

        # Colocación las etiquetas en la ventana utilizando grid
        for i, j in zip(range(3), valoresSticky):
            etiquetas[i].grid(row=0, column=i, sticky=j,padx=3, pady=3)
        # Colocar los frames en la ventana utilizando grid
        for i, j in zip(range(3), valoresSticky):
                listas[i].grid(row=1, column=i, padx=3, pady=3, sticky=j)
        # Colocación de los permisos en su lista
        for i in permisos:
            i.pack(pady=3)
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
        self.destroy()

    def checkboxPermisos(self, check_var):
        print("ok ", check_var.get())

    def checkboxGrupo(self, check_var):
        print("ok ", check_var.get())

    def checkboxProtection(self, check_var):
        print("ok ", check_var.get())

    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, etiquetas, listas, confirmacion, volver):
        anchoVentana = self.winfo_width()  # Ancho de la ventana
        altoVentana = self.winfo_height()  # Alto de la ventana

        for i, j in zip(etiquetas, listas):
            i.configure(width=max(100, anchoVentana // 3 - 6))
            j.configure(width=max(100, anchoVentana // 3 - 30))
            j.configure(height=altoVentana - 180)
            confirmacion.configure(width=max(50, (anchoVentana // 3 - 6) // 2))
            volver.configure(width=max(50, (anchoVentana // 3 - 6) // 2))
        # Actualiza la ventana
        self.update_idletasks()
