# App-Perm
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
