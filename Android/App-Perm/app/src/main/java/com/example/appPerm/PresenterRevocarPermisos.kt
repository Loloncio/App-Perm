package com.example.appPerm

import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.provider.Settings
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity

class PresenterRevocarPermisos constructor() {

    private lateinit var view: AppCompatActivity

    constructor(activity: AppCompatActivity) : this() {
        this.view = activity
    }

    // Vamos a los ajustes de la app
    fun toAjustes() {
        val intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
        intent.data = Uri.fromParts("package", view.packageName, null)
        view.startActivity(intent)
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
}