// ============================================================================
// This file is part of EavesDroid.
//
// Author: iamywang
// Date Created: Jan 27, 2024
// ============================================================================
#include <jni.h>
#include <string>
#include <sys/sysinfo.h>
#include <sys/statvfs.h>
#include <unistd.h>

extern "C" JNIEXPORT jint JNICALL
Java_com_iamywang_sampler_BackService_sysinfo_1procs(JNIEnv *env, jobject thiz) {
    struct sysinfo info{};
    sysinfo(&info);
    return info.procs;
}

extern "C" JNIEXPORT jlong JNICALL
Java_com_iamywang_sampler_BackService_statvfs_1f_1bavail(JNIEnv *env, jobject thiz) {
    struct statvfs st{};
    statvfs("/sdcard", &st);
    return st.f_bavail;
}

extern "C"
JNIEXPORT jlong JNICALL
Java_com_iamywang_sampler_BackService_sysconf_1avphys_1pages(JNIEnv *env, jobject thiz) {
    return sysconf(_SC_AVPHYS_PAGES);
}

extern "C"
JNIEXPORT jlong JNICALL
Java_com_iamywang_sampler_BackService_statvfs_1f_1ffree(JNIEnv *env, jobject thiz) {
    struct statvfs st{};
    statvfs("/sdcard", &st);
    return st.f_ffree;
}

extern "C" JNIEXPORT jlong JNICALL
Java_com_iamywang_sampler_BackService_sysinfo_1freeram(JNIEnv *env, jobject thiz) {
    struct sysinfo info{};
    sysinfo(&info);
    return info.freeram;
}

extern "C" JNIEXPORT jlong JNICALL
Java_com_iamywang_sampler_BackService_sysinfo_1sharedram(JNIEnv *env, jobject thiz) {
    struct sysinfo info{};
    sysinfo(&info);
    return info.sharedram;
}

extern "C" JNIEXPORT jlong JNICALL
Java_com_iamywang_sampler_BackService_get_1avphys_1pages(JNIEnv *env, jobject thiz) {
    return get_avphys_pages();
}
