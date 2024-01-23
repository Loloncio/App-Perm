package com.example.appPerm

import android.R.id
import android.content.pm.PackageManager
import android.content.pm.PermissionGroupInfo
import android.content.pm.PermissionInfo
import android.os.Environment
import android.util.Log
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import java.io.BufferedWriter
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.OutputStreamWriter
import java.nio.charset.Charset

class PresenterGruposNoSys constructor() {

    private lateinit var view: AppCompatActivity
    private lateinit var grupos: List<PermissionGroupInfo>

    constructor(activity: AppCompatActivity) : this() {
        this.view = activity
        // Obtenemos una lista con todos los grupos que existen en la app
        grupos = view.packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA)
    }

    //Metodo para volver al menu principal de la app
    fun toMenu(item: MenuItem): Boolean {
        when (item.itemId) {
            id.home -> {
                view.finish()
                return true
            }
        }
        return view.onOptionsItemSelected(item)
    }

    //Obtenemos todos los grupos que no son del sistema
    fun getGrupos(): MutableList<String> {
        // Obtenemos solo el nombre de los grupos
        val nombreGrupos: MutableList<String> = mutableListOf()
        for (grupo in grupos) {
            nombreGrupos.add(grupo.name)
        }
        return nombreGrupos
    }

    // Obtenemos informacion de los permisos del grupo si la hubiera
    fun infoGrupo(grupo: String): MutableList<String> {
        val info: MutableList<String> = mutableListOf()
        info.add("Permisos en el grupo $grupo:\n")

        val permisos = view.packageManager.queryPermissionsByGroup(grupo, 0)

        if (permisos.isEmpty()) {
            info.add("Este grupo no contiene permisos")
        } else {
            for (permiso in permisos) {
                //Miramos el protection level del permiso
                val protection = when (permiso.protection) {
                    PermissionInfo.PROTECTION_NORMAL -> "Normal"
                    PermissionInfo.PROTECTION_DANGEROUS -> "Dangerous"
                    PermissionInfo.PROTECTION_SIGNATURE -> "Signature"
                    PermissionInfo.PROTECTION_INTERNAL -> "Internal"
                    else -> "Desconocido"
                }
                info.add("${permiso.name}\n$protection\n")
            }
        }
        return info
    }

    //Muestra información de todos los permisos de todos los grupos.
    fun getPermissionsInGroups() {
        if (!compruebaCarpeta())
            return
        val packageManager = view.packageManager
        compruebaCarpeta()
        val carpetaTFG = File(Environment.getExternalStorageDirectory(), "TFG")
        val rutaCompleta = File(carpetaTFG, "GruposNoSys.csv")

        try {
            val fileOutputStream = FileOutputStream(rutaCompleta)
            val outputStreamWriter = OutputStreamWriter(fileOutputStream, Charset.forName("UTF-8"))
            val bufferedWriter = BufferedWriter(outputStreamWriter)

            // Escribir una línea de cabecera en el archivo CSV
            bufferedWriter.write("Grupo;Permisos")
            bufferedWriter.newLine()
            grupos = packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA)
            for (grupo in grupos) {
                val listaPermisos = packageManager.queryPermissionsByGroup(grupo.name, 0)
                var permisos = ""
                for (permiso in listaPermisos) {
                    permisos += "${permiso.name},"
                }
                permisos = permisos.dropLast(1)
                bufferedWriter.write("${grupo.name};$permisos")
                bufferedWriter.newLine()
            }

            bufferedWriter.close()
            outputStreamWriter.close()
            fileOutputStream.close()

            Log.d("CSV", "Archivo CSV creado exitosamente en: ${rutaCompleta.absolutePath}")
        } catch (e: IOException) {
            e.printStackTrace()
            Log.e("CSV", "Error al crear el archivo CSV.")
        }
    }

    private fun compruebaCarpeta(): Boolean {
        // Comprobar si el almacenamiento externo está montado y listo para escribir
        if (Environment.getExternalStorageState() == Environment.MEDIA_MOUNTED) {
            val rutaCompleta = File(Environment.getExternalStorageDirectory(), "TFG")
            // Crea la carpeta
            return if (!rutaCompleta.exists()) {
                val exito = rutaCompleta.mkdir()
                if (exito) {
                    Log.i("Carpeta", "Carpeta creada, creando archivos")
                    true
                } else {
                    Log.e("Carpeta", "No se ha podido crea la carpeta")
                    false
                }
            } else {
                Log.i("Carpeta", "La carpeta ya existe en el almacenamiento externo.")
                true
            }
        } else {
            Log.e("Carpeta", "El almacenamiento externo no está disponible.")
            return false
        }
    }
}