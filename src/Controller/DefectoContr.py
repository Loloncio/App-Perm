# Controlador para la vista Defecto de la app App-Perm
# Autor: Alejandro de la Cruz Garijo
import os
import subprocess
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Model.Grupos import Grupos
from Model.Permisos import Permisos
from View.VistaCompara import VistaCompara

class DefectoContr():
    # Cargamos los modelos de datos necesarios
    modeloGrupos = Grupos()
    modeloPermisos = Permisos()
    # Obtenemos el nombre de todos los grupos
    def getGrupos(self):
        return self.modeloGrupos.getGrupos()
    # Obtenemos todos los permisos de un grupo dado
    def getPermisosGrupo(self, grupo):
        permisos = self.modeloGrupos.getPermisos(grupo)
        lista = ""
        for i in permisos:
            lista += i+"\n"
        return lista
    # Obtenemos el nombre de todos los permisos
    def getPermisos(self):
        return self.modeloPermisos.getPermisos()
    # Obtenemos información de un permiso, su grupo y su protection level
    def getInfoPermiso(self, permiso):
        texto = "Permiso: "+permiso+"\n"
        texto += "Grupo: "+self.modeloPermisos.getGrupo(permiso)+"\n"
        texto += "Protection level: "+self.modeloPermisos.getProtection(permiso)+"\n"
        return texto
    # Obtenemos todos los permisos normales
    def getPermisosNormales(self):
        permisos = self.modeloPermisos.getPermisosNormales()
        lista = ""
        for permiso in permisos:
            lista += permiso+"\n"
        return lista
    # Obtenemos todos los permisos dangerous
    def getPermisosDangerous(self):
        permisos = self.modeloPermisos.getPermisosDangerous()
        lista = ""
        for permiso in permisos:
            lista += permiso+"\n"
        return lista
    # Obtenemos todos los permisos signatures
    def getPermisosSignature(self):
        permisos = self.modeloPermisos.getPermisosSignature()
        lista = ""
        for permiso in permisos:
            lista += permiso+"\n"
        return lista
    # Método para vovler al menú principal
    def volver(self, vistaDefecto, vistaMenu):
        vistaMenu.deiconify()
        vistaDefecto.destroy()
    # Método para cerrar del todo la app al pulsar en cerrar
    def cerrar(self, vistMenu):
        vistMenu.destroy()
    # Instalación de la app App-Perm en dispositivo adb conectado
    def isntalaApp(self):
        ruta_apk = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} install "{ruta_apk}"'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        print("Salida: ", resultado.stdout)
        print("Error: ", resultado.stderr)

    def aCompara(self, ventanaPrincipal):
        VistaCompara(ventanaPrincipal)
        return