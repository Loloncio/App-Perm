import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Model.Ayuda import Ayuda

class AyudaContr():
    modeloAyuda = Ayuda()
    # Método para vovler al menú principal
    def volver(self, vistaFirmadas, vistaMenu):
        vistaMenu.deiconify()
        vistaFirmadas.destroy()
    # Método para cerrar del todo la app al pulsar en cerrar
    def cerrar(self, vistMenu):
        vistMenu.destroy()

    def getTutorial(self):
        elementos = self.modeloAyuda.getTutorial()
        return elementos