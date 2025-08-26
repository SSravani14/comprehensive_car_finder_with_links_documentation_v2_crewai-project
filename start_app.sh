#!/bin/bash

# Comprehensive Car Finder - Startup Script
echo "🚗 Starting Comprehensive Car Finder with Real AI Agents..."

# Set up Python 3.10 path
export PATH="/opt/homebrew/bin:$PATH"

# Check if Python 3.10 is available
if ! command -v python3.10 &> /dev/null; then
    echo "❌ Python 3.10 not found. Please install it first:"
    echo "   brew install python@3.10"
    exit 1
fi

# Check if CrewAI is installed
if ! python3.10 -c "import crewai" &> /dev/null; then
    echo "❌ CrewAI not found. Installing..."
    python3.10 -m pip install "crewai[tools]>=0.150.0,<1.0.0"
fi

# Check if Flask is installed
if ! python3.10 -c "import flask" &> /dev/null; then
    echo "❌ Flask not found. Installing..."
    python3.10 -m pip install flask
fi

# Kill any existing process on port 5000
if lsof -ti:5000 > /dev/null 2>&1; then
    echo "🔄 Stopping existing process on port 5000..."
    kill -9 $(lsof -ti:5000)
fi

echo "✅ Starting the application..."
echo "🌐 Access the UI at: http://localhost:5000"
echo "📱 The application will use your real API keys for:"
echo "   - OpenAI GPT-4 (for AI agents)"
echo "   - Brave Search (for web search)"
echo "   - Serper (for search functionality)"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Set up Python path for the CrewAI module
export PYTHONPATH="/Users/sravanisiddanthapu/Downloads/comprehensive_car_finder_with_links_documentation_v2_crewai-project/src:$PYTHONPATH"

# Start the application
python3.10 app.py
