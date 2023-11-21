package com.example.appPerm

import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AppCompatActivity

class Inicio : AppCompatActivity() {
    private lateinit var presenter: PresenterInicio

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_inicio)
        presenter = PresenterInicio(this)
    }

    // Vamos la opcion de los permisos
    fun clickPermisos(v: View?) {
        presenter.toPermisos()
    }

    // Vamos la opcion de los grupos
    fun clickGrupos(v: View?) {
        presenter.toGrupos()
    }

    // Vamos la opcion de los grupos que no son del sistema
    fun clickNoSysGrupos(v: View?) {
        presenter.toNoSysGrupos()
    }

    //Vamos a la opción de revocar permisos
    fun clickAjustes(v: View?) {
        presenter.toRevocar()
    }

    //Solicitamos los permisos dangerous
    fun clickSolicitaPermisos(v: View?) {
        presenter.solicitaPermisos()
    }
}