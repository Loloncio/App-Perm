import os
import sys

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