@echo off
setlocal EnableExtensions EnableDelayedExpansion

color 0A
call "%~dp0common.bat" "%~1"
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
echo Changes:
git diff --shortstat

echo.

set "MSG="
set /p "MSG=Commit message [chore: update project]: "
if "!MSG!"=="" set "MSG=chore: update project"

echo.
echo [1/4] Adding files...
git add .
if errorlevel 1 exit /b 1

echo [2/4] Creating commit...
git commit -m "!MSG!"
if errorlevel 1 (
  echo Nothing new to commit or commit failed.
  exit /b 0
)
echo [3/4] Pushing to remote...
git push origin HEAD
if errorlevel 1 (
  echo Push failed. Check your remote URL and credentials.
  exit /b 1
)
echo [4/4] Done.
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
endlocal
