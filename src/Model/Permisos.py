# Clase PermisosMod del modelo de datos de la aplicación App-perm.
# Obtiene los datos de los permisos y su grupo y protection level asociados.
# Permite acceder a estos datos de varias formas.
# Autor: Alejandro de la Cruz Garijo
import csv
import os
class Permisos():
    # Abrimos el fichero csv de datos y obtenemos una matriz con los datos de los permisos
    def __init__(self):
        self.permisos = []
        ruta_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./Permisos.csv")
        with open(ruta_csv) as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                permiso = row['Permiso']
                grupo = row['Grupo']
                protection = row['Protection']
                self.permisos.append([permiso, grupo, protection])
    # Obtenemos una lista con todos los permisos
    def getPermisos(self):
        listaPermisos = []
        for permiso in self.permisos:
            listaPermisos.append(permiso[0][permiso[0].rfind('.')+1::1])
        return listaPermisos
    # Obtenemos una lista con todos los permisos cuyo protection level sea normal
    def getPermisosNormales(self):
        normales = []
        for permiso in self.permisos:
            if permiso[2] == "Normal":
                normales.append(permiso[0][permiso[0].rfind('.')+1::1])
        return normales
    # Obtenemos una lista con todos los permisos cuyo protection level sea dangerous
    def getPermisosDangerous(self):
        dangerous = []
        for permiso in self.permisos:
            if permiso[2] == "Dangerous":
                dangerous.append(permiso[0][permiso[0].rfind('.')+1::1])
        return dangerous
    # Obtenemos una lista con todos los permisos cuyo protection level sea signature
    def getPermisosSignature(self):
        signature = []
        for permiso in self.permisos:
            if permiso[2] == "Signature":
                signature.append(permiso[0][permiso[0].rfind('.')+1::1])
        return signature
    # Obtenemos el grupo asociado a un permiso
    def getGrupo(self, permiso):
        for perm in self.permisos:
            if perm[0][perm[0].rfind('.')+1::1] == permiso:
                if perm[1] != "-":
                    return perm[1][perm[1].rfind('.')+1::1]
                else:
                    return "No pertenece a ningún grupo"
    # Obtenemos el protection level asociado a un permiso
    def getProtection(self,permiso):
        for perm in self.permisos:
            if perm[0][perm[0].rfind('.')+1::1] == permiso:
                return perm[2]
    # Obtenemos el nombre completo del permiso dado
    def getPermisoCompleto(self, permiso):
        for perm in self.permisos:
            if permiso in perm[0]:
                return perm[0]
    # Obtenemos el nombre completo del grupo dado
    def getGrupoCompleto(self, grupo):
        for perm in self.permisos:
            if grupo in perm[1]:
                return perm[1]