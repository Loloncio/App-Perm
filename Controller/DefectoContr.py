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
        return GruposMod.getPermisos(grupo=grupo)