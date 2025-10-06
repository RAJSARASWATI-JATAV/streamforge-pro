@echo off
echo ========================================
echo StreamForge-Pro Browser Extension Setup
echo ========================================
echo.

echo Installing advanced features dependencies...
pip install -r requirements_advanced.txt

echo.
echo ========================================
echo Chrome Extension Setup:
echo ========================================
echo 1. Open Chrome and go to: chrome://extensions/
echo 2. Enable "Developer mode" (top right)
echo 3. Click "Load unpacked"
echo 4. Navigate to: %CD%\src\streamforge\extensions\chrome
echo 5. Select the folder and click "Select Folder"
echo.

echo ========================================
echo Firefox Extension Setup:
echo ========================================
echo 1. Open Firefox and go to: about:debugging
echo 2. Click "This Firefox"
echo 3. Click "Load Temporary Add-on"
echo 4. Navigate to: %CD%\src\streamforge\extensions\firefox
echo 5. Select manifest.json
echo.

echo ========================================
echo Extension files location:
echo %CD%\src\streamforge\extensions\
echo ========================================
echo.

pause
