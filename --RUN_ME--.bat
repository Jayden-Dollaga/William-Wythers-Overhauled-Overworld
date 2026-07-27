@echo off
setlocal
cd /d "%~dp0"

echo.
echo ========================================
echo   Auto Commit Launcher
echo ========================================
echo.
echo Starting Auto Commit tools...
if exist "Auto_Commit\push.bat" (
    start "" cmd /k "cd /d ""%~dp0"" && Auto_Commit\push.bat"
) else (
    echo Auto_Commit folder not found.
    pause
)
endlocal
