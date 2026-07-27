@echo off
setlocal EnableExtensions EnableDelayedExpansion
set "ROOT=%~dp0"

:menu
cls
echo.
echo ================================
echo   Git Helper Suite
echo ================================
echo.
echo 1. Status
echo 2. Commit
echo 3. Push
echo 4. Release
echo 5. Backup
echo 6. Exit
echo.
set /p "CHOICE=Select an option [1-6]: "

if /I "!CHOICE!"=="1" (
    start "Git Status" cmd /c "cd /d ""!ROOT!"" && Auto_Commit\status.bat"
) else if /I "!CHOICE!"=="2" (
    start "Git Commit" cmd /c "cd /d ""!ROOT!"" && Auto_Commit\commit.bat"
) else if /I "!CHOICE!"=="3" (
    start "Git Push" cmd /c "cd /d ""!ROOT!"" && Auto_Commit\push.bat"
) else if /I "!CHOICE!"=="4" (
    start "Git Release" cmd /c "cd /d ""!ROOT!"" && Auto_Commit\release.bat"
) else if /I "!CHOICE!"=="5" (
    start "Git Backup" cmd /c "cd /d ""!ROOT!"" && Auto_Commit\backup.bat"
) else if /I "!CHOICE!"=="6" (
    echo Exiting.
    goto :done
) else (
    echo Invalid option.
)

goto :menu

:done
endlocal
exit /b 0
