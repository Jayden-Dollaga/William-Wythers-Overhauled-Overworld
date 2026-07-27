@echo off
setlocal EnableExtensions EnableDelayedExpansion

color 0A
call "%~dp0common.bat" "%~1"
if errorlevel 1 exit /b %errorlevel%
if not defined PROJECT_DIR set "PROJECT_DIR=%CD%"
cd /d "%PROJECT_DIR%" >nul 2>&1

echo.
echo Git status for %PROJECT_DIR%
echo Branch: %CURRENT_BRANCH%
echo Last commit: %LAST_COMMIT%
echo.
git status --short --branch
endlocal
exit /b 0
