[app]
title = MyApp
package.name = myapp
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy
android.archs = arm64-v8a
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk = 25b

android.permissions = INTERNET
