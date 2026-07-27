@echo off
setlocal EnableExtensions EnableDelayedExpansion

color 0A
set "TARGET_DIR=%CD%"
if not "%~1"=="" (
  set "TARGET_DIR=%~f1"
)

for %%I in ("%TARGET_DIR%") do set "TARGET_DIR=%%~fI"

cd /d "%TARGET_DIR%" >nul 2>&1
if errorlevel 1 (
  echo ERROR: Could not access folder "%TARGET_DIR%".
  exit /b 1
)

echo.
echo ========================================
echo   Git Helper Suite
echo ========================================

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo.
  echo This folder is not a Git repository yet.
  set /p "INIT=Initialize it now? [Y/n]: "
  if /I "!INIT!"=="" set "INIT=Y"
  if /I "!INIT!"=="Y" (
    git init
    if errorlevel 1 (
      echo ERROR: Git init failed.
      exit /b 1
    )
    echo Git repository initialized.
  ) else (
    echo Aborted. Run this again after connecting a Git repository.
    exit /b 0
  )
)

for /f "delims=" %%R in ('git remote get-url origin 2^>nul') do set "REMOTE_URL=%%R"
if not defined REMOTE_URL (
  echo.
  echo No remote repository is connected yet.
  set /p "REMOTE_URL=Enter a Git remote URL (GitHub/SSH) or leave blank to skip: "
  if not "!REMOTE_URL!"=="" (
    git remote add origin "!REMOTE_URL!"
    echo Remote connected as origin.
  ) else (
    echo Remote was not set. You can connect it later.
  )
)

for /f "delims=" %%N in ('git config user.name 2^>nul') do set "USER_NAME=%%N"
if not defined USER_NAME (
  set /p "USER_NAME=Enter your Git display name: "
  if not "!USER_NAME!"=="" git config user.name "!USER_NAME!"
)

for /f "delims=" %%E in ('git config user.email 2^>nul') do set "USER_EMAIL=%%E"
if not defined USER_EMAIL (
  set /p "USER_EMAIL=Enter your Git email: "
  if not "!USER_EMAIL!"=="" git config user.email "!USER_EMAIL!"
)

for /f "delims=" %%B in ('git branch --show-current 2^>nul') do set "CURRENT_BRANCH=%%B"
if not defined CURRENT_BRANCH set "CURRENT_BRANCH=detached"

for /f "delims=" %%L in ('git log -1 --oneline 2^>nul') do set "LAST_COMMIT=%%L"
if not defined LAST_COMMIT set "LAST_COMMIT=No commits yet"

endlocal & set "PROJECT_DIR=%TARGET_DIR%" & set "CURRENT_BRANCH=%CURRENT_BRANCH%" & set "LAST_COMMIT=%LAST_COMMIT%"
