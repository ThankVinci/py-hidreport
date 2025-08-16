@echo off

@call .\prebuild.bat
set ALPHA_VER=
set PKG_VERSION=%FULL_VER%%ALPHA_VER%

python -m pip install --upgrade pip build setuptools wheel
python -m build --wheel

pause