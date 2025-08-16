@echo off

@call .\prebuild.bat
set PKG_VERSION=%FULL_VER%

python -m pip install --upgrade pip build setuptools wheel
python -m build --wheel

pause