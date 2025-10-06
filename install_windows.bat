@echo off
REM StreamForge-Pro Windows Installer
REM Created by RAJSARASWATI JATAV
REM Copyright (c) 2025 RAJSARASWATI JATAV

echo.
echo ========================================
echo  StreamForge-Pro Windows Installer
echo  Created by RAJSARASWATI JATAV
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Check pip
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip not found!
    pause
    exit /b 1
)

echo [OK] pip found
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements_complete.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                    ✅ INSTALLATION COMPLETE                   ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 🚀 Quick Start:
echo    python streamforge_hacker.py
echo.
echo 📖 Full Guide: type WINDOWS_COMPLETE_GUIDE.md
echo.
echo 🎯 Create Desktop Shortcut:
echo    Right-click streamforge_hacker.py ^> Send to ^> Desktop
echo.
echo © 2025 RAJSARASWATI JATAV - Gwalior, India
echo.
pause
