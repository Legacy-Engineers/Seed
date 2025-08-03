#!/usr/bin/env python3
"""
Simple test script to verify the model works
"""

from seed.model import SeedModel


def test_model():
    print("Testing Gambia Crop Prediction Model...")

    # Initialize model
    model = SeedModel()

    # Load real data
    print("Loading real data...")
    real_data = model.load_real_data()
    print(f"Loaded {len(real_data)} data points")

    # Train model
    print("Training model...")
    model.train_models(real_data)
    print("Model trained successfully!")

    # Test prediction
    print("Testing prediction...")
    test_input = {
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
    }

    predictions = model.predict(test_input)
    print("Predictions:")
    for target, value in predictions.items():
        print(f"  {target}: {value[0]:.2f}")

    print("Test completed successfully!")


if __name__ == "__main__":
    test_model()
