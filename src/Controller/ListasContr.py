# Controlador para la vista listas de la app App-Perm
# Autor: Alejandro de la Cruz Garijo
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Model.GruposMod import GruposMod
from Model.PermisosMod import PermisosMod
from View.Final import final

class ListasContr():
    modeloPermisos = PermisosMod()
    modeloGrupos = GruposMod()

    def getPermisos(self, opcion):
        if opcion == 4:
            return self.modeloPermisos.getPermisosNormales()
        if opcion == 5:
            return self.modeloPermisos.getPermisosSignature()
        else:
            return self.modeloPermisos.getPermisos()
    def getGrupos(self):
        return list(self.modeloGrupos.getGrupos())
    def aFinal(self, parent, permiso, grupos, protection, opcion):
        if opcion == 1:
            #print(grupos[0], self.modeloPermisos.getGrupo(permiso))
            if grupos[0] == self.modeloPermisos.getGrupo(permiso):
                return "El permiso ya pertenece a ese grupo"
            else:
                final(parent, opcion, permiso, grupos, protection)
        elif opcion == 2:
            return "OK"
        elif opcion == 3:
            if protection == self.modeloPermisos.getProtection(permiso):
                return "El permiso ya tiene ese protection level"
            else:
                return "OK"
        else:
            return "OK"