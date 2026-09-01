[app]

title = KivyTest
package.name = kivytest
package.domain = org.kivytest

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy

android.ndk = 25b
android.api = 33
android.minapi = 21

android.permissions = INTERNET

# 关闭私有库，云端不需要
android.accept_sdk_license = True
