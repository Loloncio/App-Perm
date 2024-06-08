package com.example.appPerm

import android.os.Bundle
import android.view.MenuItem
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.ListView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class Permisos : AppCompatActivity() {
    private lateinit var presenter: PresenterPermisos

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_permisos)

        // Botón para volver al menu principal
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        presenter = PresenterPermisos(this)

        val listaPermisos: ListView = findViewById(R.id.Permissions)
        val permisoView: TextView = findViewById(R.id.PermissionInfo)

        // Obtenemos una lista con los permisos solicitados en el Manifest y la mostramos
        val permisos = presenter.getPermisos()
        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, permisos)
        listaPermisos.adapter = adapter

        // Cuando se pulsa un elemento de la lista mostramos información del permiso
        listaPermisos.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val permiso = adapter.getItem(position)
            if (permiso != null) {
                presenter.infoPermiso(permiso) { infoPermiso ->
                    permisoView.setTextColor(0xFF000000.toInt())
                    permisoView.text = infoPermiso
                }
            }
        }
        //Imprimimos en los logs la información de los permisos
        presenter.creaInfoPermisos()
    }

    // Método para que funcione el botón de vuelta al menu
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return presenter.toMenu(item)
    }
}