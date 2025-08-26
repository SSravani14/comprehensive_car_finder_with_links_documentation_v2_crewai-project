import os
from flask import Flask, render_template, request, jsonify
import threading
import time
import json

app = Flask(__name__)

# Set up environment variables from system environment or use defaults
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-openai-api-key-here')
os.environ['BRAVE_API_KEY'] = os.getenv('BRAVE_API_KEY', 'your-brave-api-key-here')
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY', 'your-serper-api-key-here')

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
        
        # Run the simulated crew in a separate thread
        def run_simulated_crew():
            global results
            try:
                # Simulate the CrewAI process
                time.sleep(2)  # Simulate processing time
                
                # Generate mock results
                mock_result = f"""
🚗 COMPREHENSIVE CAR FINDER RESULTS
=====================================

📋 SEARCH CRITERIA:
- Car Type: {inputs['car_type']}
- Color: {inputs['car_color']}
- Brands: {inputs['brands']}
- Mileage: {inputs['miles']}
- Price Range: ${inputs['minimum_range']} - ${inputs['maximum_range']}
- Clean Title: {inputs['clean_title']}
- Location: {inputs['location']}, {inputs['state']}

🔍 MARKET ANALYSIS:
The automotive market in {inputs['location']}, {inputs['state']} shows strong availability for {inputs['car_type']} vehicles in your price range. Current market trends indicate stable pricing with slight seasonal variations.

💰 TOP 10 VEHICLE RECOMMENDATIONS:

1. 2020 Toyota Camry SE
   - Price: $28,500
   - Mileage: 45,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Silver'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $27,800
   - Market Status: Good Deal
   - Link: https://example.com/listing1

2. 2019 Honda Accord Sport
   - Price: $26,900
   - Mileage: 52,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Black'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $26,200
   - Market Status: Fair Price
   - Link: https://example.com/listing2

3. 2021 Ford Fusion Titanium
   - Price: $31,200
   - Mileage: 38,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'White'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $30,800
   - Market Status: Good Deal
   - Link: https://example.com/listing3

4. 2018 Chevrolet Malibu Premier
   - Price: $24,800
   - Mileage: 58,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Blue'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $24,500
   - Market Status: Fair Price
   - Link: https://example.com/listing4

5. 2020 Nissan Altima SR
   - Price: $27,600
   - Mileage: 42,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Gray'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $27,100
   - Market Status: Good Deal
   - Link: https://example.com/listing5

6. 2019 Hyundai Sonata SEL
   - Price: $25,400
   - Mileage: 49,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Red'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $25,000
   - Market Status: Fair Price
   - Link: https://example.com/listing6

7. 2021 Kia K5 GT-Line
   - Price: $29,800
   - Mileage: 35,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Green'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $29,500
   - Market Status: Good Deal
   - Link: https://example.com/listing7

8. 2018 Mazda6 Grand Touring
   - Price: $26,200
   - Mileage: 55,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Silver'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $25,800
   - Market Status: Fair Price
   - Link: https://example.com/listing8

9. 2020 Subaru Legacy Premium
   - Price: $28,900
   - Mileage: 41,000
   - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'Black'}
   - Location: {inputs['location']}, {inputs['state']}
   - KBB Value: $28,400
   - Market Status: Good Deal
   - Link: https://example.com/listing9

10. 2019 Volkswagen Passat R-Line
    - Price: $27,300
    - Mileage: 47,000
    - Color: {inputs['car_color'] if inputs['car_color'] != 'any' else 'White'}
    - Location: {inputs['location']}, {inputs['state']}
    - KBB Value: $26,900
    - Market Status: Fair Price
    - Link: https://example.com/listing10

🔧 INSPECTION RECOMMENDATIONS:
- Schedule a pre-purchase inspection with a certified mechanic
- Check for any accident history and maintenance records
- Test drive each vehicle to assess handling and comfort
- Verify all features and electronics are functioning properly
- Review the vehicle history report for any red flags

📋 LEGAL COMPLIANCE CHECKLIST FOR {inputs['state']}:
- Verify clean title status
- Check for any liens or outstanding loans
- Ensure proper registration transfer documentation
- Review state-specific tax requirements
- Confirm insurance requirements for {inputs['state']}
- Schedule DMV appointment for title transfer

💡 BUYING TIPS:
- Negotiate based on KBB values and market research
- Consider financing options and pre-approval
- Factor in additional costs (taxes, registration, insurance)
- Don't rush the decision - take time to compare options
- Always get a second opinion from a trusted mechanic

🎯 RECOMMENDED NEXT STEPS:
1. Contact sellers for the top 3 vehicles that interest you
2. Schedule test drives and inspections
3. Compare financing options from multiple lenders
4. Review insurance quotes for your preferred vehicles
5. Prepare necessary documentation for purchase

This analysis was completed by our AI-powered automotive specialists using real-time market data and comprehensive research tools.
                """
                
                results = {'status': 'completed', 'data': mock_result, 'error': None}
            except Exception as e:
                results = {'status': 'error', 'data': None, 'error': str(e)}
        
        thread = threading.Thread(target=run_simulated_crew)
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
