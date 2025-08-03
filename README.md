# SEED

A comprehensive system for agricultural data generation and machine learning predictions for The Gambia.

## !NOTE

this is a learning project for [Dawda Borje Kujabi](https://github.com/Dawdaborje) to learn machine learning

## 🌾 Features

### Data Generation

- **Historical Data**: Agricultural datasets from 2001-2021
- **Real Data Integration**: Uses actual datasets from `data/` directory
- **Multiple Categories**: Crops, Fisheries, Sales, Livestock, Farm Practices, Land Tenure
- **Growth Projections**: Realistic growth patterns with climate variability

### Machine Learning Model

- **Multi-Target Prediction**: Yield, Price, and Production
- **Environmental Factors**: Rainfall, temperature, humidity, soil pH
- **Economic Factors**: Fuel prices, labor costs, market demand
- **Technology Factors**: Fertilizer use, irrigation, crop type
- **Future Predictions**: Support for current and future years (2024-2030+)

## 🚀 Quick Start

### Run Main Predictions

```bash
# Run comprehensive predictions for current and future years
python seed/main.py
```

### Run Specific Year Predictions

```bash
# Predict for current year
python scripts/run_predictions.py 2024

# Predict for future year
python scripts/run_predictions.py 2029

# Predict specific crop for 2025
python scripts/run_predictions.py 2025 --crop Rice

# Rainfall impact analysis for 2026
python scripts/run_predictions.py 2026 --rainfall
```

### Test Model

```bash
# Simple model test
python test_model.py
```

## 📊 Prediction Capabilities

### Current Year Predictions

- **2024**: Current year with real data
- **Good/Average/Poor Conditions**: Multiple scenarios
- **All Crops**: Rice, Millet, Sorghum, Maize, Groundnuts, Cotton, Vegetables, Fruits

### Future Year Predictions

- **2025-2030+**: Future predictions with trend adjustments
- **Climate Change**: Temperature and rainfall projections
- **Technology Adoption**: Increasing fertilizer and irrigation use
- **Economic Trends**: Rising fuel prices and labor costs
- **Market Evolution**: Growing demand for certain crops

### Rainfall Impact Analysis

- **Rainfall Levels**: 400-1400mm range
- **Crop Sensitivity**: Different crops respond differently to rainfall
- **Yield Impact**: Shows how rainfall affects crop yields
- **Price Effects**: Rainfall impact on crop prices

## 📁 Project Structure

```
seed/
├── data/                    # Agricultural datasets (2001-2021)
│   ├── 2001/              # Year-specific data
│   ├── 2002/
│   └── ...                # Up to 2021
├── scripts/                # Data generation scripts
│   ├── create_datasets.py
│   ├── run_predictions.py
│   └── README.md
├── seed/
│   ├── model.py           # ML model using real data
│   └── main.py            # Main prediction application
├── external_data/         # Excel data source
└── test_model.py          # Simple model test
```

## 🎯 Model Features

### Input Variables

- **Rainfall** (mm/year): Primary environmental factor
- **Temperature** (°C): Climate impact
- **Humidity** (%): Moisture conditions
- **Soil pH**: Soil quality indicator
- **Fertilizer Use** (kg/ha): Technology adoption
- **Irrigation Area** (%): Water management
- **Fuel Price** (USD/liter): Economic factor
- **Labor Cost** (USD/day): Economic factor
- **Market Demand** (index): Market conditions
- **Crop Type**: Categorical variable

### Output Predictions

- **Yield** (tons/hectare): Crop productivity
- **Price** (USD/ton): Market value
- **Production** (tons): Total output

### Machine Learning Models

- **Random Forest**: Best for complex relationships
- **Gradient Boosting**: Handles non-linear patterns
- **Ridge Regression**: Linear relationships
- **Linear Regression**: Baseline model

## 📈 Future Predictions

The system can predict for any future year with realistic adjustments:

### Climate Trends (2024-2030)

- **Temperature**: +1% annually (climate change)
- **Rainfall**: +0.5% annually (slight increase)
- **Humidity**: Stable with minor variations

### Technology Trends

- **Fertilizer Use**: +3% annually (increasing adoption)
- **Irrigation**: +3% annually (water management)
- **Crop Yields**: +2% annually (improved practices)

### Economic Trends

- **Fuel Prices**: +5% annually (inflation)
- **Labor Costs**: +5% annually (wage increases)
- **Market Demand**: +2% annually (population growth)

## 🌧️ Rainfall Impact Analysis

The model shows how different rainfall levels affect crop performance:

| Rainfall (mm) | Rice Yield | Millet Yield | Groundnuts Yield |
| ------------- | ---------- | ------------ | ---------------- |
| 400           | Low        | Medium       | Low              |
| 600           | Medium     | High         | Medium           |
| 800           | High       | High         | High             |
| 1000          | Very High  | High         | Very High        |
| 1200          | Very High  | Medium       | Very High        |
| 1400          | Very High  | Low          | Very High        |

## 🎯 Usage Examples

### Predict Rice Production for 2029

```python
from seed.model import GambiaCropPredictor

model = GambiaCropPredictor()
real_data = model.load_real_data()
model.train_models(real_data)

# Predict for 2029
input_data = {
    "crop": "Rice",
    "rainfall_mm": 850,
    "temperature_c": 28.5,  # Adjusted for 2029
    "humidity_percent": 75,
    "soil_ph": 6.8,
    "fertilizer_use_kg_ha": 85,  # Higher adoption
    "irrigation_area_percent": 35,  # More irrigation
    "fuel_price_usd_liter": 1.8,  # Higher fuel prices
    "labor_cost_usd_day": 22,  # Higher labor costs
    "market_demand_index": 120,  # Higher demand
}

predictions = model.predict(input_data)
print(f"Yield: {predictions['yield'][0]:.2f} tons/hectare")
print(f"Price: ${predictions['price'][0]:.2f}/ton")
print(f"Production: {predictions['production'][0]:.0f} tons")
```

## 📋 Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- joblib

## 🔧 Installation

```bash
# Install dependencies
pip install pandas numpy scikit-learn joblib

# Run predictions
python seed/main.py
```

## 📊 Data Sources

- **FAO Agricultural Census Report 2001/2002**
- **GBOS (Gambia Bureau of Statistics) Data**
- **Real datasets from data/ directory**
- **Environmental and economic projections**

The system is now ready for comprehensive agricultural predictions for The Gambia, with support for current and future years based on real data and realistic projections.
