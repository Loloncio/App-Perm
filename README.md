# App-Perm
<p align="left">
   <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
</p>

## Índice
- #### [Objetivos del proyecto](https://github.com/Loloncio/App-Perm/tree/main#objetivos-del-proyecto-1)
- #### [Funcionalidad](https://github.com/Loloncio/App-Perm/tree/main#funcionalidad-1)
- #### [TODO](https://github.com/Loloncio/App-Perm/tree/main#todo-1)

## Objetivos del proyecto
Esta aplicación tiene por objetivo poder probar algunas preguntas que pueden surgir al iniciarse en los permisos de Android:

¿Podrían darse estos escenarios?

* En el fichero AndroidManifest.xml, se declaran permisos, pero algunos permisos “dangerous” no aparecen asociados a ningún grupo.
* En el fichero AndroidManifest.xml, se declaran permisos y se declara de forma explícita su pertenencia a un grupo de permisos. La asociación es acorde con las indicaciones que Google proporciona en sus manuales para desarrolladores.
* En el fichero AndroidManifest.xml, se declaran permisos y se declara de forma explícita su pertenencia a un grupo de permisos. La asociación entra en conflicto con las indicaciones que Google proporciona en sus manuales para desarrolladores.

¿Que ocuure en estos casos?

* ¿A qué protection level asigna el sistema operativo los permisos, al declarado en el fichero Manifest.xml o al predefinido por Google?
* ¿A qué grupo asigna el sistema operativo los permisos, al declarado en el fichero Manifest.xml o al predefinido por Google?
* ¿Es posible asociar un permiso que no sea de tipo dangerous a un grupo de permisos?
* ¿En qué fichero define Android los grupos de permisos soportados? ¿Puede conocerse vía adb?
* ¿En qué fichero define Android los permisos soportados? ¿Puede conocerse vía adb?
* ¿Puede un permiso estar en más de un grupo a la vez?
* Dado un grupo de permisos, ¿es posible obtener qué permisos forman el grupo?
* Si una app logra un permiso de tipo dangerous, ¿otra app firmada con el mismo certificado digital consigue automáticamente ese permiso (se lo concede el SO sin intervención del usuario)?
* Si una app logra un permiso de tipo signature, ¿otra app firmada con el mismo certificado digital consigue automáticamente ese permiso?

## Funcionalidad
El proyecto constará de una aplicación Python y una app Android. La app Android ya está creada, con la aplicación Python endremos que crear distintos AndroidManifest.xml que usaremos en esa app. La aplicación Python también deberá compilar e instalar esa app Android. A partir de ahora cuando digamos app, estaremos refiriendonos a la app Android y cuando digamos aplicación, estaremos hablando de la aplicación Python. Las funciones que deberá realizar la aplicación serán:

* Mostrar permisos y grupos de permisos por defecto: En este caso se compilará e instalará la app original donde el usuario podrá ver los grupos y grupos de permisos y que permisos están asociados a que grupo. Al mismo tiempo, en la aplicación se mostrará esa misma lista que ya se ha obtenido previamente.

* Añadir un permiso a otro grupo de permisos: La aplicación creará un AndroidManifest.xml con esa orden, a continuación, se sustituirá el manifest original por ese nuevo, se compilará, se instalará y se devolverá éxito o el mensaje de error al instalar.

* Añadir un permiso a variso grupos de permisos: La aplicación creará un AndroidManifest que intentará añadir un permiso a dos grupos, se compilará, se instalará y se devolverá éxito o el mensaje de error al instalar.

* Cambiar protection level: Se intentará modificar el protection level de un permiso se compilará, se instalará y se devolverá éxito o el mensaje de error al instalar.

* Asignar permiso normal a un grupo: Se tratará de añadir un permiso normal a un grupo de permisos, se compilará, se instalará y se devolverá éxito o el mensaje de error al instalar.

* Asignar permiso signature a un grupo: Se tratará de añadir un permiso normal a un grupo de permisos, se compilará, se instalará y se devolverá éxito o el mensaje de error al instalar.

* Ver los permisos y grupos del dispositivo: Se hará mediante adb, se manda el comando y se muestra el resultado en la aplicación, es decir, en este caso no haríamos nada de la app Android.

* Pruebas con apps firmadas: En este caso se abrirá una pestaña similar al menu principal con más opciones sobre estas pruebas.

## TODO

1. Menu.py: Métodos funcionales para todos los botones (Faltan el primero y los dos últimos)
2. Listas.py:
   <ul>
	   <li>Cubrirá las 5 primeras opciones, en función de cual se pulse, se hará una u otra.</li>
	   <li><b>Opción 3:</b></li>
	   <li>El protection level ha de ser distinto al original</li>
	   <li><b>Opción 4:</b></li>
	   <li>Se muestran solo los permisos normales</li>
	   <li><b>Opción 5:</b></li>
	   <li>Solo aparecen los permisos con protection level signature</li>
	   <li><b>General</b></li>
	   <li>Al pulsar confirmar se cambia de ventana y se pasan las opciones marcadas </li>
   </ul>
3. Defecto.py
	<ul>
		<li>Se mostrará la info requerida a la derecha de cada opción</li>
		<li>Añadir boton para volver al menú principal</li>
	</ul>
4. Final.py
	<ul>
		<li>Aquí se mostraran varios mensajes de carga: Creando Manifest, compilando app, Instalando app y finalmente exito o fallo y mensaje de error en caso de fallo</li>
		<li>Debe comprobar que haya un dispositivo adb conectado</li>
		<li>Aquí podría ir un emulador android o un botón para abrir uno si fuese posible</li>
	</ul>
5. ADB.py
	<ul>
		<li>Mostrará opciones para hacer con apps firmadas</li>
		<li>Comprobar si se conceden permisos dangerous a 2 apps firmadas con mismo certificado</li>
		<li>Comprobar si se conceden permisos signature a 2 apps firmadas con mismo certificado</li>
		<li>Comprobar que solo se conceden permisos signature a apps con el mismo dertificado</li>
	</ul>

6. PermisosMod.py    
	Guardará una lista con todos los permisos, a que grupo pertenece cada uno y su protection level.    
	Permitira obtener toda esa información, o solo un permiso con su info.
7. GruposMod.py    
	Guardará una lista con todos los permisos, a que grupo pertenece cada uno y su protection level.    
	Permitira obtener toda esa información, o solo un permiso con su info.
8. MenuContr.py
	<ul>
		<li>Se encargará de abrir las otras vistas</li>
	</ul>
9. DefectoContr.py
	<ul>
		<li>Permitira volver a Menu</li>
		<li>Pedira los datos necesarios a los modelos de datos</li>
		<li>Permitira ir a la vista Final</li>
	</ul>
10. Emulador Android incluido?
11. Crear un main que solo tenga la ventana principal y no la clase mainWindow, de esta forma no esta mainWindow siempre en segundo plano
