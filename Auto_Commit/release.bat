@echo off
setlocal EnableExtensions EnableDelayedExpansion

color 0A
call "%~dp0common.bat" "%~1"
if errorlevel 1 exit /b %errorlevel%
if not defined PROJECT_DIR set "PROJECT_DIR=%CD%"
cd /d "%PROJECT_DIR%" >nul 2>&1

echo.
echo Branch: %CURRENT_BRANCH%
echo Last commit: %LAST_COMMIT%

echo.
set "TAG="
set /p "TAG=Release tag [v1.0.0]: "
if "!TAG!"=="" set "TAG=v1.0.0"

echo.
echo Creating release tag !TAG!...
git tag "!TAG!"
if errorlevel 1 (
  echo Tag already exists or creation failed.
  exit /b 1
)
git push origin "!TAG!"
if errorlevel 1 exit /b 1

echo Release tag pushed.
endlocal
