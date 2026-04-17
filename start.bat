@echo off
title AI Chatbot Launcher
echo ===================================================
echo   Starting AI Chatbot for Secondary School Students
echo ===================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH.
    pause
    exit
)

echo [1/3] Starting Python Backend Server (Port 5000)...
start "AI Backend Server" cmd /k "cd backend && python app.py"

echo [2/3] Starting Frontend Web Server (Port 8000)...
start "AI Frontend Server" cmd /k "cd frontend && python -m http.server 8000"

echo [3/3] Waiting for servers to initialize...
timeout /t 3 /nobreak >nul

echo Launching application in your default browser...
start http://localhost:8000

echo.
echo ===================================================
echo All systems go! 
echo Please keep the two black console windows open while testing.
echo Close them when you are done to stop the servers.
echo ===================================================
echo.
pause
