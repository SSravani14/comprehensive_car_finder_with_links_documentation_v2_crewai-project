# Comprehensive Car Finder with Links Documentation

A sophisticated AI-powered car search application that uses CrewAI agents to find vehicles with real-time data and direct links to listings.

## 🚀 Quick Start

### Option 1: Real-Time Search (Recommended)
**Uses your actual API keys for real car listings with direct links**

```bash
./run_real_app.sh
```

This will:
- ✅ Use your real API keys (OpenAI, Brave, Serper, Browserbase)
- ✅ Search actual automotive platforms (AutoTrader, Cars.com, CarMax, etc.)
- ✅ Provide real-time vehicle listings with direct links
- ✅ Give you actual pricing and availability data

### Option 2: Demo Mode
**Shows UI functionality with simulated results**

```bash
python3.10 app_demo.py
```

This will:
- ✅ Show how the interface works
- ✅ Display simulated car listings
- ✅ No API keys required
- ❌ Uses example/predefined data

## 🔑 API Keys Required for Real-Time Search

The real-time search requires these API keys:

- **OpenAI API Key**: For AI agents (GPT-4)
- **Brave API Key**: For web search capabilities
- **Serper API Key**: For search functionality
- **Browserbase API Key**: For web browsing tools

## 🌐 Access the Application

Once running, access the web interface at:
- **Real-time mode**: http://localhost:5001
- **Demo mode**: http://localhost:5001

## 📋 What You'll Get with Real-Time Search

### Real Data Sources
- **AutoTrader**: Direct links to vehicle listings
- **Cars.com**: Real-time pricing and availability
- **CarMax**: Certified pre-owned vehicles
- **Carvana**: Online car buying platform
- **Facebook Marketplace**: Private seller listings
- **Local dealerships**: Actual inventory

### Comprehensive Analysis
- **KBB/Edmunds valuations**: Real market pricing
- **Vehicle history reports**: Actual VIN lookups
- **Seller verification**: Real contact information
- **Local market analysis**: Current pricing trends
- **Inspection recommendations**: Based on actual vehicle data

### Direct Links Provided
- ✅ **Listing URLs**: Direct links to car listings
- ✅ **VIN Lookup**: Links to vehicle history reports
- ✅ **Seller Contact**: Real phone numbers and emails
- ✅ **Dealership Info**: Actual business information

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SSravani14/comprehensive_car_finder_with_links_documentation_v2_crewai-project.git
   cd comprehensive_car_finder_with_links_documentation_v2_crewai-project
   ```

2. **Install Python 3.10+** (if not already installed):
   ```bash
   brew install python@3.10
   ```

3. **Install dependencies**:
   ```bash
   python3.10 -m pip install -r requirements.txt
   ```

## 🎯 How to Use

1. **Start the application**:
   ```bash
   ./run_real_app.sh  # For real-time search
   # OR
   python3.10 app_demo.py  # For demo mode
   ```

2. **Open your browser** and go to http://localhost:5001

3. **Fill in your search criteria**:
   - Car type (sedan, SUV, truck, etc.)
   - Color preference
   - Brand preferences
   - Mileage range
   - Price range
   - Location

4. **Click "Search Cars"** and wait for the AI agents to:
   - Search real automotive platforms
   - Analyze market pricing
   - Provide direct links to listings
   - Generate comprehensive reports

## 🔍 Real-Time vs Demo Mode

| Feature | Real-Time Mode | Demo Mode |
|---------|----------------|-----------|
| **Data Source** | Actual car listings | Simulated data |
| **Links** | Real URLs to listings | Example links |
| **Pricing** | Current market prices | Sample prices |
| **Availability** | Real inventory | Mock availability |
| **API Keys** | Required | Not needed |
| **Processing Time** | 2-5 minutes | 2-3 seconds |

## 📊 Sample Real-Time Output

When you use real-time mode, you'll get:

```
🚗 COMPREHENSIVE CAR FINDER RESULTS
=====================================

📋 SEARCH CRITERIA:
- Car Type: sedan
- Color: any
- Brands: Toyota, Honda
- Mileage: under 50,000
- Price Range: $20,000 - $35,000
- Location: Los Angeles, CA

💰 TOP 10 VEHICLE RECOMMENDATIONS:

1. 2020 Toyota Camry SE
   - Price: $28,500
   - Mileage: 45,000
   - Location: Los Angeles, CA
   - Direct Link: https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=123456789
   - VIN: 4T1B11HK5KU123456
   - Seller: Toyota of Downtown LA
   - Contact: (555) 123-4567

2. 2019 Honda Accord Sport
   - Price: $26,900
   - Mileage: 52,000
   - Location: Los Angeles, CA
   - Direct Link: https://www.cars.com/vehicledetail/987654321/
   - VIN: 1HGCV1F3XKA987654
   - Seller: Honda World
   - Contact: (555) 987-6543
```

## 🛡️ Security

- API keys are handled securely through environment variables
- No sensitive information is stored in the code
- All API calls are made securely through official SDKs

## 🐛 Troubleshooting

### Port Already in Use
```bash
lsof -ti:5001 | xargs kill -9
```

### Module Not Found Error
```bash
export PYTHONPATH="/path/to/project/src:$PYTHONPATH"
```

### API Key Issues
Make sure your API keys are valid and have sufficient credits.

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
