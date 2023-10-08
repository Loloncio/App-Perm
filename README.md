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

1. Menu.py: Métodos funcionales para todos los botones (Faltan los dos últimos)
2. Defecto.py
	<ul>
		<li>Añadir boton para ir a vista final</li>
	</ul>
3. Listas.py
	<ul>
		<li>Si estamos en las opciones 2 a 5, no funciona el botón confirmar</li>
	</ul>
4. Final.py
	<ul>
		<li>Arreglar bug por el cual a veces no se muestra nada hasta que no se ha compilado el apk</li>
		<li>Aquí podría ir un emulador android o un botón para abrir uno si fuese posible</li>
	</ul>
5. Firmadas.py
	<ul>
		<li>Mostrará opciones para hacer con apps firmadas</li>
		<li>Comprobar si se conceden permisos dangerous a 2 apps firmadas con mismo certificado</li>
		<li>Comprobar si se conceden permisos signature a 2 apps firmadas con mismo certificado</li>
		<li>Comprobar que solo se conceden permisos signature a apps con el mismo dertificado</li>
	</ul>
6. ADB.py
	<ul>
		<li>Mostrará todos los permisos del dispositivo conectado, de forma similar a Defecto.py</li>
	</ul>
5. DefectoContr.py
	<ul>
		<li>Permitirá ir a la vista Final</li>
	</ul>
6. Emulador Android incluido?
