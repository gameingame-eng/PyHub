@echo off
cd /d "%~dp0"

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.12 or later from https://www.python.org/
    pause
    exit /b
)

echo.
echo Checking for requirements.txt...
if not exist requirements.txt (
    echo requirements.txt not found!
    echo Please create one with your dependencies.
    pause
    exit /b
)

echo.
echo Installing required Python packages from requirements.txt...

:: Show pip commands while running
echo on
echo by the way, thank you for using PyHub!
python -m pip install -r requirements.txt
@echo off

echo.
echo Running PyHub...
echo on
python main.py
@echo off

echo.
pause
