@echo off

python -m pip install --upgrade pip build setuptools wheel

if exist ".\build\build" (
    @rmdir /Q /S ".\build\build"
)

cd build && python -m build --wheel && cd ..\
pause