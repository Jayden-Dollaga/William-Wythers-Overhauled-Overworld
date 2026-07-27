@echo off
setlocal EnableExtensions EnableDelayedExpansion

color 0A
call "%~dp0common.bat" "%~1"
if errorlevel 1 exit /b %errorlevel%
if not defined PROJECT_DIR set "PROJECT_DIR=%CD%"
cd /d "%PROJECT_DIR%" >nul 2>&1

echo.
echo Project: %PROJECT_DIR%
if defined CURRENT_BRANCH (
  echo Branch: %CURRENT_BRANCH%
)
echo.
echo Last commit:
git log -1 --oneline
echo.
echo Changes:
git diff --shortstat
echo.

set "MSG="
set /p "MSG=Commit message [chore: update project]: "
if "!MSG!"=="" set "MSG=chore: update project"

echo.
echo [1/3] Adding files...
git add .
if errorlevel 1 exit /b 1

echo [2/3] Creating commit...
git commit -m "!MSG!"
if errorlevel 1 (
  echo Nothing new to commit or commit failed.
  exit /b 0
)
echo [3/3] Done.
echo Commit created successfully.
endlocal
