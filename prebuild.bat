@echo off

@call .\version.bat

if exist ".\build\bdist.win32" (
    @rmdir /Q /S ".\build\bdist.win32"
)

if exist ".\build\lib" (
    @rmdir /Q /S ".\build\lib"
)