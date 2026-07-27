@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0"

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
set "CHOICE=%~1"
if not defined CHOICE set /p "CHOICE=Select an option [1-6]: "

if /I "!CHOICE!"=="1" (
    call "%~dp0Auto_Commit\status.bat" "" "--noninteractive"
    goto :done
) else if /I "!CHOICE!"=="2" (
    call "%~dp0Auto_Commit\commit.bat" "" "--noninteractive"
    goto :done
) else if /I "!CHOICE!"=="3" (
    call "%~dp0Auto_Commit\push.bat" "" "--noninteractive"
    goto :done
) else if /I "!CHOICE!"=="4" (
    call "%~dp0Auto_Commit\release.bat" "" "--noninteractive"
    goto :done
) else if /I "!CHOICE!"=="5" (
    call "%~dp0Auto_Commit\backup.bat" "" "--noninteractive"
    goto :done
) else if /I "!CHOICE!"=="6" (
    echo Exiting.
    goto :done
) else (
    echo Invalid option.
)

:done
exit /b 0
