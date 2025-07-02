#!/bin/bash

# Activate virtual env Flask
cd backend
source env/bin/activate
echo "Starting Flask backend..."
python app.py &
BACKEND_PID=$!
cd ..

# Lauching Frontend
cd frontend
echo "Staring React (Vite) frontend..."
npm run dev &
FRONTEND_PID=$!
cd ..

# Kill process at the end
trap "kill $BACKEND_PID $FRONTEND_PID" EXIT
wait