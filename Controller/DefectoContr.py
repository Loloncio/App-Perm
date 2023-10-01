import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from Model.GruposMod import GruposMod
from Model.PermisosMod import PermisosMod

class ControladorDef:
    modeloGrupos = GruposMod()
    modeloPermisos = PermisosMod()
    def getGrupos(self):
        return self.modeloGrupos.getGrupos()

    def getPermisosGrupo(self, grupo):
        permisos = self.modeloGrupos.getPermisos(grupo)
        lista = ""
        for i in permisos:
            lista += i+"\n"
        return lista

    def getPermisos(self):
        return self.modeloPermisos.getPermisos()

    def getInfoPermiso(self, permiso):
        texto = "Permiso: "+permiso+"\n"
        texto += "Grupo: "+self.modeloPermisos.getGrupo(permiso)+"\n"
        texto += "Protection level: "+self.modeloPermisos.getProtection(permiso)+"\n"
        return texto
    def getPermisosNormales(self):
        return self.modeloPermisos.getPermisosNormales()
    def getPermisosDangerous(self):
        return self.modeloPermisos.getPermisosDangerous()
    def getPermisosSignature(self):
        return self.modeloPermisos.getPermisosSignature()
    def volver(self, vistaDefecto, vistaMenu):
        vistaMenu.deiconify()
        vistaDefecto.destroy()

    def cerrar(self, vistMenu):
        vistMenu.destroy()