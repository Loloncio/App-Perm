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

class Final(ctk.CTkToplevel):
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
        self.title("APK")
        self.WIDTH=1280
        # Fuentes que usaremos para los botones y etiquetas
        titleFont = ctk.CTkFont(family="Inter", size=30, weight="normal")
        textFont = ctk.CTkFont(family="Inter", size=20, weight="normal")
        # Canvas y mensaje para mostrar el progreso
        canvas = tk.Canvas(self, width=100, height=100,bg="#1E1E1E", highlightthickness=0)
        self.realizando = ctk.CTkLabel(self,text_color="white",text="Creando archivo AndroidManifest.xml...",
                                       font= titleFont, corner_radius=10)
        canvas.pack(anchor="center", pady = 100)
        self.realizando.pack(pady = 50, padx = 30)
        # Hacemos que el canvas se recargue periodicamente para crear el efecto de que gira
        self.update = self.draw(canvas).__next__
        self.after(100, self.update)
        # Zona para poner botones de ir al menú, abrir la ubicación del apk o instalar el apk
        frameBotones = ctk.CTkFrame(self, fg_color="#1E1E1E")
        # Abre la ubicación del apk
        botonAbrir = ctk.CTkButton(frameBotones, text = "Abrir ruta a apk", command = self.motrarApk,
                                font= textFont, fg_color="#D9D9D9", text_color="black",width = 170, height=60)
        # Instala el apk
        botonInstalar = ctk.CTkButton(frameBotones, text = "Instalar apk",command = self.instalaApk,
                                font = textFont, fg_color="#D9D9D9", text_color="black", width=170, height=60)
        # Volvemos al menú
        botonVolver = ctk.CTkButton(frameBotones, text="Menu", command = self.volver, font = textFont, fg_color="#D9D9D9",
                                text_color="black", width=170, height=60)
        # Salida del botón instalar y mensaje con los requisitos para usarlo
        frameSalida = ctk.CTkScrollableFrame(master=self,fg_color="#504F4F", corner_radius= 10,width = ((self.WIDTH)-40),height=400);
        self.resultado = ctk.CTkLabel(frameSalida,text_color="white", text="Para usar el botón instalar debes tener conectado\
                                un dispositivo con depuración USB habilitada y Android 13 o superior", font= textFont,
                                wraplength=650)
        # Desactivamos abrir e instalar mientras se compila la apk
        botonAbrir.configure(state="disabled")
        botonInstalar.configure(state="disabled")
        # Hilo para la compilación
        thread = threading.Thread(target=self.compila, kwargs={'canvas': canvas, 'botonAbrir': botonAbrir,
                                                               'botonInstalar': botonInstalar})
        # En función de la opción elegida en el menú compilamos una cosa u otra
        self.opt = int(opt)
        permiso = str(permiso)
        if self.opt == 1:
            grupos = list(grupos)
            self.creaManifestGrupo(permiso, grupos)
            thread.start()
        elif self.opt == 2:
            grupos = list(grupos)
            self.creaManifestGrupo(permiso, grupos)
            thread.start()
        elif self.opt == 3:
            protection = str(protection)
            self.creaManifestProtection(permiso, protection)
            thread.start()
        elif self.opt == 4:
            grupos = list(grupos)
            self.creaManifestGrupo(permiso, grupos)
            thread.start()
        elif self.opt == 5:
            grupos = list(grupos)
            self.creaManifestGrupo(permiso, grupos)
            thread.start()
        # Colocamos los botones
        frameBotones.pack(pady = 10, padx = 10)
        botonVolver.grid(row = 0, column = 0, padx = 10, pady =10)
        botonAbrir.grid(row = 0, column = 1, padx = 10, pady =10)
        botonInstalar.grid(row = 0, column = 2, padx = 10, pady =10)
        frameSalida.pack(pady = 50, padx = 30)
        self.resultado.pack(pady = 5, padx = 30)
    # Métodos para cerrar la ventana y volver al menú
    def cerrar(self):
        self.parent.parent.destroy()
    def volver(self):
        self.parent.aMenu()
        self.destroy()
    # Le pedimos al controlador que cree un Manifest para modificar el grupo de un permiso
    def creaManifestGrupo(self, permisso, grupos):
        if(self.opt == 2):
            self.controlador.creaManifestGrupos(permisso, grupos)
        else:
            self.controlador.creaManifestGrupo(permisso, grupos)
        return
    # Le pedimos al controlador que cree un Manifest para modificar el protection level de un permiso
    def creaManifestProtection(self, permiso, protection):
        self.controlador.creaManifestProtection(permiso, protection)
        return
    # Le pedimos al compilador que compile el apk y reactivamos los botones de abrir e instalar al terminar
    def compila(self, canvas, botonAbrir, botonInstalar):
        self.realizando.configure(text="Compilando apk...")
        resultado =  self.controlador.compilar()
        self.DONE = True
        if resultado.returncode == 0:
            self.realizando.configure(text="APK compilado con éxito")
            self.resultado.configure(text = resultado.stdout, text_color="white", wraplength = self.WIDTH-150)
            botonAbrir.configure(state="normal")
            botonInstalar.configure(state="normal")
        else:
            self.realizando.configure(text="Error al compilar apk")
            self.resultado.configure(text = resultado.stderr, text_color="red", wraplength = self.WIDTH-150)
        canvas.destroy()
        return
    # Abrimos el explorador de archivos donde se encuentra el apk
    def motrarApk(self):
        self.controlador.abrirExplorador()
    # Intentamos instalar el apk y mostramos el resultado
    def instalaApk(self):
        salida = self.controlador.instalaApk()
        if salida[1] != "":
            self.resultado.configure(text = salida[1], text_color="red")
        else:
            self.resultado.configure(text = salida[0], text_color="white")
    # Recargamos el icono de carga rotado para que de el efecto de que gira
    def draw(self, canvas):
        imagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../assets/cargando.png")
        image = Image.open(imagePath)
        image = image.resize([100,100])
        angle = 0
        while not self.DONE:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = canvas.create_image(50, 50
                , image=tkimage)
            self.after_idle(self.update)
            yield
            canvas.delete(canvas_obj)
            angle -= 10
            angle %= 360
            time.sleep(0.02)