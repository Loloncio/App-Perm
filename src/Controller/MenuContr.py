import os
import sys
import subprocess

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from View.VistaDefecto import VistaDefecto
from View.VistaListas import VistaListas
from View.VistaADB import VistaADB
from View.VistaFirmadas import VistaFirmadas
from View.VistaAyuda import VistaAyuda

class MenuContr:
    def iniciaADB(self):
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} start-server'
        subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    def aDefecto(self, ventanaPrincipal):
        VistaDefecto(ventanaPrincipal)
        return
    def aListas(self, ventanaMenu, opcion):
        VistaListas(ventanaMenu.parent, opcion)
        return
    def aFirmadas(self, ventanaPrincipal):
        VistaFirmadas(ventanaPrincipal)
        return
    def aADB(self, ventanaPrincipal):
        VistaADB(ventanaPrincipal)
        return
    def aAyuda(self, ventanaPrincipal):
        VistaAyuda(ventanaPrincipal)
        return