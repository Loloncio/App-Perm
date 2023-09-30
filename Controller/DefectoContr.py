import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Model.GruposMod import GruposMod

class ControladorDef:

    def getGrupos():
        return GruposMod.getGrupos()

    def getPermisos(grupo):
        permisos = GruposMod.getPermisos(grupo=grupo)
        lista = ""
        for i in permisos:
            lista += i+"\n"
        return lista

    def volver(vistaDefecto, vistaMenu):
        vistaMenu.deiconify()
        vistaDefecto.destroy()

    def cerrar(vistMenu):
        vistMenu.destroy()