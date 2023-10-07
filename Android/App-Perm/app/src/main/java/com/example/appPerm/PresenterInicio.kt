package com.example.appPerm

import android.content.Intent
import android.content.pm.PackageManager
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat

class PresenterInicio constructor() {

    private lateinit var modelo: Modelo
    private lateinit var view: AppCompatActivity

    constructor(activity: AppCompatActivity) : this() {
        this.view = activity
        modelo = Modelo(view.packageManager.getAllPermissionGroups(PackageManager.GET_META_DATA))
    }
    //Vamos a la actividad permisos
    fun toPermisos() {
        val intent = Intent(view, Permisos::class.java)
        view.startActivity(intent)
    }
    //Vamos a la actividad grupos
    fun toGrupos() {
        val intent = Intent(view, Grupos::class.java)
        view.startActivity(intent)
    }
    //Vamos a la actividad GruposNoSys
    fun toNoSysGrupos() {
        val intent = Intent(view, GruposNoSys::class.java)
        view.startActivity(intent)
    }
    //Vamos a la actividad revocar
    fun toRevocar() {
        val intent = Intent(view, RevocarPermisos::class.java)
        view.startActivity(intent)
    }
    //Vamos a la actividad phone
    fun toPhone() {
        val intent = Intent(view, Phone::class.java)
        view.startActivity(intent)
    }
    //Solicitamos los permisos al usuario
    fun solicitaPermisos() {
        view.requestPermissions(modelo.getPermisos(), 101)
    }
    //Pedimos los permisos de phone1 o vamos a la actividad phone si ya esta concedidos
    fun phone1() {
        if (checkPermissions(modelo.getPhone1())) {
            // Si los permisos ya están concedidos, iniciamos la actividad Phone
            toPhone()
        } else {
            // Si los permisos no están concedidos, los solicitamos
            view.requestPermissions(modelo.getPhone1(), 102)
        }
    }
    //Pedimos los permisos de phone2 o vamos a la actividad phone si ya esta concedidos
    fun phone2() {
        if (checkPermissions(modelo.getPhone2())) {
            // Si los permisos ya están concedidos, iniciamos la actividad Phone
            toPhone()
        } else {
            // Si los permisos no están concedidos, los solicitamos
            view.requestPermissions(modelo.getPhone2(), 103)
        }
    }

    // Función para verificar si los permisos de un array dado están concedidos
    private fun checkPermissions(permissions: Array<String>): Boolean {
        for (permission in permissions) {
            if (ContextCompat.checkSelfPermission(
                    view, permission
                ) != PackageManager.PERMISSION_GRANTED
            ) {
                return false
            }
        }
        return true
    }
}