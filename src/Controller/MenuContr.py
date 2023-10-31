import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from View.Defecto import defecto
from View.Listas import listas
from View.Final import final
from View.ADB import adb

class ControladorMenu:
    def aDefecto(self, ventanaPrincipal):
        defecto(ventanaPrincipal)
        return
    def aListas(self, ventanaMenu, opcion):
        listas(ventanaMenu.parent, opcion)
        return
    def aFirmadas(self, ventanaPrincipal):
        return
    def aADB(self, ventanaPrincipal):
        adb(ventanaPrincipal)
        return
    def aAyuda(self, ventanaPrincipal):
        return