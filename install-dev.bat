@echo off

@call .\prebuild.bat
set DEV_VER=dev0
set PKG_VERSION=%FULL_VER%.%DEV_VER%

pip install . 

pause