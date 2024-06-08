import os
import sys
import subprocess
from Model.Grupos import Grupos

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)

class ComparaContr():
    modeloGrupos = Grupos()

    def getCSV(self):
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} '

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
        vistMenu.parent.destroy()
    def descargaMovil(self):
        rutaPermisos = "/storage/emulated/0/TFG/Grupos.csv"
        ruta_adb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Android/Sdk/platform-tools/adb")
        comando = f'{ruta_adb} pull {rutaPermisos} ./src/Model/PermisosMovil.csv'

        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        salida = []
        salida.append(resultado.stdout)
        salida.append(resultado.stderr)

        return salida
    def comparaGrupos(self):
        salida = self.descargaMovil()
        if salida[1] != "":
            return salida[1]

        movil = self.modeloGrupos.getGruposPermisosMovil()
        app = self.modeloGrupos.getGruposPermisos()
        # Compara los dos diccionarios y detecta las diferencias.
        diferenciasStr = ""
        for group, permission_1 in movil.items():
            permission_2 = app.get(group)
            if permission_1 != permission_2:
                if permission_1 == None:
                    diferenciasStr += f"El dispositivo contiene los siguientes permisos del grupo {group} que no se encuentran en la lista de permisos por defecto: {permission_2} "
                elif permission_2 == None:
                    diferenciasStr += f"La lista de permisos por defecto contiene los siguientes permisos del grupo {group} que no se encuentran en el dispositivo: {permission_1} "
                else:
                    diferenciasStr += f"El grupo {group} presenta las siguientes diferencias: " + self.obtenerDiferencias(permission_1, permission_2)
        if diferenciasStr == "":
            return "No se han encontrado diferencias"

        return "Se han encontrado las siguientes diferencias:\n\n"+diferenciasStr

    def obtenerDiferencias(self, list1, list2):
        # Find the differences between the lists
        differences = set(list1) ^ set(list2)
        # Create the output string
        output_string = ""

        # If there are no differences, indicate that the lists are the same
        if not differences:
            return ""
        else:
            # Iterate through the differences and create the output string
            for difference in differences:
                if difference in list1:
                    output_string += f"{difference} se encuentra unicamente en la lista de permisos por defecto.\n"
                else:
                    output_string += f"{difference} se encuentra unicamente en el dispositivo.\n"

        return output_string