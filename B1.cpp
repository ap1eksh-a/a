#include <jni.h>
#include "B1.h" 

extern "C" {
    JNIEXPORT jint JNICALL Java_B1_add(JNIEnv *, jobject, jint a, jint b) {
        return a + b;
    }

    JNIEXPORT jint JNICALL Java_B1_sub(JNIEnv *, jobject, jint a, jint b) {
        return a - b;
    }

    JNIEXPORT jint JNICALL Java_B1_mult(JNIEnv *, jobject, jint a, jint b) {
        return a * b;
    }

    JNIEXPORT jint JNICALL Java_B1_div(JNIEnv *, jobject, jint a, jint b) {
        if (b != 0)
            return a / b;
        else
            return 0; 
    }
}
