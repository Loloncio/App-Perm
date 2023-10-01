class GruposMod:

    GRUPOS = {
        "PHONE":["ANSWER_PHONE_CALLS", "READ_PHONE_NUMBERS", "READ_PHONE_STATE", "CALL_PHONE", "ACCEPT_HANDOVER", "USE_SIP", "ADD_VOICEMAIL"],
        "CONTACTS":["WRITE_CONTACTS", "GET_ACCOUNTS", "READ_CONTACTS"],
        "CALL_LOG":["READ_CALL_LOG", "WRITE_CALL_LOG", "PROCESS_OUTGOING_CALLS"],
        "READ_MEDIA_VISUAL":["READ_MEDIA_IMAGES", "READ_MEDIA_VIDEO", "ACCESS_MEDIA_LOCATION"],
        "READ_MEDIA_AURAL":["READ_MEDIA_AUDIO"],
        "CAR_INFORMATION":["No hay permisos"],
        "ACTIVITY_RECOGNITION":["ACTIVITY_RECOGNITION"],
        "UNDEFINED":["No hay permisos"],
        "SENSORS":["BODY_SENSORS", "BODY_SENSORS_BACKGROUND"],
        "STORAGE":["READ_EXTERNAL_STORAGE", "WRITE_EXTERNAL_STORAGE"],
        "NOTIFICATIONS":["POST_NOTIFICATIONS"],
        "LOCATION":["ACCESS_FINE_LOCATION", "ACCESS_COARSE_LOCATION", "ACCESS_BACKGROUND_LOCATION"],
        "CALENDAR":["READ_CALENDAR", "WRITE_CALENDAR"],
        "CAMERA":["CAMERA", "BACKGROUND_CAMERA"],
        "MICROPHONE":["RECORD_BACKGROUND_AUDIO", "RECORD_AUDIO"],
        "NEARBY_DEVICES":["NEARBY_WIFI_DEVICES", "BLUETOOTH_CONNECT", "BLUETOOTH_ADVERTISE", "UWB_RANGING", "BLUETOOTH_SCAN"],
        "SMS":["READ_SMS", "RECEIVE_WAP_PUSH", "RECEIVE_MMS", "RECEIVE_SMS", "SEND_SMS", "READ_CELL_BROADCASTS"]
    }

    def getGrupos(self):
        return self.GRUPOS.keys()

    def getPermisos(self, grupo):
        return self.GRUPOS.get(grupo)