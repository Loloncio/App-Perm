package com.example.appPerm

import android.R
import android.content.pm.PackageManager
import android.content.pm.PermissionGroupInfo
import android.os.Environment
import android.util.Log
import android.view.MenuItem
import android.widget.ListView
import androidx.appcompat.app.AppCompatActivity
import kotlinx.coroutines.DelicateCoroutinesApi
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.BufferedWriter
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.OutputStreamWriter
import java.nio.charset.Charset

class PresenterGrupos constructor() {

    private lateinit var modelo: Modelo
    private lateinit var view: AppCompatActivity
    private lateinit var grupos: List<PermissionGroupInfo>

    constructor(activity: AppCompatActivity) : this() {
        this.view = activity
        modelo = Modelo(view.packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA))
        grupos = view.packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA)
    }

    //Para volver a la actividad principal
    fun toMenu(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.home -> {
                view.finish()
                return true
            }
        }
        return view.onOptionsItemSelected(item)
    }

    // Esta función crea una lista con todos los grupos de permisos y la devuelve
    fun getGrupos(listaGrupos: ListView): MutableList<String> {
        grupos = view.packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA)
        // Obtenemos solo el nombre de los grupos
        var nombreGrupos: MutableList<String> = mutableListOf()
        for (grupo in grupos) {
            nombreGrupos.add(grupo.name)
        }
        return nombreGrupos
    }

    // Este callback obtiene información de toods los permisos de un grupo, si los hay y la devuelve
    fun infoGrupo(grupo: String?, callback: (List<String>) -> Unit) {
        if (grupo != null) {
            view.packageManager.getPlatformPermissionsForGroup(grupo, view.mainExecutor) { group ->
                val cadenas: MutableList<String> = mutableListOf<String>()
                cadenas.add("Permisos en el grupo $grupo:\n")
                //Comprobamos si el grupo tiene o no permisos
                if (group.isEmpty()) {
                    cadenas.add("Este grupo no contiene permisos")
                } else {
                    for (permiso in group) {
                        //Miramos el protection level del permiso
                        val protection =
                            when (view.packageManager.getPermissionInfo(permiso, 0).protection) {
                                0 -> "Normal"
                                1 -> "Dangerous"
                                2 -> "Signature"
                                4 -> "Internal"
                                else -> "Desconocido"
                            }
                        cadenas.add("$permiso\n$protection\n")
                    }
                }
                callback(cadenas)
            }
        }
    }

    // Muestra en los logs información de todos los permisos ordenados por pertenencia a cada grupo.
    @OptIn(DelicateCoroutinesApi::class)
    fun getPermissionsInGroups() {
        if(!compruebaCarpeta("TFG"))
            return
        val packageManager = view.packageManager
        val listaGrupos = mutableListOf<String>()
        val carpetaTFG = File(Environment.getExternalStorageDirectory(), "TFG")
        val rutaCompleta = File(carpetaTFG, "Grupos.csv")

        try {
            val fileOutputStream = FileOutputStream(rutaCompleta)
            val outputStreamWriter = OutputStreamWriter(fileOutputStream, Charset.forName("UTF-8"))
            val bufferedWriter = BufferedWriter(outputStreamWriter)

            // Escribir una línea de cabecera en el archivo CSV
            bufferedWriter.write("Grupo;Permisos")
            bufferedWriter.newLine()
            GlobalScope.launch(Dispatchers.Main) {
                grupos = packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA)
                for (grupo in grupos) {
                    val nombreGrupo = grupo.name
                    withContext(Dispatchers.IO) {
                        packageManager.getPlatformPermissionsForGroup(
                            nombreGrupo, view.mainExecutor
                        ) { group ->
                            var permisos = ""
                            for (grupo in group){
                                permisos +="$grupo,"
                            }
                            permisos = permisos.dropLast(1)
                            listaGrupos.add("$nombreGrupo;$permisos")
                        }
                    }
                }
                for (grupo in listaGrupos) {
                    bufferedWriter.write(grupo)
                    bufferedWriter.newLine()
                }
                bufferedWriter.close()
                outputStreamWriter.close()
                fileOutputStream.close()
            }
            Log.d("CSV", "Archivo CSV creado exitosamente en: ${rutaCompleta.absolutePath}")
        } catch (e: IOException) {
            e.printStackTrace()
            Log.e("CSV", "Error al crear el archivo CSV.")
        }
    }

    private fun compruebaCarpeta(carpeta: String): Boolean {
        // Comprobar si el almacenamiento externo está montado y listo para escribir
        if (Environment.getExternalStorageState() == Environment.MEDIA_MOUNTED) {
            val rutaCompleta = File(Environment.getExternalStorageDirectory(), carpeta)
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