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

    // Comprobamos los permisos de telefono sin solicitarlos
    fun clickNoPhone(v: View?) {
        presenter.toPhone()
    }

    //Solicitamos parte 1 de los permisos de telefono y mostramos la lista de permisos de telefono
    fun clickPhone1(v: View?) {
        presenter.phone1()
    }

    //Solicitamos parte 2 de los permisos de telefono y mostramos la lista de permisos de telefono
    fun clickPhone2(v: View?) {
        presenter.phone2()
    }

    // Método que se llama cuando el usuario responde a la solicitud de permisos.
    // En este caso se usa para esperar la respuesta del usuario en los permisos de telefono para que
    // no se salte de actividad directamente, esperamos respuesta y luego saltamos.
    override fun onRequestPermissionsResult(
        requestCode: Int, permissions: Array<String>, grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == 102 || requestCode == 103) {
            presenter.toPhone()
        }
    }
}