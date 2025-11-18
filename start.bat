@echo off
REM VentriChat Quick Start Script for Windows

echo 🎭 Starting VentriChat...

REM Check for required tools
set MISSING_TOOLS=

where uv >nul 2>nul
if %ERRORLEVEL% NEQ 0 set MISSING_TOOLS=%MISSING_TOOLS% uv

where hatch >nul 2>nul
if %ERRORLEVEL% NEQ 0 set MISSING_TOOLS=%MISSING_TOOLS% hatch

where pnpm >nul 2>nul
if %ERRORLEVEL% NEQ 0 set MISSING_TOOLS=%MISSING_TOOLS% pnpm

if NOT "%MISSING_TOOLS%"=="" (
    echo ❌ Missing required tools:%MISSING_TOOLS%
    echo.
    echo Please install the following:
    echo   - uv: https://github.com/astral-sh/uv#installation
    echo   - hatch: pipx install hatch
    echo   - pnpm: https://pnpm.io/installation
    exit /b 1
)

echo ✨ All required tools found

REM Setup backend
if not exist "backend\.venv" (
    echo Installing backend dependencies...
    cd backend
    uv sync
    cd ..
)

REM Setup frontend
if not exist "frontend\node_modules" (
    echo Installing frontend dependencies...
    cd frontend
    pnpm install
    cd ..
)

REM Copy .env if it doesn't exist
if not exist "backend\.env" (
    echo Creating .env file...
    copy backend\.env.example backend\.env
)

REM Start backend
echo Starting backend server...
cd backend
start /B hatch run dev
cd ..

REM Wait for backend to start
timeout /t 3 /nobreak

REM Start frontend
echo Starting frontend dev server...
cd frontend
start /B pnpm dev
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
