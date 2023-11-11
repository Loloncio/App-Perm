import os
import subprocess

class AyudaContr():
    # Método para vovler al menú principal
    def volver(self, vistaFirmadas, vistaMenu):
        vistaMenu.deiconify()
        vistaFirmadas.destroy()
    # Método para cerrar del todo la app al pulsar en cerrar
    def cerrar(self, vistMenu):
        vistMenu.destroy()