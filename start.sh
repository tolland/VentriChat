#!/bin/bash

# VentriChat Quick Start Script

echo "🎭 Starting VentriChat..."

# Check for uv and hatch
USE_MODERN_TOOLS=false
if command -v uv &> /dev/null && command -v hatch &> /dev/null; then
    USE_MODERN_TOOLS=true
    echo "✨ Using modern tools (uv + hatch)"
else
    echo "Using traditional tools (venv + pip)"
    echo "💡 Tip: Install uv for faster setup: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

# Setup backend
if [ "$USE_MODERN_TOOLS" = true ]; then
    if [ ! -f "backend/.venv/bin/activate" ] && [ ! -f "backend/pyproject.toml" ]; then
        echo "Installing backend dependencies with uv..."
        cd backend
        uv sync
        cd ..
    fi
else
    if [ ! -d "backend/venv" ]; then
        echo "Creating Python virtual environment..."
        cd backend
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        cd ..
    fi
fi

# Check if node_modules exists
if [ ! -d "frontend/node_modules" ]; then
    echo "Installing frontend dependencies..."
    cd frontend
    npm install
    cd ..
fi

# Start backend in background
echo "Starting backend server..."
cd backend
if [ "$USE_MODERN_TOOLS" = true ]; then
    hatch run dev &
    BACKEND_PID=$!
else
    source venv/bin/activate
    python main.py &
    BACKEND_PID=$!
fi
cd ..

# Wait for backend to start
sleep 3

# Start frontend
echo "Starting frontend dev server..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ VentriChat is running!"
echo "   Frontend: http://localhost:5173"
echo "   Backend:  http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop all servers..."

# Trap Ctrl+C to kill both processes
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT

# Wait for processes
wait
