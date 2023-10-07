MANIFEST1 = '<?xml version="1.0" encoding="utf-8"?>\n<manifest xmlns:android="http://schemas.android.com/apk/res/android"\nxmlns:tools="http://schemas.android.com/tools">\n<uses-feature\nandroid:name="android.hardware.camera"\nandroid:required="false" />\n<uses-feature\nandroid:name="android.hardware.telephony"\nandroid:required="false" />'
MANIFEST2 ='\n<application\n android:allowBackup="true"\n android:dataExtractionRules="@xml/data_extraction_rules"\n android:fullBackupContent="@xml/backup_rules"\n android:icon="@mipmap/ic_launcher"\n android:label="@string/app_name"\n android:roundIcon="@mipmap/ic_launcher_round"\n android:supportsRtl="true"\n android:theme="@style/Theme.TFG"> \n<activity\nandroid:name=".RevocarPermisos"\nandroid:exported="false" /> \n<activity\nandroid:name=".GruposNoSys"\nandroid:exported="false" /> \n<activity\nandroid:name=".Phone"\nandroid:exported="false" /> \n<activity\nandroid:name=".Grupos"\nandroid:exported="false" /> \n<activity\nandroid:name=".Permisos"\nandroid:exported="false" /> \n<activity\nandroid:name=".Inicio"\nandroid:exported="true">\n<intent-filter>  \n<action android:name="android.intent.action.MAIN" />  \n<category android:name="android.intent.category.LAUNCHER" />\n</intent-filter>\n<meta-data\n  android:name="android.app.lib_name"\n  android:value="" />\n </activity>\n    </application>\n\n</manifest>'
ESQUEMA_NUEVO_PERMISO = '<permission\nandroid:name="XXXX"\nandroid:protectionLevel="XXXX"\nandroid:permissionGroup="XXXX"\nandroid:description="@string/descripción_generica"/>'
ESQUEMA_NUEVO_GRUPO = '<permission-group\nandroid:name="App-perm.GRUPO"\nandroid:description="@string/descripcion_grupo_general"\nandroid:label="@string/grupo_general" />'

class ManifestMod:
    manifest = None
    def getManifest1(self):
        return MANIFEST1
    def getManifest2(self):
        return MANIFEST2
    def getNuevoPermiso(self):
        return ESQUEMA_NUEVO_PERMISO
    def getNuevoGrupo(self):
        return ESQUEMA_NUEVO_GRUPO
    def setManifest(self,manifest):
        self.manifest = manifest
        return
    def getManifest(self):
        return self.manifest