@echo off

@call .\version.bat

set PACK_NAME=".\dist\py_hidreport-%FULL_VER%-py38-none-any.whl"

if exist %PACK_NAME% (
    python -m pip install --upgrade twine
    python -m twine upload --repository testpypi %PACK_NAME%
) else (
    echo Could not found %PACK_NAME%
)

pause
