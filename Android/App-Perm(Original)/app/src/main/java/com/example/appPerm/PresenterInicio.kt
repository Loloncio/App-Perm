package com.example.appPerm

import android.content.Intent
import android.content.pm.PackageManager
import androidx.appcompat.app.AppCompatActivity

class PresenterInicio constructor() {

    private lateinit var permisosMod: PermisosMod
    private lateinit var view: AppCompatActivity

    constructor(activity: AppCompatActivity) : this() {
        this.view = activity
        permisosMod = PermisosMod()
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
    //Solicitamos los permisos al usuario
    fun solicitaPermisos() {
        view.requestPermissions(permisosMod.getPermisos(), 101)
    }
}