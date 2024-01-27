// ============================================================================
// This file is part of EavesDroid.
//
// Author: iamywang
// Date Created: Jan 27, 2024
// ============================================================================
package com.iamywang.sampler

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.view.View
import android.widget.ListView
import androidx.appcompat.app.AppCompatActivity
import com.alibaba.fastjson.JSON
import com.alibaba.fastjson.JSONObject
import com.iamywang.sampler.databinding.ActivityMainBinding
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import java.io.IOException
import java.util.*

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    private var globalList = LinkedList<ListItem>()

    private val model = Build.MODEL
    private val manufacturer = Build.MANUFACTURER
    private val brand = Build.BRAND
    private val version = Build.VERSION.RELEASE
    private val sdk = Build.VERSION.SDK_INT

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        globalList.add(ListItem(1, "$manufacturer $brand $model", Date().toString()))
        globalList.add(ListItem(2, "Android $version (SDK $sdk)", Date().toString()))

        setList(globalList, binding.mainList)

        val service = Intent(baseContext, BackService::class.java)
        startService(service)
    }

    fun trainNetwork(view: View) {
        val api = "http://192.168.1.2:8000"
        val obj = JSONObject()
        obj["model"] = "$manufacturer $brand $model"
        obj["version"] = "$version $sdk"

        val okHttpClient = OkHttpClient()
        val mediaType = "application/json; charset=utf-8".toMediaType()
        val requestBody = JSON.toJSONString(obj).toRequestBody(mediaType)
        val request = Request.Builder()
            .url("$api/train/")
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
    }

    private fun setList(list: LinkedList<ListItem>, listView: ListView) {
        val mAdapter = ListItemAdapter(list, this)
        listView.adapter = mAdapter
    }

    companion object {
        init {
            System.loadLibrary("sampler")
        }
    }
}