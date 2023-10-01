class PermisosMod:
    PERMISOS = [
        "DELIVER_COMPANION_MESSAGES;-;Normal",
        "HIDE_OVERLAY_WINDOWS;-;Normal",
        "READ_ASSISTANT_APP_SEARCH_DATA;-;Internal",
        "READ_BASIC_PHONE_STATE;-;Normal",
        "READ_HOME_APP_SEARCH_DATA;-;Internal",
        "USE_EXACT_ALARM;-;Normal",
        "ACCESS_BACKGROUND_LOCATION;LOCATION;Dangerous",
        "ACCESS_COARSE_LOCATION;LOCATION;Dangerous",
        "ACCESS_FINE_LOCATION;LOCATION;Dangerous",
        "ACCESS_MEDIA_LOCATION;READ_MEDIA_VISUAL;Dangerous",
        "ACTIVITY_RECOGNITION;ACTIVITY_RECOGNITION;Dangerous",
        "ADD_VOICEMAIL;PHONE;Dangerous",
        "ANSWER_PHONE_CALLS;PHONE;Dangerous",
        "BLUETOOTH_ADVERTISE;NEARBY_DEVICES;Dangerous",
        "ACCEPT_HANDOVER;PHONE;Dangerous",
        "BLUETOOTH_CONNECT;NEARBY_DEVICES;Dangerous",
        "BLUETOOTH_SCAN;NEARBY_DEVICES;Dangerous",
        "BODY_SENSORS;SENSORS;Dangerous",
        "BODY_SENSORS_BACKGROUND;SENSORS;Dangerous",
        "CALL_PHONE;PHONE;Dangerous",
        "UNINSTALL_SHORTCUT;-;Normal",
        "REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE;-;Normal",
        "REQUEST_COMPANION_PROFILE_AUTOMOTIVE_PROJECTION;-;Internal",
        "CAMERA;CAMERA;Dangerous",
        "GET_ACCOUNTS;CONTACTS;Dangerous",
        "POST_NOTIFICATIONS;NOTIFICATIONS;Dangerous",
        "READ_CALENDAR;CALENDAR;Dangerous",
        "READ_MEDIA_IMAGES;READ_MEDIA_VISUAL;Dangerous",
        "READ_MEDIA_AUDIO;READ_MEDIA_AURAL;Dangerous",
        "READ_CALL_LOG;CALL_LOG;Dangerous",
        "READ_EXTERNAL_STORAGE;STORAGE;Dangerous",
        "NEARBY_WIFI_DEVICES;NEARBY_DEVICES;Dangerous",
        "READ_CONTACTS;CONTACTS;Dangerous",
        "READ_MEDIA_VIDEO;READ_MEDIA_VISUAL;Dangerous",
        "READ_PHONE_NUMBERS;PHONE;Dangerous",
        "READ_PHONE_STATE;PHONE;Dangerous",
        "READ_SMS;SMS;Dangerous",
        "RECEIVE_MMS;SMS;Dangerous",
        "RECEIVE_SMS;SMS;Dangerous",
        "RECEIVE_WAP_PUSH;SMS;Dangerous",
        "RECORD_AUDIO;MICROPHONE;Dangerous",
        "SEND_SMS;SMS;Dangerous",
        "UWB_RANGING;NEARBY_DEVICES;Dangerous",
        "WRITE_CALL_LOG;CALL_LOG;Dangerous",
        "WRITE_CALENDAR;CALENDAR;Dangerous",
        "WRITE_EXTERNAL_STORAGE;STORAGE;Dangerous",
        "WRITE_CONTACTS;CONTACTS;Dangerous",
        "USE_SIP;PHONE;Dangerous",
        "ACCESS_LOCATION_EXTRA_COMMANDS;-;Normal",
        "ACCESS_NETWORK_STATE;-;Normal",
        "ACCESS_NOTIFICATION_POLICY;-;Normal",
        "ACCESS_WIFI_STATE;-;Normal",
        "BLUETOOTH;-;Normal",
        "BLUETOOTH_ADMIN;-;Normal",
        "BROADCAST_STICKY;-;Normal",
        "CALL_COMPANION_APP;-;Normal",
        "CHANGE_NETWORK_STATE;-;Normal",
        "CHANGE_WIFI_MULTICAST_STATE;-;Normal",
        "CHANGE_WIFI_STATE;-;Normal",
        "DISABLE_KEYGUARD;-;Normal",
        "EXPAND_STATUS_BAR;-;Normal",
        "GET_PACKAGE_SIZE;-;Normal",
        "INSTALL_SHORTCUT;-;Normal",
        "INTERNET;-;Normal",
        "KILL_BACKGROUND_PROCESSES;-;Normal",
        "HIGH_SAMPLING_RATE_SENSORS;-;Normal",
        "MANAGE_OWN_CALLS;-;Normal",
        "MODIFY_AUDIO_SETTINGS;-;Normal",
        "NFC;-;Normal",
        "NFC_TRANSACTION_EVENT;-;Normal",
        "READ_SYNC_SETTINGS;-;Normal",
        "RECEIVE_BOOT_COMPLETED;-;Normal",
        "READ_SYNC_STATS;-;Normal",
        "FOREGROUND_SERVICE;-;Normal",
        "NFC_PREFERRED_PAYMENT_INFO;-;Normal",
        "QUERY_ALL_PACKAGES;-;Normal",
        "REQUEST_COMPANION_PROFILE_WATCH;-;Normal",
        "REORDER_TASKS;-;Normal",
        "REQUEST_COMPANION_RUN_IN_BACKGROUND;-;Normal",
        "REQUEST_COMPANION_USE_DATA_IN_BACKGROUND;-;Normal",
        "REQUEST_DELETE_PACKAGES;-;Normal",
        "REQUEST_IGNORE_BATTERY_OPTIMIZATIONS;-;Normal",
        "REQUEST_PASSWORD_COMPLEXITY;-;Normal",
        "REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND;-;Normal",
        "SET_ALARM;-;Normal",
        "SET_WALLPAPER;-;Normal",
        "SET_WALLPAPER_HINTS;-;Normal",
        "TRANSMIT_IR;-;Normal",
        "UPDATE_PACKAGES_WITHOUT_USER_ACTION;-;Normal",
        "USE_BIOMETRIC;-;Normal",
        "USE_FULL_SCREEN_INTENT;-;Normal",
        "VIBRATE;-;Normal",
        "WAKE_LOCK;-;Normal",
        "WRITE_SYNC_SETTINGS;-;Normal",
        "REQUEST_INSTALL_PACKAGES;-;Signature",
        "MANAGE_EXTERNAL_STORAGE;-;Signature",
        "SCHEDULE_EXACT_ALARM;-;Normal",
        "SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE;-;Internal",
        "SYSTEM_ALERT_WINDOW;-;Signature",
    ]

    def getPermisos(self):
        listaPermisos = []
        for permiso in self.PERMISOS:
            info = permiso.split(sep=";")
            listaPermisos.append(info[0])
        return listaPermisos

    def getPermisosNormales(self):
        normales = ""
        for permiso in self.PERMISOS:
            permiso = permiso.split(sep=";")
            if permiso[2] == "Normal":
                normales += permiso[0]+"\n"
        return normales
    def getPermisosDangerous(self):
        dangerous = ""
        for permiso in self.PERMISOS:
            permiso = permiso.split(sep=";")
            if permiso[2] == "Dangerous":
                dangerous += permiso[0]+"\n"
        return dangerous

    def getPermisosSignature(self):
        signature = ""
        for permiso in self.PERMISOS:
            permiso = permiso.split(sep=";")
            if permiso[2] == "Signature":
                signature += permiso[0]+"\n"
        return signature
    def getGrupo(self, permiso):
        for perm in self.PERMISOS:
            perm = perm.split(sep=";")
            if perm[0] == permiso:
                if perm[1] != "-":
                    return perm[1]
                else:
                    return "No pertenece a ningún grupo"
    def getProtection(self,permiso):
        for perm in self.PERMISOS:
            perm = perm.split(sep=";")
            if perm[0] == permiso:
                return perm[2]
