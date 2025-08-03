# Scripts Directory

This directory contains all Python scripts for data generation, processing, and machine learning models for The Gambia agricultural data.

## Scripts Overview

### Data Generation Scripts

1. **`create_datasets.py`**

   - Creates basic agricultural datasets for years 2001-2004
   - Based on FAO Agricultural Census Report 2001/2002 and GBOS data
   - Generates 6 categories: crops, fisheries, sales, livestock, practices, tenure

2. **`create_simple_datasets.py`**

   - Simplified version of dataset creation
   - Creates basic datasets with minimal complexity

3. **`create_2004_2021_data.py`**

   - Generates extended datasets from 2004 to 2021
   - Uses growth factors and realistic projections
   - Creates 108 files (6 categories × 18 years)

4. **`simple_data_generator.py`**

   - Advanced data generation with realistic growth patterns
   - Includes climate variability and technology improvements
   - Uses mathematical functions for realistic projections

5. **`generate_extended_datasets.py`**

   - Comprehensive dataset generation with multiple factors
   - Includes climate cycles, market fluctuations, and policy changes
   - Most sophisticated data generation script

6. **`extract_excel_data.py`**
   - Extracts data from GBoS-National-Accounts.xlsx
   - Analyzes Excel file structure and generates datasets
   - Includes Excel data analysis capabilities

### Verification and Testing Scripts

7. **`verify_datasets.py`**

   - Verifies that all datasets have been created correctly
   - Shows summary of created files and data structure
   - Validates data integrity

8. **`test_crop_model.py`**
   - Tests the machine learning crop prediction model
   - Demonstrates model capabilities with different scenarios
   - Includes rainfall impact analysis

## Machine Learning Model

The main machine learning model is located in `../seed/model.py` and includes:

- **GambiaCropPredictor**: Class for predicting crop yield, price, and production
- **Features**: Rainfall, temperature, humidity, soil pH, fertilizer use, irrigation, fuel price, labor cost, market demand
- **Models**: Random Forest, Gradient Boosting, Ridge Regression, Linear Regression
- **Targets**: Yield (tons/hectare), Price (USD/ton), Production (tons)

## Usage Examples

### Generate Basic Datasets

```bash
cd scripts
python create_datasets.py
```

### Generate Extended Datasets (2004-2021)

```bash
cd scripts
python create_2004_2021_data.py
```

### Test Machine Learning Model

```bash
cd scripts
python test_crop_model.py
```

### Verify Datasets

```bash
cd scripts
python verify_datasets.py
```

## Data Categories

1. **Crops**: Rice, Millet, Sorghum, Maize, Groundnuts, Cotton, Vegetables, Fruits
2. **Fisheries**: Fresh Fish, Dried Fish, Smoked Fish, Crustaceans, Molluscs
3. **Sales**: Cereals, Groundnuts, Vegetables, Fish, Livestock, Fruits
4. **Livestock**: Cattle, Sheep, Goats, Poultry, Pigs, Horses, Donkeys
5. **Farm Practices**: Irrigation, Fertilizer Use, Pesticide Use, Mechanization, Organic Farming
6. **Land Tenure**: Owned Land, Rented Land, Communal Land, Leased Land, Inherited Land

## File Structure

Each year directory contains 6 CSV files:

- `crops_YYYY.csv`
- `fisheries_YYYY.csv`
- `sales_YYYY.csv`
- `livestock_YYYY.csv`
- `practices_YYYY.csv`
- `tenure_YYYY.csv`

## Dependencies

- pandas
- numpy
- scikit-learn
- joblib
- pathlib
- csv
- os

## Notes

- All scripts are designed to work with The Gambia's agricultural context
- Data includes realistic growth projections and climate variability
- Machine learning model uses synthetic data with realistic relationships
- Scripts can be run independently or as part of a data pipeline
