#!/usr/bin/env python3
"""
Test script for the Gambia Crop Prediction Model
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from seed.model import GambiaCropPredictor
import pandas as pd
import numpy as np


def test_model():
    """
    Test the crop prediction model
    """
    print("Testing Gambia Crop Prediction Model")
    print("=" * 50)

    # Initialize model
    model = GambiaCropPredictor()

    # Generate training data
    print("1. Generating training data...")
    training_data = model.generate_synthetic_data()
    print(f"   Generated {len(training_data)} training samples")
    print(f"   Data shape: {training_data.shape}")
    print(f"   Features: {list(training_data.columns)}")

    # Train models
    print("\n2. Training models...")
    model.train_models(training_data)

    # Test predictions with different scenarios
    print("\n3. Testing predictions...")

    # Scenario 1: Good conditions for Rice
    good_conditions = {
        "crop": "Rice",
        "rainfall_mm": 900,
        "temperature_c": 28,
        "humidity_percent": 80,
        "soil_ph": 6.8,
        "fertilizer_use_kg_ha": 80,
        "irrigation_area_percent": 30,
        "fuel_price_usd_liter": 1.2,
        "labor_cost_usd_day": 15,
        "market_demand_index": 120,
    }

    predictions_good = model.predict(good_conditions)
    print(f"\nGood conditions for Rice:")
    print(f"  Yield: {predictions_good['yield'][0]:.2f} tons/hectare")
    print(f"  Price: ${predictions_good['price'][0]:.2f}/ton")
    print(f"  Production: {predictions_good['production'][0]:.0f} tons")

    # Scenario 2: Poor conditions for Groundnuts
    poor_conditions = {
        "crop": "Groundnuts",
        "rainfall_mm": 600,
        "temperature_c": 32,
        "humidity_percent": 60,
        "soil_ph": 5.5,
        "fertilizer_use_kg_ha": 40,
        "irrigation_area_percent": 10,
        "fuel_price_usd_liter": 1.5,
        "labor_cost_usd_day": 18,
        "market_demand_index": 80,
    }

    predictions_poor = model.predict(poor_conditions)
    print(f"\nPoor conditions for Groundnuts:")
    print(f"  Yield: {predictions_poor['yield'][0]:.2f} tons/hectare")
    print(f"  Price: ${predictions_poor['price'][0]:.2f}/ton")
    print(f"  Production: {predictions_poor['production'][0]:.0f} tons")

    # Scenario 3: Average conditions for Millet
    average_conditions = {
        "crop": "Millet",
        "rainfall_mm": 800,
        "temperature_c": 27,
        "humidity_percent": 70,
        "soil_ph": 6.5,
        "fertilizer_use_kg_ha": 60,
        "irrigation_area_percent": 20,
        "fuel_price_usd_liter": 1.3,
        "labor_cost_usd_day": 16,
        "market_demand_index": 100,
    }

    predictions_average = model.predict(average_conditions)
    print(f"\nAverage conditions for Millet:")
    print(f"  Yield: {predictions_average['yield'][0]:.2f} tons/hectare")
    print(f"  Price: ${predictions_average['price'][0]:.2f}/ton")
    print(f"  Production: {predictions_average['production'][0]:.0f} tons")

    # Show feature importance
    print("\n4. Feature Importance Analysis:")
    for target in ["yield", "price", "production"]:
        importance_df = model.get_feature_importance(target)
        print(f"\nTop 5 features for {target} prediction:")
        print(importance_df.head().to_string(index=False))

    # Test multiple predictions at once
    print("\n5. Batch Predictions:")
    batch_inputs = [
        {
            "crop": "Rice",
            "rainfall_mm": 850,
            "temperature_c": 28,
            "humidity_percent": 75,
            "soil_ph": 6.8,
            "fertilizer_use_kg_ha": 70,
            "irrigation_area_percent": 25,
            "fuel_price_usd_liter": 1.3,
            "labor_cost_usd_day": 16,
            "market_demand_index": 110,
        },
        {
            "crop": "Maize",
            "rainfall_mm": 750,
            "temperature_c": 29,
            "humidity_percent": 65,
            "soil_ph": 6.2,
            "fertilizer_use_kg_ha": 55,
            "irrigation_area_percent": 15,
            "fuel_price_usd_liter": 1.4,
            "labor_cost_usd_day": 17,
            "market_demand_index": 95,
        },
        {
            "crop": "Vegetables",
            "rainfall_mm": 900,
            "temperature_c": 26,
            "humidity_percent": 85,
            "soil_ph": 7.0,
            "fertilizer_use_kg_ha": 90,
            "irrigation_area_percent": 40,
            "fuel_price_usd_liter": 1.1,
            "labor_cost_usd_day": 14,
            "market_demand_index": 130,
        },
    ]

    batch_df = pd.DataFrame(batch_inputs)
    batch_predictions = model.predict(batch_df)

    print(f"\nBatch predictions for {len(batch_inputs)} scenarios:")
    for i, (_, row) in enumerate(batch_df.iterrows()):
        print(f"\nScenario {i + 1} ({row['crop']}):")
        print(f"  Yield: {batch_predictions['yield'][i]:.2f} tons/hectare")
        print(f"  Price: ${batch_predictions['price'][i]:.2f}/ton")
        print(f"  Production: {batch_predictions['production'][i]:.0f} tons")

    # Save model
    print("\n6. Saving model...")
    model.save_model("seed_model.pkl")

    print("\nModel testing completed successfully!")


def analyze_rainfall_impact():
    """
    Analyze the impact of rainfall on crop yields
    """
    print("\n" + "=" * 50)
    print("Rainfall Impact Analysis")
    print("=" * 50)

    # Load or create model
    model = GambiaCropPredictor()
    training_data = model.generate_synthetic_data()
    model.train_models(training_data)

    # Test different rainfall levels
    rainfall_levels = [400, 600, 800, 1000, 1200, 1400]
    crops = ["Rice", "Millet", "Groundnuts"]

    print(f"\nAnalyzing rainfall impact on crop yields:")
    print(
        f"{'Rainfall (mm)':<15} {'Crop':<12} {'Yield (t/ha)':<15} {'Price ($/t)':<15} {'Production (t)':<15}"
    )
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

            predictions = model.predict(input_data)
            yield_val = predictions["yield"][0]
            price_val = predictions["price"][0]
            production_val = predictions["production"][0]

            print(
                f"{rainfall:<15} {crop:<12} {yield_val:<15.2f} {price_val:<15.2f} {production_val:<15.0f}"
            )


if __name__ == "__main__":
    test_model()
    analyze_rainfall_impact()
