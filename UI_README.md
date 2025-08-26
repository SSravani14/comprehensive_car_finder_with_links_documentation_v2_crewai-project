# Comprehensive Car Finder - Web UI

A modern web interface for the CrewAI-powered car finder application.

## Features

- 🎨 Modern, responsive design
- 🔍 Real-time search with AI agents
- 📱 Mobile-friendly interface
- ⚡ Real-time status updates
- 🎯 Comprehensive car search criteria

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the UI**
   Open your browser and go to: `http://localhost:5000`

## Usage

1. **Fill out the search form** with your car preferences:
   - Car type (sedan, SUV, truck, etc.)
   - Color preference
   - Preferred brands
   - Mileage range
   - Price range
   - Location and state

2. **Click "Search for Cars"** to start the AI-powered search

3. **Wait for results** - The AI agents will:
   - Analyze your requirements
   - Search automotive marketplaces
   - Evaluate vehicle values
   - Create inspection plans
   - Provide legal compliance information
   - Generate top 10 recommendations

## API Endpoints

- `GET /` - Main UI page
- `POST /api/search` - Start a car search
- `GET /api/status` - Check search status

## Environment Variables

The application automatically sets the following API keys:
- `OPENAI_API_KEY` - For AI model access
- `BRAVE_API_KEY` - For web search capabilities
- `SERPER_API_KEY` - For search functionality

## File Structure

```
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Main UI template
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── script.js     # Frontend logic
└── requirements.txt      # Python dependencies
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **AI**: CrewAI with OpenAI GPT-4
- **Styling**: Custom CSS with modern design principles
- **Icons**: Emoji and Unicode symbols

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Troubleshooting

1. **Port already in use**: Change the port in `app.py` line 67
2. **API key errors**: Verify your API keys are valid
3. **Search not starting**: Check browser console for JavaScript errors
4. **Results not showing**: Ensure the CrewAI agents are working properly
