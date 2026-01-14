@echo off
REM Pre-deployment checker for TikTok Downloader
REM Verifies that there are no uncommitted changes before deployment

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo 🚀 TikTok Downloader - Pre-Deployment Check
echo ============================================================
echo.

set FORCE_MODE=false
set GIT_OK=true

REM Check for --force flag
for %%a in (%*) do (
    if "%%a"=="--force" set FORCE_MODE=true
    if "%%a"=="-f" set FORCE_MODE=true
)

REM Check if git is available
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Git not found. Skipping git checks.
    goto check_python
)

REM Check if we're in a git repository
git rev-parse --git-dir >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Not a git repository. Skipping git checks.
    goto check_python
)

REM Check for uncommitted changes
git status --porcelain > nul
for /f %%i in ('git status --porcelain ^| find /c /v ""') do set COUNT=%%i

if !COUNT! gtr 0 (
    echo ❌ Uncommitted changes detected!
    echo.
    echo The following files have uncommitted changes:
    git status --short
    echo.
    echo ============================================================
    echo Options:
    echo   1. Commit changes: git add . ^&^& git commit -m "Your message"
    echo   2. Stash changes: git stash
    echo   3. Proceed anyway: Use --force flag
    echo ============================================================
    set GIT_OK=false
) else (
    echo ✅ No uncommitted changes detected. Safe to proceed.
    set GIT_OK=true
)

:check_python
REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.8 or higher.
    goto failed
)

echo ✅ Python is installed.

echo.
echo ============================================================

if "!GIT_OK!"=="false" if "!FORCE_MODE!"=="false" (
    echo ❌ Deployment check FAILED: Uncommitted changes detected
    echo    Commit your changes or use --force to proceed anyway
    echo ============================================================
    echo.
    exit /b 1
)

if "!FORCE_MODE!"=="true" if "!GIT_OK!"=="false" (
    echo ⚠️  Proceeding with deployment despite uncommitted changes (forced^)
) else (
    echo ✅ All checks passed! Ready for deployment
)

echo ============================================================
echo.
exit /b 0

:failed
echo ============================================================
echo.
exit /b 1
