import os
import subprocess

class FirmadasContr():
    def instalaDangerous(self):
        ruta_apk1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/FirmaDang1.apk")
        ruta_apk2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/FirmaDang2.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} install "{ruta_apk1}","{ruta_apk2}"'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []

        salida.append(resultado.stdout)

        salida.append(resultado.stderr)
        return salida
    def isntalaSignature(self):
        ruta_apk1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/FimraSign1.apk")
        ruta_apk2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/FirmaSign2.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} install "{ruta_apk1}", "{ruta_apk2}"'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []

        salida.append(resultado.stdout)

        salida.append(resultado.stderr)
        return salida
    def testFirmadas(self):
        ruta_apk1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/FimraSign1.apk")
        ruta_apk2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/FirmaSign2.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")

        comando = f'{ruta_adb} install "{ruta_apk1}", "{ruta_apk2}"'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []

        salida.append(resultado.stdout)

        salida.append(resultado.stderr)
        return salida
    # Método para vovler al menú principal
    def volver(self, vistaFirmadas, vistaMenu):
        vistaMenu.deiconify()
        vistaFirmadas.destroy()
    # Método para cerrar del todo la app al pulsar en cerrar
    def cerrar(self, vistMenu):
        vistMenu.destroy()