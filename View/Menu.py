# Menú principal de App-Perm, una aplicación que nos permitirá comprobar
# de forma empírica algunas preguntas que pueden surgir sobre la gestión
# de los permisos y grupos de permisos de Android.
# Este menú nos permite ir a las distintas pruebas que se han planteado.
# Autor: Alejandro de la Cruz Garijo
import tkinter as tk
import customtkinter as ctk
from Listas import listas
from Defecto import defecto

class mainWindow(ctk.CTkFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.configure(fg_color = "#4B4B4B")
        #Ejemplo de paso de variables a hijo
        self.optList = tk.StringVar(self)

        # Variables
        # Diccionario que toma como clave el texto que tendra el botón y como valor la función que ejecutará
        variablesBotones = {
            "Grupos y permisos\npor defecto": self.defecto,
            "Cambiar grupo\nde permiso": self.cambioGrupo,
            "Añadir permiso\na dos grupos": self.permisoADosGrupos,
            "Cambiar protection\nlevel": self.cambiaProtLevel,
            "Asignar permiso\nnormal a un grupo": self.normalAGrupo,
            "Asignar permiso\nsignature a un grupo": self.signaAGrupo,
            "Ver permisos y\ngrupos\ndel dispositivo": self.verDispositivo,
            "Pruebas con apps\nfirmadas": self.appsFirmadas
        }
        botones = []

        # Fuente que se usará en la app, tamaños para título y texto
        tittleFont = ctk.CTkFont(family="Inter", size=60, weight="bold")
        textFont = ctk.CTkFont(family="Inter", size=20, weight="normal")

        # Etiqueta que muestra el nombre de la app
        mainText = ctk.CTkLabel(self, text="App-Perm", text_color="white", font=tittleFont, pady=60)
        # Frame que contendrá los botones ordenados con un gridLayout
        gridBotones = ctk.CTkFrame(master=self,fg_color="#4B4B4B")
        # Botones del menu
        for texto, funcion in variablesBotones.items():
            boton = ctk.CTkButton(gridBotones, command=funcion, text=texto, font=textFont, corner_radius=10,
                                  fg_color="#D9D9D9", text_color="black", width=250, height=100)
            botones.append(boton)

        # Colocación de los botones en el Frame para los botones
        cont = 0;
        for i in range(0,2):
            for j in range(0,4):
                botones[cont].grid(row=i, column=j, padx=30, pady=40)
                cont += 1

        # Mostramos la etiqueta de texto y el frame de los botones
        mainText.pack()
        gridBotones.pack()

    # Funciones para los botones
    def defecto(self):
        defecto(self.parent)
        return
    def cambioGrupo(self):
        self.optList.set(1)
        listas(self.parent, self.optList.get())
        return
    def permisoADosGrupos(self):
        self.optList.set(2)
        listas(self.parent, self.optList.get())
        print("Añade a dos grupos")
        return
    def cambiaProtLevel(self):
        self.optList.set(3)
        listas(self.parent, self.optList.get())
        print("Cambia protection level")
        return
    def normalAGrupo(self):
        self.optList.set(4)
        listas(self.parent, self.optList.get())
        print("Añade normal a grupo")
        return
    def signaAGrupo(self):
        self.optList.set(5)
        listas(self.parent, self.optList.get())
        print("Añade signature a grupo")
        return
    def verDispositivo(self):
        print("Ver dispositivo")
        return
    def appsFirmadas(self):
        print("Apps firmadas")
        return

if __name__ == "__main__":
    # Creación de ventana principal
    root = ctk.CTk()
    root.geometry("1280x720")
    root.minsize(width=1280,height=720)
    root.title("App-Perm")
    mainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()