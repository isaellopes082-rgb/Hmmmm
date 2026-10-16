[app]

title = Para Allya
package.name = paraallya
package.domain = org.allya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Dependências corretas do Kivy + KivyMD para Android:
requirements = python3,kivy==2.3.0,kivymd==1.2.0

orientation = portrait
fullscreen = 0

# Android SDK e NDK configurados para estabilidade:
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
