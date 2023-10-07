package com.example.appPerm

import android.os.Bundle
import android.view.MenuItem
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class Phone : AppCompatActivity() {
    private lateinit var presenter: PresenterPhone

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_phone)
        // Botón para volver al menu
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        presenter = PresenterPhone(this)
        val phoneView: TextView = findViewById(R.id.PermisosPhone)
        // Comprobamos y mostramos que permisos se han concedido
        val permisosPhone = presenter.compruebaPermisos()
        phoneView.text = permisosPhone
    }

    // Método para que funcione el botón de vuelta al menu
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return presenter.toMenu(item)
    }
}