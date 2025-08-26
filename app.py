import os
from flask import Flask, render_template, request, jsonify
from comprehensive_car_finder_with_links_documentation.crew import ComprehensiveCarFinderWithLinksDocumentationCrew
import threading
import time
import json

app = Flask(__name__)

# Set up environment variables from system environment or use defaults
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-openai-api-key-here')
os.environ['BRAVE_API_KEY'] = os.getenv('BRAVE_API_KEY', 'your-brave-api-key-here')
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY', 'your-serper-api-key-here')
os.environ['BROWSERBASE_API_KEY'] = os.getenv('BROWSERBASE_API_KEY', 'your-browserbase-api-key-here')

# Global variable to store results
results = {}
current_task = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_cars():
    global results, current_task
    
    try:
        data = request.json
        
        # Prepare inputs for the crew
        inputs = {
            'car_type': data.get('car_type', 'sedan'),
            'car_color': data.get('car_color', 'any'),
            'brands': data.get('brands', 'any'),
            'miles': data.get('miles', 'any'),
            'minimum_range': data.get('minimum_range', '10000'),
            'maximum_range': data.get('maximum_range', '50000'),
            'clean_title': data.get('clean_title', 'yes'),
            'state': data.get('state', 'CA'),
            'location': data.get('location', 'Los Angeles')
        }
        
        # Reset results
        results = {'status': 'running', 'data': None, 'error': None}
        current_task = 'search'
        
        # Run the crew in a separate thread
        def run_crew():
            global results
            try:
                crew = ComprehensiveCarFinderWithLinksDocumentationCrew()
                result = crew.crew().kickoff(inputs=inputs)
                # Convert CrewOutput to string to make it JSON serializable
                result_str = str(result) if result else "No results found"
                results = {'status': 'completed', 'data': result_str, 'error': None}
            except Exception as e:
                results = {'status': 'error', 'data': None, 'error': str(e)}
        
        thread = threading.Thread(target=run_crew)
        thread.start()
        
        return jsonify({'status': 'started', 'message': 'Search started successfully'})
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/status')
def get_status():
    global results
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
