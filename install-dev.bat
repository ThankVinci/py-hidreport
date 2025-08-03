@echo off

if exist ".\install-dev\build" (
    @rmdir /Q /S ".\install-dev\build"
)

pip install ./install-dev
pause