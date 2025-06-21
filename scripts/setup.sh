#!/bin/bash

echo "🚀 Quick Start Script for AI Profile Assistant Project"
echo "=================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

echo "✅ Environment check passed"

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
npm install

# Install backend dependencies
echo "🐍 Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

# Create environment variable file
if [ ! -f .env ]; then
    echo "📝 Creating environment variable file..."
    cp env.example .env
    echo "⚠️  Please edit the .env file to set your backend API address."
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit the backend/personal_data.json file with your personal information."
echo "2. Edit the .env file to set the backend API address."
echo "3. Run 'npm run dev' to start the frontend development server."
echo "4. In the backend directory, run 'python app.py' to start the backend server."
echo ""
echo "📚 For more information, see README.md and DEPLOYMENT.md" 