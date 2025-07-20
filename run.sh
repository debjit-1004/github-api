#!/bin/bash

# GitHub API Scraper Deployment Script
echo "🚀 GitHub API Scraper Deployment"
echo "================================="

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment with uv..."
    uv venv .venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
uv pip install -r requirements.txt

# Run the application
echo "🎉 Starting GitHub API Scraper..."
echo "📍 API will be available at: http://localhost:8000"
echo "📖 Documentation: http://localhost:8000/docs"
echo "🔍 Interactive docs: http://localhost:8000/redoc"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================="

python main.py
