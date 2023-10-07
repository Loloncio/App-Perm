package com.example.appPerm

import android.Manifest
import android.content.pm.PermissionGroupInfo

class Modelo constructor() {
    private var permisos = arrayOf(
        Manifest.permission.ACCEPT_HANDOVER,
        Manifest.permission.ACCESS_COARSE_LOCATION,
        Manifest.permission.ACCESS_FINE_LOCATION,
        Manifest.permission.ACCESS_MEDIA_LOCATION,
        Manifest.permission.ACTIVITY_RECOGNITION,
        Manifest.permission.ADD_VOICEMAIL,
        Manifest.permission.ANSWER_PHONE_CALLS,
        Manifest.permission.BLUETOOTH_ADVERTISE,
        Manifest.permission.BLUETOOTH_CONNECT,
        Manifest.permission.BLUETOOTH_SCAN,
        Manifest.permission.BODY_SENSORS,
        Manifest.permission.CALL_PHONE,
        Manifest.permission.CAMERA,
        Manifest.permission.GET_ACCOUNTS,
        Manifest.permission.NEARBY_WIFI_DEVICES,
        Manifest.permission.POST_NOTIFICATIONS,
        Manifest.permission.PROCESS_OUTGOING_CALLS,
        Manifest.permission.READ_CALENDAR,
        Manifest.permission.READ_CALL_LOG,
        Manifest.permission.READ_CONTACTS,
        Manifest.permission.READ_EXTERNAL_STORAGE,
        Manifest.permission.READ_MEDIA_AUDIO,
        Manifest.permission.READ_MEDIA_IMAGES,
        Manifest.permission.READ_MEDIA_VIDEO,
        //Manifest.permission.READ_MEDIA_VISUAL_USER_SELECTED,
        Manifest.permission.READ_PHONE_NUMBERS,
        Manifest.permission.READ_PHONE_STATE,
        Manifest.permission.READ_SMS,
        Manifest.permission.RECEIVE_MMS,
        Manifest.permission.RECEIVE_SMS,
        Manifest.permission.RECEIVE_WAP_PUSH,
        Manifest.permission.RECORD_AUDIO,
        Manifest.permission.SEND_SMS,
        Manifest.permission.USE_SIP,
        Manifest.permission.UWB_RANGING,
        Manifest.permission.WRITE_CALENDAR,
        Manifest.permission.WRITE_CALL_LOG,
        Manifest.permission.WRITE_CONTACTS,
        Manifest.permission.WRITE_EXTERNAL_STORAGE,
        )
    private var phone1: Array<String> = arrayOf(
        Manifest.permission.ANSWER_PHONE_CALLS,
        Manifest.permission.READ_PHONE_NUMBERS,
        Manifest.permission.CALL_PHONE,
    )
    private var phone2: Array<String> = arrayOf(
        Manifest.permission.ACCEPT_HANDOVER,
        Manifest.permission.USE_SIP,
        Manifest.permission.ADD_VOICEMAIL
    )
    private var phonePerm = arrayOf(
        Manifest.permission.ANSWER_PHONE_CALLS,
        Manifest.permission.READ_PHONE_NUMBERS,
        Manifest.permission.CALL_PHONE,
        Manifest.permission.ACCEPT_HANDOVER,
        Manifest.permission.USE_SIP,
        Manifest.permission.ADD_VOICEMAIL,
        Manifest.permission.READ_PHONE_STATE
    )
    private lateinit var grupos: MutableList<PermissionGroupInfo>

    constructor(grupos: MutableList<PermissionGroupInfo>) : this() {
        this.grupos = grupos
    }

    fun getPermisos(): Array<String> {
        return permisos
    }

    fun getGrupos(): MutableList<PermissionGroupInfo> {
        return grupos
    }

    fun getPhonePerm(): Array<String> {
        return phonePerm
    }

    fun getPhone1(): Array<String> {
        return phone1
    }

    fun getPhone2(): Array<String> {
        return phone2
    }
}