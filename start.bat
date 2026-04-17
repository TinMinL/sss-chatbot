@echo off
title AI Chatbot Launcher
echo ===================================================
echo   Starting AI Chatbot for Secondary School Students
echo ===================================================
echo.


python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH.
    pause
    exit
)


if not exist backend\.env (
    echo [SETUP] No API Key found. Let's set it up!
    set /p apikey="Please paste your DeepSeek API Key here and press Enter: "
    echo DEEPSEEK_API_KEY=%apikey% > backend\.env
    echo [SUCCESS] Key saved to backend\.env automatically!
    echo.
)

echo [1/3] Installing dependencies and starting Python Backend (Port 5000)...
start "AI Backend Server" cmd /k "cd backend && pip install -r requirements.txt && python app.py"

echo [2/3] Starting Frontend Web Server (Port 8000)...
start "AI Frontend Server" cmd /k "cd frontend && python -m http.server 8000"

echo [3/3] Waiting for servers to initialize...
timeout /t 5 /nobreak >nul

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
