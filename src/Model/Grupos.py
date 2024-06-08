# Clase GruposMod del modelo de datos de la aplicación App-perm.
# Obtiene los datos de los grupos de permisos y sus permisos asociados
# y permite acceder a estos datos.
# Autor: Alejandro de la Cruz Garijo
import csv
import os
import pandas as pd

class Grupos():
    # Abrimos el csv con los datos y creamos un diccionario con los grupos como clave y
    # una lista de sus permsios como valor
    def __init__(self):
        self.grupos = {}
        ruta_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./Permisos.csv")
        with open(ruta_csv) as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                permiso = row['Permiso']
                grupo = row['Grupo']
                if grupo in self.grupos:
                    self.grupos[grupo].append(permiso)
                else:
                    self.grupos.update({grupo:[permiso]})
    # Obtenemos todas las claves del diccionario, es decir, los grupos
    def getGrupos(self):
        grupos = self.grupos.keys()
        lista = []
        for key in grupos:
            lista.append(key[key.rfind('.')+1::1])
        return lista
    # Obtenemos todos los permisos de un grupo
    def getPermisos(self, grupo):
        permisos = self.grupos.get(self.getGrupoCompleto(grupo))
        lista = [permiso[permiso.rfind('.')+1::1] for permiso in permisos]
        return lista
    # Obtenemos el nombre completo de un grupo dado
    def getGrupoCompleto(self, grupo):
        for group in self.grupos.keys():
            if grupo in group:
                return group

    def getGruposPermisosMovil(self):
        ruta_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./PermisosMovil.csv")
        # Lee los datos de los dos archivos CSV.
        data1 = pd.read_csv(ruta_csv, delimiter=";")
        # Crea un diccionario con los permisos de los grupos en el primer archivo CSV.
        group_permissions_1 = {}
        for row in data1.itertuples():
            key = row[1]
            if(type(row.Permisos)!=type(1.0)):
                value = row.Permisos.split(",")
                group_permissions_1[key] = value
            else:
                value = ""

        return group_permissions_1

    def getGruposPermisos(self):
        return self.grupos