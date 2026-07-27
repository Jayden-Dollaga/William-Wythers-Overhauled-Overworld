@echo off
setlocal EnableExtensions EnableDelayedExpansion

color 0A
set "AUTO_MODE=0"
if /I "%~2"=="--noninteractive" set "AUTO_MODE=1"
call "%~dp0common.bat" "%~1" "%~2"
if errorlevel 1 exit /b %errorlevel%
if not defined PROJECT_DIR set "PROJECT_DIR=%CD%"
cd /d "%PROJECT_DIR%" >nul 2>&1

echo.
echo Branch: %CURRENT_BRANCH%
echo Last commit: %LAST_COMMIT%

echo.
set "TAG=%~3"
if not defined TAG (
  if /I "%AUTO_MODE%"=="1" (
    set "TAG=v1.0.0"
  ) else (
    set "TAG="
    set /p "TAG=Release tag [v1.0.0]: "
    if "!TAG!"=="" set "TAG=v1.0.0"
  )
)

echo.
echo Creating annotated release tag !TAG!...
git tag -a "!TAG!" -m "Version !TAG!"
if errorlevel 1 (
  echo Tag already exists or creation failed.
  exit /b 1
)
git push origin "!TAG!"
if errorlevel 1 exit /b 1

echo Release tag pushed.
endlocal
exit /b 0
