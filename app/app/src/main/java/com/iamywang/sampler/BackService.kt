// ============================================================================
// This file is part of EavesDroid.
//
// Author: iamywang
// Date Created: Jan 27, 2024
// ============================================================================
package com.iamywang.sampler

import android.app.Service
import android.content.Intent
import android.os.Build
import android.os.IBinder
import com.alibaba.fastjson.JSON
import com.alibaba.fastjson.JSONObject
import java.util.*

import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import java.io.IOException


class BackService : Service() {

    private external fun sysinfo_procs(): Int
    private external fun statvfs_f_bavail(): Long
    private external fun sysconf_avphys_pages(): Long
    private external fun statvfs_f_ffree(): Long
    private external fun sysinfo_freeram(): Long
    private external fun sysinfo_sharedram(): Long
    private external fun get_avphys_pages(): Long


    override fun onBind(arg0: Intent): IBinder? {
        return null
    }

    override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {
        // new Thread
        val thread = Thread {
            val time = Date().toString()
            val total = 5000L
            val init = System.currentTimeMillis()
            var i = 0L

            var vs1 = ""
            var vs2 = ""
            var vs3 = ""
            var vs4 = ""
            var vs5 = ""
            // var vs6 = ""
            // var vs7 = ""

            val model = Build.MODEL
            val manufacturer = Build.MANUFACTURER
            val brand = Build.BRAND
            val version = Build.VERSION.RELEASE
            val sdk = Build.VERSION.SDK_INT

            while (true) {
                val t = System.currentTimeMillis() - init
                if (t > i) {
                    val v1 = sysinfo_procs()
                    val v2 = statvfs_f_bavail()
                    val v3 = sysconf_avphys_pages()
                    val v4 = statvfs_f_ffree()
                    val v5 = sysinfo_freeram()
                    // val v6 = sysinfo_sharedram()
                    // val v7 = get_avphys_pages()

                    vs1 += "$v1,"
                    vs2 += "$v2,"
                    vs3 += "$v3,"
                    vs4 += "$v4,"
                    vs5 += "$v5,"
                    // vs6 += "$v6,"
                    // vs7 += "$v7,"
                    i++

                    if (t > total - 1) {
                        vs1 += "$v1"
                        vs2 += "$v2"
                        vs3 += "$v3"
                        vs4 += "$v4"
                        vs5 += "$v5"
                        // vs6 += "$v6"
                        // vs7 += "$v7"

                        val api = "http://10.201.170.123:8000"
                        val obj = JSONObject()
                        obj["model"] = "$manufacturer $brand $model"
                        obj["version"] = "$version $sdk"
                        obj["time"] = time
                        obj["vs1"] = vs1
                        obj["vs2"] = vs2
                        obj["vs3"] = vs3
                        obj["vs4"] = vs4
                        obj["vs5"] = vs5
                        // obj["vs6"] = vs6
                        // obj["vs7"] = vs7

                        val okHttpClient = OkHttpClient()
                        val mediaType = "application/json; charset=utf-8".toMediaType()
                        val requestBody = JSON.toJSONString(obj).toRequestBody(mediaType)
                        val request = Request.Builder()
                            .url("$api/upload/")
                            .post(requestBody)
                            .build()
                        okHttpClient.newCall(request).enqueue(object : Callback {
                            override fun onFailure(call: Call, e: IOException) {
                                println("failed")
                            }

                            override fun onResponse(call: Call, response: Response) {
                                println("success")
                            }
                        })
                        break
                    }
                }
            }
        }

        // start thread
        thread.start()

        return START_STICKY
    }
}
