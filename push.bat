@echo off
title WWOO Sync + Push

echo.
echo ========================================
echo   WWOO Sync + Push
echo ========================================
echo.

:: Step 1 - Run sync script from root
echo [1/4] Syncing files to organized/...
python3 "%~dp0reorganize_wwoo.py"
if errorlevel 1 (
    echo ERROR: Sync script failed. Aborting.
    pause
    exit /b 1
)

:: Step 2 - Ask for commit message
echo.
set /p MSG="[2/4] Commit message: "
if "%MSG%"=="" set MSG="chore: sync organized folder"

:: Step 3 - Stage and commit inside organized/
echo.
echo [3/4] Staging and committing...
cd "%~dp0organized"
git add .
git commit -m "%MSG%"
if errorlevel 1 (
    echo Nothing new to commit or commit failed.
)

:: Step 4 - Push
echo.
echo [4/4] Pushing to GitHub...
git push origin main
if errorlevel 1 (
    echo ERROR: Push failed. Check your connection or credentials.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Done! Changes are live on GitHub.
echo ========================================
echo.
pause
