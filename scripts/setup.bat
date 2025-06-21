@echo off
echo 🚀 Quick Start Script for AI Profile Assistant Project
echo ==================================

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js first.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python first.
    pause
    exit /b 1
)

echo ✅ Environment check passed

REM Install frontend dependencies
echo 📦 Installing frontend dependencies...
call npm install

REM Install backend dependencies
echo 🐍 Installing backend dependencies...
cd backend
call pip install -r requirements.txt
cd ..

REM Create environment variable file
if not exist .env (
    echo 📝 Creating environment variable file...
    copy env.example .env
    echo ⚠️  Please edit the .env file to set your backend API address.
)

echo.
echo 🎉 Installation complete!
echo.
echo 📋 Next steps:
echo 1. Edit the backend/personal_data.json file with your personal information.
echo 2. Edit the .env file to set the backend API address.
echo 3. Run 'npm run dev' to start the frontend development server.
echo 4. In the backend directory, run 'python app.py' to start the backend server.
echo.
echo 📚 For more information, see README.md and DEPLOYMENT.md
pause 