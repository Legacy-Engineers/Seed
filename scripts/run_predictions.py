#!/usr/bin/env python3
"""
Script to run crop predictions for specific years
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from seed.model import GambiaCropPredictor
import argparse
from datetime import datetime


def run_single_year_prediction(year, crop=None):
    """
    Run predictions for a single year
    """
    print(f"🌾 Running predictions for year {year}")
    print("=" * 50)
    
    # Initialize and train model
    model = GambiaCropPredictor()
    real_data = model.load_real_data()
    model.train_models(real_data)
    
    # Define crops to predict
    if crop:
        crops = [crop]
    else:
        crops = ["Rice", "Millet", "Sorghum", "Maize", "Groundnuts", "Cotton", "Vegetables", "Fruits"]
    
    # Define scenarios
    scenarios = {
        "Good Conditions": {
            "rainfall_mm": 900,
            "temperature_c": 28,
            "humidity_percent": 80,
            "soil_ph": 6.8,
            "fertilizer_use_kg_ha": 80,
            "irrigation_area_percent": 30,
            "fuel_price_usd_liter": 1.2,
            "labor_cost_usd_day": 15,
            "market_demand_index": 120,
        },
        "Average Conditions": {
            "rainfall_mm": 800,
            "temperature_c": 27,
            "humidity_percent": 70,
            "soil_ph": 6.5,
            "fertilizer_use_kg_ha": 60,
            "irrigation_area_percent": 20,
            "fuel_price_usd_liter": 1.3,
            "labor_cost_usd_day": 16,
            "market_demand_index": 100,
        },
        "Poor Conditions": {
            "rainfall_mm": 600,
            "temperature_c": 32,
            "humidity_percent": 60,
            "soil_ph": 5.5,
            "fertilizer_use_kg_ha": 40,
            "irrigation_area_percent": 10,
            "fuel_price_usd_liter": 1.5,
            "labor_cost_usd_day": 18,
            "market_demand_index": 80,
        },
    }
    
    current_year = datetime.now().year
    
    for scenario_name, conditions in scenarios.items():
        print(f"\n📊 {scenario_name.upper()}")
        print("-" * 40)
        
        # Adjust conditions for future years
        adjusted_conditions = {}
        for key, value in conditions.items():
            if key in ["rainfall_mm", "temperature_c", "humidity_percent"]:
                if key == "temperature_c":
                    adjusted_conditions[key] = value * (1 + (year - current_year) * 0.01)
                elif key == "rainfall_mm":
                    adjusted_conditions[key] = value * (1 + (year - current_year) * 0.005)
                else:
                    adjusted_conditions[key] = value
            elif key in ["fertilizer_use_kg_ha", "irrigation_area_percent"]:
                adjusted_conditions[key] = value * (1 + (year - current_year) * 0.03)
            elif key in ["fuel_price_usd_liter", "labor_cost_usd_day"]:
                adjusted_conditions[key] = value * (1 + (year - current_year) * 0.05)
            elif key == "market_demand_index":
                adjusted_conditions[key] = value * (1 + (year - current_year) * 0.02)
            else:
                adjusted_conditions[key] = value
        
        print(f"Year {year} Conditions:")
        for key, value in adjusted_conditions.items():
            print(f"  {key}: {value:.2f}")
        
        print(f"\n{'Crop':<12} {'Yield (t/ha)':<15} {'Price ($/t)':<15} {'Production (t)':<15}")
        print("-" * 60)
        
        for crop_name in crops:
            input_data = {
                "crop": crop_name,
                **adjusted_conditions
            }
            
            try:
                predictions = model.predict(input_data)
                yield_val = predictions["yield"][0]
                price_val = predictions["price"][0]
                production_val = predictions["production"][0]
                
                print(f"{crop_name:<12} {yield_val:<15.2f} {price_val:<15.2f} {production_val:<15.0f}")
            except Exception as e:
                print(f"{crop_name:<12} {'ERROR':<15} {'ERROR':<15} {'ERROR':<15}")


def run_rainfall_analysis(year):
    """
    Run rainfall impact analysis for a specific year
    """
    print(f"🌧️  Rainfall impact analysis for year {year}")
    print("=" * 50)
    
    model = GambiaCropPredictor()
    real_data = model.load_real_data()
    model.train_models(real_data)
    
    rainfall_levels = [400, 600, 800, 1000, 1200, 1400]
    crops = ["Rice", "Millet", "Groundnuts"]
    
    print(f"\n{'Rainfall (mm)':<15} {'Crop':<12} {'Yield (t/ha)':<15} {'Price ($/t)':<15} {'Production (t)':<15}")
    print("-" * 75)
    
    for rainfall in rainfall_levels:
        for crop in crops:
            input_data = {
                "crop": crop,
                "rainfall_mm": rainfall,
                "temperature_c": 27,
                "humidity_percent": 70,
                "soil_ph": 6.5,
                "fertilizer_use_kg_ha": 60,
                "irrigation_area_percent": 20,
                "fuel_price_usd_liter": 1.3,
                "labor_cost_usd_day": 16,
                "market_demand_index": 100,
            }
            
            try:
                predictions = model.predict(input_data)
                yield_val = predictions["yield"][0]
                price_val = predictions["price"][0]
                production_val = predictions["production"][0]
                
                print(f"{rainfall:<15} {crop:<12} {yield_val:<15.2f} {price_val:<15.2f} {production_val:<15.0f}")
            except Exception as e:
                print(f"{rainfall:<15} {crop:<12} {'ERROR':<15} {'ERROR':<15} {'ERROR':<15}")


def main():
    """
    Main function with command line arguments
    """
    parser = argparse.ArgumentParser(description="Run crop predictions for specific years")
    parser.add_argument("year", type=int, help="Year to predict for")
    parser.add_argument("--crop", type=str, help="Specific crop to predict (optional)")
    parser.add_argument("--rainfall", action="store_true", help="Run rainfall impact analysis")
    
    args = parser.parse_args()
    
    if args.rainfall:
        run_rainfall_analysis(args.year)
    else:
        run_single_year_prediction(args.year, args.crop)


if __name__ == "__main__":
    main() 