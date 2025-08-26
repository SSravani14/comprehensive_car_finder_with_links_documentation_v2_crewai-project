#!/bin/bash

echo "🚗 Starting Comprehensive Car Finder with Real AI Agents..."
echo ""

# Set up Python 3.10 in PATH
export PATH="/opt/homebrew/bin:$PATH"

# Set up Python path for the CrewAI module
export PYTHONPATH="/Users/sravanisiddanthapu/Downloads/comprehensive_car_finder_with_links_documentation_v2_crewai-project/src:$PYTHONPATH"

# Set up environment variables with real API keys
# Replace these with your actual API keys
export OPENAI_API_KEY="your-openai-api-key-here"
export BRAVE_API_KEY="your-brave-api-key-here"
export SERPER_API_KEY="your-serper-api-key-here"
export BROWSERBASE_API_KEY="your-browserbase-api-key-here"

echo "✅ Environment variables set up"
echo "✅ Python 3.10 configured"
echo "✅ CrewAI module path configured"
echo ""

# Check if port 5001 is in use and kill any existing process
if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null ; then
    echo "🔄 Stopping existing process on port 5001..."
    lsof -ti:5001 | xargs kill -9
    sleep 2
fi

echo "✅ Starting the application..."
echo "🌐 Access the UI at: http://localhost:5001"
echo "📱 The application will use your real API keys for:"
echo "   - OpenAI GPT-4 (for AI agents)"
echo "   - Brave Search (for web search)"
echo "   - Serper (for search functionality)"
echo "   - Browserbase (for web browsing)"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the application
python3.10 app.py
