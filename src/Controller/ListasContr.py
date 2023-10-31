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
    # Obtenemos una lista de permisos, si opcion es 4 o 5 solo se dan
    # permisos normales o signature respectivamente
    def getPermisos(self, opcion):
        if opcion == 4:
            return self.modeloPermisos.getPermisosNormales()
        if opcion == 5:
            return self.modeloPermisos.getPermisosSignature()
        else:
            return self.modeloPermisos.getPermisos()
    # Obtenemos una lista con todos los grupos
    def getGrupos(self):
        return list(self.modeloGrupos.getGrupos())
    # Vamos a la vista final pasandole permiso, grupo, protectionLevel y opcion indicados,
    # Si la opción seleccionada no necesita alguno de estos valores, se manda None en su lugar
    def aFinal(self, parent, permiso, grupos, protection, opcion):
        if opcion == 1:
            if grupos[0] == self.modeloPermisos.getGrupo(permiso):
                return "El permiso ya pertenece a ese grupo"
            else:
                final(parent, opcion, permiso, grupos, protection)
        elif opcion == 2:
            if grupos[0] == self.modeloPermisos.getGrupo(permiso):
                return "El permiso ya pertenece a ese grupo"+grupos[0]
            elif grupos[1] == self.modeloPermisos.getGrupo(permiso):
                return "El permiso ya pertenece al grupo"+grupos[1]
            else:
                final(parent, opcion, permiso, grupos, protection)
        elif opcion == 3:
            if protection == self.modeloPermisos.getProtection(permiso):
                return "El permiso ya tiene ese protection level"
            else:
                final(parent, opcion, permiso, grupos, protection)
        else:
            final(parent, opcion, permiso, grupos, protection)