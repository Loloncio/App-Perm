import os
import subprocess

class FirmadasContr():
    def instalaDangerous(self):
        ruta_apk1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm.apk")
        ruta_apk2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Dangerous.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} install "{ruta_apk1}"'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []
        salida.append(resultado.stdout)
        salida.append(resultado.stderr)

        comando = f'{ruta_adb} install "{ruta_apk2}"'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida[0] = salida[0]+resultado.stdout
        salida[1] = salida[1]+resultado.stderr

        return salida
    def isntalaSignature(self):
        ruta_apk1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm.apk")
        ruta_apk2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Signature.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} install "{ruta_apk1}"'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []
        salida.append(resultado.stdout)
        salida.append(resultado.stderr)

        comando = f'{ruta_adb} install "{ruta_apk2}"'
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida[0] = salida[0]+resultado.stdout
        salida[1] = salida[1]+resultado.stderr

        return salida
    def testFirmadas(self):
        ruta_signer = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/build-tools/33.0.1/apksigner")
        apks = {}
        apks["App-Perm"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm.apk")
        apks["Dangerous"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Dangerous.apk")
        apks["Signature"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Signature.apk")
        salida = ["","",""]
        for nombre, apk in apks.items():
            comando = f'{ruta_signer} verify --print-certs "{apk}"'
            resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(resultado.stdout)
            salida[0] = salida[0]+nombre+":\n"+resultado.stdout
            if(resultado.stderr != ""):
                salida[1] = salida[1]+nombre+":\n"+resultado.stderr
        print(salida[1])

        return salida
    # Método para vovler al menú principal
    def volver(self, vistaFirmadas, vistaMenu):
        vistaMenu.deiconify()
        vistaFirmadas.destroy()
    # Método para cerrar del todo la app al pulsar en cerrar
    def cerrar(self, vistMenu):
        vistMenu.destroy()