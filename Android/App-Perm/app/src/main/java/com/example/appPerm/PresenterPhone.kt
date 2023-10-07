package com.example.appPerm

import android.content.pm.PackageManager
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat

class PresenterPhone constructor() {

    private lateinit var modelo: Modelo
    private lateinit var view: AppCompatActivity

    constructor(activity: AppCompatActivity) : this() {
        this.view = activity
        modelo = Modelo(view.packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA))
    }

    //Boton para volver al menu principal de la app
    fun toMenu(item: MenuItem): Boolean {
        when (item.itemId) {
            android.R.id.home -> {
                view.finish()
                return true
            }
        }
        return view.onOptionsItemSelected(item)
    }

    //Funcion que comprueba los permisos del grupo telefono y obtiene información de ellos
    fun compruebaPermisos(): String {
        val stringBuilder = StringBuilder()
        for (permiso in modelo.getPhonePerm()) {
            val protection = when (view.packageManager.getPermissionInfo(permiso, 0).protection) {
                0 -> "Normal"
                1 -> "Dangerous"
                2 -> "Signature"
                4 -> "Internal"
                else -> "Desconocido"
            }
            if (ContextCompat.checkSelfPermission(
                    view, permiso
                ) == PackageManager.PERMISSION_GRANTED
            ) {
                stringBuilder.append("\nSe ha concedido permiso a:\n $permiso\nProtectionLevel:$protection\n")
            } else {
                stringBuilder.append("\nNO se ha concedido permiso a:\n $permiso\nProtectionLevel:$protection\n")
            }
        }
        return stringBuilder.toString()
    }
}