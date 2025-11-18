#!/bin/bash

# VentriChat Quick Start Script

set -e  # Exit on error

echo "🎭 Starting VentriChat..."

# Check for required tools
MISSING_TOOLS=()

if ! command -v uv &> /dev/null; then
    MISSING_TOOLS+=("uv")
fi

if ! command -v hatch &> /dev/null; then
    MISSING_TOOLS+=("hatch")
fi

if ! command -v pnpm &> /dev/null; then
    MISSING_TOOLS+=("pnpm")
fi

if [ ${#MISSING_TOOLS[@]} -ne 0 ]; then
    echo "❌ Missing required tools: ${MISSING_TOOLS[*]}"
    echo ""
    echo "Please install the following:"
    for tool in "${MISSING_TOOLS[@]}"; do
        case $tool in
            uv)
                echo "  - uv: https://github.com/astral-sh/uv#installation"
                ;;
            hatch)
                echo "  - hatch: pipx install hatch"
                ;;
            pnpm)
                echo "  - pnpm: https://pnpm.io/installation"
                ;;
        esac
    done
    exit 1
fi

echo "✨ All required tools found"

# Setup backend
if [ ! -d "backend/.venv" ]; then
    echo "Installing backend dependencies..."
    cd backend
    uv sync
    cd ..
fi

# Setup frontend
if [ ! -d "frontend/node_modules" ]; then
    echo "Installing frontend dependencies..."
    cd frontend
    pnpm install
    cd ..
fi

# Copy .env if it doesn't exist
if [ ! -f "backend/.env" ]; then
    echo "Creating .env file..."
    cp backend/.env.example backend/.env
fi

# Start backend in background
echo "Starting backend server..."
cd backend
hatch run dev &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start frontend
echo "Starting frontend dev server..."
cd frontend
pnpm dev &
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
