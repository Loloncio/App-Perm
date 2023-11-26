import sys
import os
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
    # Creamos un permiso para el manifest que tendrá un unico permiso, grupo y protectionLevel
    # el permiso y el grupo de permisos los ha elegido el usuario.
    def creaManifestGrupo(self,permiso, grupos):
        nuevoGrupo = '\n<permission\
            \nandroid:name="'+self.modeloPermisos.getPermisoCompleto(permiso)+\
            '"\nandroid:protectionLevel="'+self.modeloPermisos.getProtection(permiso).lower()+\
            '"\nandroid:permissionGroup="'+self.modeloPermisos.getGrupoCompleto(grupos[0])+'"/>'\
            '\n<uses-permission android:name="'+self.modeloPermisos.getPermisoCompleto(permiso)+'"/>'
        manifest = self.modeloManifest.getManifest1()+nuevoGrupo+self.modeloManifest.getManifest2()
        self.modeloManifest.setManifest(manifest)
        return
    # Creamos un permiso para el manifest que tendrá un unico permiso, grupo y protectionLevel, el permiso
    # y el protection level los ha elegido el usuario.
    def creaManifestProtection(self, permiso, protection):
        nuevoProtection = '\n<permission\
            \nandroid:name="'+self.modeloPermisos.getPermisoCompleto(permiso)+\
            '"\nandroid:protectionLevel="'+protection.lower()+\
            '"\nandroid:permissionGroup="'+self.modeloPermisos.getGrupo(permiso)+'"/>'\
            '\n<uses-permission android:name="'+self.modeloPermisos.getPermisoCompleto(permiso)+'"/>'
        manifest = self.modeloManifest.getManifest1()+nuevoProtection+self.modeloManifest.getManifest2()
        self.modeloManifest.setManifest(manifest)
        return
    # Creamos un permiso para el manifest que tendrá un unico permiso, dos grupo y  un protectionLevel
    # el permiso y los grupos los ha elegido el usuario
    def creaManifestGrupos(self,permiso, grupos):
        nuevoGrupo = '\n<permission\
            \nandroid:name="'+self.modeloPermisos.getPermisoCompleto(permiso)+'"'\
            '\nandroid:protectionLevel="'+self.modeloPermisos.getProtection(permiso).lower()+'"'\
            '\nandroid:permissionGroup="'+self.modeloPermisos.getGrupoCompleto(grupos[0])+'","'+self.modeloPermisos.getGrupoCompleto(grupos[1])+'"/>'\
            '\n<uses-permission android:name="'+self.modeloPermisos.getPermisoCompleto(permiso)+'"/>'
        manifest = self.modeloManifest.getManifest1()+nuevoGrupo+self.modeloManifest.getManifest2()
        self.modeloManifest.setManifest(manifest)
        return
    # Crea un archivo AndroidManifest.xml y se compila el apk con ese Manifest
    def compilar(self):
        self.modeloManifest.creaManifest()

        rutaProyecto = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../Android/App-Perm")
        comando = f"{rutaProyecto}/gradlew.bat assembleDebug --stacktrace"
        resultado = subprocess.run(comando, shell=True, cwd=rutaProyecto, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return resultado
    # Abre en el explorador la ruta al archivo apk, funciona en Windows y Linux
    def abrirExplorador(self):
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug")

        if platform.system() == "Windows":
            # Si estás en Windows
            subprocess.Popen(f'explorer {ruta}', shell=True)
        elif platform.system() == "Linux":
            # Si estás en Linux
            subprocess.Popen(['xdg-open', ruta])
    # Instenta instalar el apk mediante adb
    def instalaApk(self):
        ruta_apk = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/build/outputs/apk/debug/app-debug.apk")
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} install "{ruta_apk}"'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida = []

        salida.append(resultado.stdout)

        salida.append(resultado.stderr)
        return salida
