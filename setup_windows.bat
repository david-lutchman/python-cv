@echo off
setlocal ENABLEDELAYEDEXPANSION

echo ============================================
echo Python Resume Generator - Windows Setup
echo ============================================

:: Check for Python
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Python already installed.
    goto INSTALL_LIBS
)

echo Python not found. Installing Python...

:: Download Python installer
set PYTHON_URL=https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe
set PYTHON_EXE=%TEMP%\python-installer.exe

powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %PYTHON_EXE%"

:: Install Python silently and add to PATH
%PYTHON_EXE% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

if %ERRORLEVEL% NEQ 0 (
    echo Python installation failed.
    exit /b 1
)

echo Python installed successfully.

:INSTALL_LIBS
echo Installing Python dependencies...

python -m pip install --upgrade pip
python -m pip install reportlab

if %ERRORLEVEL% NEQ 0 (
    echo Failed to install Python dependencies.
    exit /b 1
)

echo ============================================
echo Setup complete.
echo You can now run: python generate_resume.py
echo ============================================

endlocal
pause
