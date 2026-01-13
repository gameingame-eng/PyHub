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
echo Checking Java installation...
where java >nul 2>&1
if %errorlevel% equ 0 (
    set "JAVA_STATUS=True"
    echo Java found.
) else (
    set "JAVA_STATUS=False"
    echo WARNING: YOU CANNOT USE GradeApp, a PyHub feature WITHOUT AN AVAILABLE JAVA INSTALLATION.
    echo It is recommended you do get java
    echo but it is not required unless you would like to use GradeApp
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

echo by the way, thank you for using PyHub!
echo on
python -m pip install -r requirements.txt
@echo off

echo.
echo Running PyHub...
python main.py %JAVA_STATUS%
@echo off

echo.
pause
