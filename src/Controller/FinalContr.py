import sys
import os
import subprocess
import subprocess
import platform
PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Model.ManifestMod import ManifestMod
from Model.PermisosMod import PermisosMod

class FinalContr():
    modeloPermisos = PermisosMod()
    modeloManifest = ManifestMod()

    def creaManifestGrupo(self,permiso, grupos):
        nuevoGrupo = '\n<permission\
            \nandroid:name="android.permission.'+permiso+\
            '"\nandroid:protectionLevel="'+self.modeloPermisos.getProtection(permiso).lower()+\
            '"\nandroid:permissionGroup="android.permission-group.'+grupos[0]+'"/>'\
            '\n<uses-permission android:name="android.permission.'+permiso+'"/>'
        manifest = self.modeloManifest.getManifest1()+nuevoGrupo+self.modeloManifest.getManifest2()
        self.modeloManifest.setManifest(manifest)
        return

    def creaManifestProtection(self, permiso, protection):
        nuevoProtection = '\n<permission\
            \nandroid:name="android.permission.'+permiso+\
            '"\nandroid:protectionLevel="'+protection.lower()+\
            '"\nandroid:permissionGroup="android.permission-group.'+self.modeloPermisos.getGrupo(permiso)+'"/>'\
            '\n<uses-permission android:name="android.permission.'+permiso+'"/>'
        manifest = self.modeloManifest.getManifest1+nuevoProtection+self.modeloManifest.getManifest2
        self.modeloManifest.setManifest(manifest)
        return
    def compilar(self):
        manifest = self.modeloManifest.getManifest()
        rutaManifest = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../Android/App-Perm/app/src/main/AndroidManifest.xml")
        try:
            with open(rutaManifest, "w") as salida:
                for linea in manifest:
                    salida.write(linea)
        except FileNotFoundError:
            print("No existe el archivo")
            return
        except Exception as e:
            print("Se ha producido un error", end=" ")
            print(e)
            return
        rutaProyecto = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../Android/App-Perm")
        comando = f"{rutaProyecto}/gradlew assembleDebug"
        subprocess.run(comando, shell=True, cwd=rutaProyecto)
        return
    def abrirExplorador(self):
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug")

        if platform.system() == "Windows":
            # Si estás en Windows
            subprocess.Popen(f'explorer {ruta}', shell=True)
        elif platform.system() == "Linux":
            # Si estás en Linux
            subprocess.Popen(['xdg-open', ruta])
    def instalaApk(self):
        ruta_apk = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/app-debug.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} install "{ruta_apk}"'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []

        salida.append(resultado.stdout)

        salida.append(resultado.stderr)
        return salida
