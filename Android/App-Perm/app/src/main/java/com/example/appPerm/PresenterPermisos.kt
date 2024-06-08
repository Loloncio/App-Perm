package com.example.appPerm

import android.R
import android.content.pm.PackageManager
import android.content.pm.PackageManager.GET_PERMISSIONS
import android.os.Environment
import android.util.Log
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.BufferedWriter
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.OutputStreamWriter
import java.nio.charset.Charset


class PresenterPermisos constructor() {

    private lateinit var view: AppCompatActivity
    private lateinit var permisosMod: PermisosMod
    private lateinit var permissions: Array<String>

    constructor(activity: AppCompatActivity) : this() {
        this.view = activity
        permisosMod = PermisosMod()
    }

    //Boton para volver al menu principal de la app
    fun toMenu(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.home -> {
                view.finish()
                return true
            }
        }
        return view.onOptionsItemSelected(item)
    }

    // Funcion que ibtiene una lista de todos los permisos declarados en el Manifest
    fun getPermisos(): Array<String> {
        return permisosMod.getPermisos("com.example.appPerm", view)
    }

    //Obtenemos información de un permiso
    fun infoPermiso(permiso: String, callback: (String) -> Unit) {
        val permissionInfo = try {
            view.packageManager.getPermissionInfo(permiso, 0)
        } catch (e: PackageManager.NameNotFoundException) {
            null // El permiso no existe
        }
        if (permissionInfo != null) {
            view.packageManager.getGroupOfPlatformPermission(permiso, view.mainExecutor) { group ->
                val info: String
                var grupo = group ?: "No pertenece a ningún grupo"
                val concedido = permiso.let {
                    ContextCompat.checkSelfPermission(view, it)
                } == PackageManager.PERMISSION_GRANTED
                val protection =
                    when (view.packageManager.getPermissionInfo(permiso, 0).protection) {
                        0 -> "Normal"
                        1 -> "Dangerous"
                        2 -> "Signature"
                        4 -> "Internal"
                        else -> "Desconocido"
                    }
                info =
                    "Permission:\n$permiso\n\nGroup:\n$grupo\n\nProtection:\n$protection\n\nConcedido:$concedido"
                callback(info)
            }
        }
    }

    fun creaInfoPermisos() {
        if (!compruebaCarpeta("TFG"))
            return
        val listaPermisosInfo = mutableListOf<String>()
        val carpetaTFG = File(Environment.getExternalStorageDirectory(), "TFG")
        val rutaCompleta = File(carpetaTFG, "Permisos.csv")

        try {
            val fileOutputStream = FileOutputStream(rutaCompleta)
            val outputStreamWriter = OutputStreamWriter(fileOutputStream, Charset.forName("UTF-8"))
            val bufferedWriter = BufferedWriter(outputStreamWriter)

            // Escribir una línea de cabecera en el archivo CSV
            bufferedWriter.write("Permiso;Grupo;Protection;Concedido")
            bufferedWriter.newLine()
            // Usamos CoroutineScope para manejar las corrutinas
            CoroutineScope(Dispatchers.Main).launch {
                for (permiso in permissions) try {
                    val permissionInfo = try {
                        view.packageManager.getPermissionInfo(permiso, 0)
                    } catch (e: PackageManager.NameNotFoundException) {
                        null // El permiso no existe
                    }
                    if (permissionInfo != null) withContext(Dispatchers.IO) {
                        view.packageManager.getGroupOfPlatformPermission(
                            permiso, view.mainExecutor
                        ) { group ->
                            val grupo = group ?: "-"
                            val concedido = ContextCompat.checkSelfPermission(
                                view, permiso
                            ) == PackageManager.PERMISSION_GRANTED
                            val protection = when (permissionInfo.protection) {
                                0 -> "Normal"
                                1 -> "Dangerous"
                                2 -> "Signature"
                                4 -> "Internal"
                                else -> "Desconocido"
                            }
                            val info = "$permiso;$grupo;$protection;$concedido"
                            listaPermisosInfo.add(info)
                        }
                    }
                } catch (e: Exception) {
                    e.printStackTrace()
                }
                // Ahora, después de que se completen todas las llamadas asíncronas, mostramos la lista
                for (info in listaPermisosInfo) {
                    bufferedWriter.write(info)
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