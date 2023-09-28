# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk

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
        textoGrupos = [
            "Grupo1",
            "Grupo2",
            "Grupo3",
            "Grupo4",
            "Grupo5",
            "Grupo6",
        ]
        textoProtection =[
            "Normal",
            "Dangerous",
            "Signature"
        ]

        textFont = ctk.CTkFont(family="Inter", size=30, weight="normal")

        for i in range(3):
            frames.append(ctk.CTkFrame(master=self,fg_color="#504F4F", corner_radius=10, width = self.WIDTH-10))

        for i in range(3):
            scrolls.append(ctk.CTkScrollableFrame(master=frames[i],fg_color="#504F4F", corner_radius= 10, width = self.WIDTH/2-20))
            frames.append(ctk.CTkFrame(master=frames[i],fg_color="#504F4F", corner_radius= 10, width = self.WIDTH/2-20))

        for i in range(3):
            labels.append(ctk.CTkLabel(frames[i+3], text="", text_color="white", fg_color="#504F4F",
                                corner_radius=10, font=textFont))

        for i in textoPermisos:
            permisos.append(ctk.CTkButton(scrolls[0], text=i, text_color="white", fg_color="#504F4F",
                                          font=textFont, corner_radius= 10,
                                          command=lambda permiso = i, label = labels[0]: self.permisoClick(permiso, label)))
        for i in textoGrupos:
            grupos.append(ctk.CTkButton(scrolls[1], text=i, text_color="white", fg_color="#504F4F",
                                          font=textFont, corner_radius= 10,
                                          command=lambda grupo = i, label = labels[1]: self.grupoClick(grupo,label)))
        for i in textoProtection:
            protection.append(ctk.CTkButton(scrolls[2], text=i, text_color="white", fg_color="#504F4F",
                                          font=textFont, corner_radius= 10,
                                          command=lambda protection = i, label = labels[2]: self.protectionClick(protection,label)))

        for i in range(3):
            frames[i].pack(padx=5, pady=5, fill="x",expand = True)

        for i in range(3):
            scrolls[i].grid(row = 0, column=0, padx = 5, sticky="e")
            frames[i+3].grid(row = 0, column=1,padx = 5, sticky="w")

        for permiso in permisos:
            permiso.pack(fill="x", padx = 3)

        for grupo in grupos:
            grupo.pack(fill="x", padx = 3)

        for level in protection:
            level.pack(fill="x", padx = 3)

        for label in labels:
            label.pack(fill="x", padx = 3, sticky="nw")

        self.bind("<Configure>", lambda event, frames = frames, scrolls = scrolls,
                  self=self: self.ajustarTamanos(self, frames, scrolls))


    def cerrar(self):
        self.parent.destroy()

    def volver(self):
        self.parent.deiconify()
        self.destroy()

    def permisoClick(self, permiso, label):
        label.configure(text=permiso)
        print(permiso)
        return
    def grupoClick(self, grupo, label):
        label.configure(text=grupo)
        print(grupo)
        return
    def protectionClick(self, protection, label):
        label.configure(text=protection)
        print(protection)
        return

    # Función para ajustar los tamaños al cambiar el tamaño de la ventana
    def ajustarTamanos(self, event, frames, scrolls):
        anchoVentana = self.winfo_width()  # Ancho de la ventana
        altoVentana = self.winfo_height()  # Alto de la ventana
        if(self.HEIGHT != altoVentana or self.WIDTH != anchoVentana):
            self.HEIGHT = altoVentana
            self.WIDTH = anchoVentana

            for i in range(3):
                frames[i].configure(width = anchoVentana-10,height=altoVentana/3-10)
                frames[i+3].configure(width = (anchoVentana/2)-20,height=altoVentana/3-10)
                scrolls[i].configure(width = (anchoVentana/2)-20,height=altoVentana/3-10)
            # Actualiza la ventana
            self.update_idletasks()