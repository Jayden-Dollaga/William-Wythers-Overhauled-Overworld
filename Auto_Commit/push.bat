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
echo Project: %PROJECT_DIR%
echo Branch: %CURRENT_BRANCH%

echo.
echo Last commit:
git log -1 --oneline

echo.
echo Current changes:
git status --short
echo.
echo Summary:
git diff --shortstat
echo.

set "MSG=%~3"
if not defined MSG (
  if /I "%AUTO_MODE%"=="1" (
    set "MSG=chore: update project"
  ) else (
    set "MSG="
    set /p "MSG=Commit message [chore: update project]: "
    if "!MSG!"=="" set "MSG=chore: update project"
  )
)

echo.
git add .
if errorlevel 1 exit /b 1

git commit -m "!MSG!"
if errorlevel 1 (
  echo Nothing new to commit or commit failed.
  exit /b 0
)
git push origin HEAD
if errorlevel 1 (
  echo Push failed. Check your remote URL and credentials.
  exit /b 1
)
echo Changes pushed successfully.

for /f "delims=" %%R in ('git remote get-url origin 2^>nul') do set "REMOTE_URL=%%R"
if defined REMOTE_URL (
  echo !REMOTE_URL! | findstr /I "github.com" >nul
  if not errorlevel 1 (
    set "GITHUB_URL=!REMOTE_URL:git@github.com:=https://github.com/!"
    set "GITHUB_URL=!GITHUB_URL:git@github.com/:=https://github.com/!"
    set "GITHUB_URL=!GITHUB_URL:.git=!"
    echo Opening repository page...
    start "" "!GITHUB_URL!"
  )
)
echo.
echo Press any key to close this window...
pause >nul
endlocal
exit /b 0
