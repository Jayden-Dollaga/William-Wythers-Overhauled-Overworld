@echo off
setlocal EnableExtensions EnableDelayedExpansion

color 0A
call "%~dp0common.bat" "%~1"
if errorlevel 1 exit /b %errorlevel%
if not defined PROJECT_DIR set "PROJECT_DIR=%CD%"
cd /d "%PROJECT_DIR%" >nul 2>&1

set "BACKUP_DIR=%PROJECT_DIR%\Backups"
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%" >nul 2>&1

for %%I in ("%PROJECT_DIR%") do set "PROJECT_NAME=%%~nxI"
for /f "delims=" %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "STAMP=%%I"
set "ARCHIVE_PATH=%BACKUP_DIR%\%PROJECT_NAME%_%STAMP%.zip"

echo.
echo Creating backup...
powershell -NoProfile -Command "& { $proj = [System.IO.Path]::GetFullPath(\"%PROJECT_DIR%\"); $backupDir = [System.IO.Path]::GetFullPath(\"%BACKUP_DIR%\"); if (-not (Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir -Force | Out-Null }; $items = Get-ChildItem $proj -Force | Where-Object { $_.Name -ne 'Backups' -and $_.Name -ne '.git' }; if ($items) { Compress-Archive -LiteralPath $items.FullName -DestinationPath \"%ARCHIVE_PATH%\" -CompressionLevel Optimal -Force; Write-Output \"Backup created: %ARCHIVE_PATH%\" } else { Write-Output 'No files to backup.' } }"

if errorlevel 1 exit /b 1

echo Backup created: %ARCHIVE_PATH%
echo.
echo Press any key to close this window...
pause >nul
endlocal
exit /b 0
