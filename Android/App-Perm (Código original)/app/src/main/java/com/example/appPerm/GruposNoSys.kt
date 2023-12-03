package com.example.appPerm

import android.os.Bundle
import android.view.MenuItem
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.LinearLayout
import android.widget.ListView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class GruposNoSys : AppCompatActivity() {
    private lateinit var presenter: PresenterGruposNoSys
    private lateinit var adapter: ArrayAdapter<String>
    private lateinit var grupoView: LinearLayout

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_grupos_no_sys)
        // Botón para volver al menu principal
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        presenter = PresenterGruposNoSys(this)

        val listaGrupos: ListView = findViewById(R.id.NoSysPermissionGroups)
        grupoView = findViewById(R.id.PermissionsInNoSysGroup)

        //Obtenemos una lista con el nombre de todos los grupos y la mostramos en la lista
        val grupos: MutableList<String> = presenter.getGrupos()
        adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, grupos)
        listaGrupos.adapter = adapter

        // Cuando se selecciona un grupo, mostramos los permisos que contiene o que no contiene ninguno
        listaGrupos.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            //Limpiamos lo que ubiese en groupView
            eliminarElementos()
            val grupo = adapter.getItem(position)
            if (grupo != null) {
                //Obtenemos toda la información relevante del grupo.
                val info = presenter.infoGrupo(grupo)
                if (info != null) {
                    for (texto in info) {
                        val textView = TextView(this)
                        textView.layoutParams = LinearLayout.LayoutParams(
                            LinearLayout.LayoutParams.MATCH_PARENT,
                            LinearLayout.LayoutParams.WRAP_CONTENT
                        )
                        textView.textSize = 16f
                        textView.setTextColor(0xFF000000.toInt())
                        textView.text = texto
                        //Mostramos la info que viene en el formato: Nombre, [Permisos] (o mensaje de que no tiene permisos)
                        grupoView.addView(textView)
                    }
                }
            }
        }
        // Mostramos en los logs los grupos que tienen permisos y que permisos contiene.
        presenter.getPermissionsInGroups()
    }

    // Método para que funcione el botón de vuelta al menu
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return presenter.toMenu(item)
    }

    // Borramos todos los elementos de la scrollView para no mezclar resultados
    private fun eliminarElementos() {
        for (i in grupoView.childCount - 1 downTo 0) {
            val childView = grupoView.getChildAt(i)
            if (childView is TextView) {
                grupoView.removeViewAt(i)
            }
        }
    }
}