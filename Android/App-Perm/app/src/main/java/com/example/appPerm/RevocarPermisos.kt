package com.example.appPerm

import android.os.Bundle
import android.view.MenuItem
import android.view.View
import androidx.appcompat.app.AppCompatActivity

class RevocarPermisos : AppCompatActivity() {
    private lateinit var presenter: PresenterRevocarPermisos

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_revocar_permisos)
        presenter = PresenterRevocarPermisos(this)

        // Botón para volver al menu principal
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
    }

    //Vamos a los ajustes de la aplicación
    fun clickIrAjustes(v: View?) {
        presenter.toAjustes()
    }

    // Método para que funcione el botón de vuelta al menu
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return presenter.toMenu(item)
    }
}