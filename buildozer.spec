[app]

# (str) Title of your application
title = Para Allya

# (str) Package name
package.name = paraallya

# (str) Package domain (needed for android packaging)
package.domain = org.allya

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
# NOTA: Kivy 2.3.0 e KivyMD 1.2.0 sao as versoes estaveis perfeitas para o Android
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,sdl2_image,sdl2_ttf

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
