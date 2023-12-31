import os
import sys
import subprocess

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)

class ADBContr():
    def ejecutar(self):
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} shell pm list permissions -g'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []

        salida.append(resultado.stdout)
        salida.append(resultado.stderr)
        return salida

    # Método para vovler al menú principal
    def volver(self, vistaDefecto, vistaMenu):
        vistaMenu.deiconify()
        vistaDefecto.destroy()
    # Método para cerrar del todo la app al pulsar en cerrar
    def cerrar(self, vistMenu):
        vistMenu.destroy()