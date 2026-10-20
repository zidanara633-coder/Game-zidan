[app]
title = Game Zidan
package.name = gamezidan
package.domain = org.zidan

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3,ttf

version = 0.1
requirements = python3,pygame

orientation = landscape
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
