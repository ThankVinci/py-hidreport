@echo off

set MAJOR_VER=1
set MINOR_VER=0
set BUILD_VER=0
set FULL_VER=%MAJOR_VER%.%MINOR_VER%.%BUILD_VER%

if exist ".\build\bdist.win32" (
    @rmdir /Q /S ".\build\bdist.win32"
)

if exist ".\build\lib" (
    @rmdir /Q /S ".\build\lib"
)