import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from View.Defecto import Defecto
from View.Listas import Listas
from View.ADB import ADB
from View.Firmadas import Firmadas
from View.Ayuda import Ayuda

class MenuContr:
    def aDefecto(self, ventanaPrincipal):
        Defecto(ventanaPrincipal)
        return
    def aListas(self, ventanaMenu, opcion):
        Listas(ventanaMenu.parent, opcion)
        return
    def aFirmadas(self, ventanaPrincipal):
        Firmadas(ventanaPrincipal)
        return
    def aADB(self, ventanaPrincipal):
        ADB(ventanaPrincipal)
        return
    def aAyuda(self, ventanaPrincipal):
        Ayuda(ventanaPrincipal)
        return