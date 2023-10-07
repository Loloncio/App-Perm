import sys
import os
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
            \nandroid:name="'+permiso+\
            '"\nandroid:protectionLevel="'+self.modeloPermisos.getProtection(permiso)+\
            '"\nandroid:permissionGroup="'+grupos[0]+'"/>'\
            '\n<uses-permission android:name="android.permission.'+permiso+'"/>'
        manifest = self.modeloManifest.getManifest1()+nuevoGrupo+self.modeloManifest.getManifest2()
        self.modeloManifest.setManifest(manifest)
        return

    def creaManifestProtection(self, permiso, protection):
        nuevoProtection = '\n<permission\
            \nandroid:name="'+permiso+\
            '"\nandroid:protectionLevel="'+protection+\
            '"\nandroid:permissionGroup="'+self.modeloPermisos.getGrupo(permiso)+'"/>'\
            '\n<uses-permission android:name="android.permission.'+permiso+'"/>'
        manifest = self.modeloManifest.getManifest1+nuevoProtection+self.modeloManifest.getManifest2
        self.modeloManifest.setManifest(manifest)
        return
    def compilar(self):
        manifest = self.modeloManifest.getManifest()
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/App-Perm/app/src/main/AndroidManifest.xml")
        try:
            with open(ruta, "w") as salida:
                for linea in manifest:
                    salida.write(linea)
        except FileNotFoundError:
            print("No existe el archivo")
            return
        except Exception as e:
            print("Se ha producido un error", end=" ")
            print(e)
            return
        return