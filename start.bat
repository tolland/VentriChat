@echo off
REM VentriChat Quick Start Script for Windows

echo 🎭 Starting VentriChat...

REM Check if virtual environment exists
if not exist "backend\venv" (
    echo Creating Python virtual environment...
    cd backend
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
    cd ..
)

REM Check if node_modules exists
if not exist "frontend\node_modules" (
    echo Installing frontend dependencies...
    cd frontend
    call npm install
    cd ..
)

REM Start backend
echo Starting backend server...
cd backend
call venv\Scripts\activate
start /B python main.py
cd ..

REM Wait for backend to start
timeout /t 3 /nobreak

REM Start frontend
echo Starting frontend dev server...
cd frontend
start /B npm run dev
cd ..

echo.
echo ✅ VentriChat is running!
echo    Frontend: http://localhost:5173
echo    Backend:  http://localhost:8000
echo.
echo Press any key to stop all servers...
pause

REM Kill processes (basic cleanup)
taskkill /F /IM python.exe /T
taskkill /F /IM node.exe /T
