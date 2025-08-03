#!/usr/bin/env python3
"""
Main application for Gambia Crop Prediction Model
Runs predictions for current and future years
"""

from datetime import datetime
from model import SeedModel


def get_current_year():
    """Get current year"""
    return datetime.now().year


def run_predictions_for_year(model, year, scenarios=None):
    """
    Run predictions for a specific year with different scenarios
    """
    print(f"\n{'=' * 60}")
    print(f"PREDICTIONS FOR YEAR {year}")
    print(f"{'=' * 60}")

    if scenarios is None:
        # Default scenarios for the year
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

    crops = [
        "Rice",
        "Millet",
        "Sorghum",
        "Maize",
        "Groundnuts",
        "Cotton",
        "Vegetables",
        "Fruits",
    ]

    # Adjust environmental factors based on year (future trends)
    year_factor = 1 + (year - get_current_year()) * 0.02  # 2% annual change

    for scenario_name, base_conditions in scenarios.items():
        print(f"\n📊 {scenario_name.upper()}")
        print("-" * 40)

        # Adjust conditions for future years
        adjusted_conditions = {}
        for key, value in base_conditions.items():
            if key in ["rainfall_mm", "temperature_c", "humidity_percent"]:
                # Climate factors
                if key == "temperature_c":
                    adjusted_conditions[key] = value * (
                        1 + (year - get_current_year()) * 0.01
                    )  # Warming
                elif key == "rainfall_mm":
                    adjusted_conditions[key] = value * (
                        1 + (year - get_current_year()) * 0.005
                    )  # Slight increase
                else:
                    adjusted_conditions[key] = value
            elif key in ["fertilizer_use_kg_ha", "irrigation_area_percent"]:
                # Technology adoption
                adjusted_conditions[key] = value * (
                    1 + (year - get_current_year()) * 0.03
                )
            elif key in ["fuel_price_usd_liter", "labor_cost_usd_day"]:
                # Economic factors
                adjusted_conditions[key] = value * (
                    1 + (year - get_current_year()) * 0.05
                )
            elif key == "market_demand_index":
                # Market demand
                adjusted_conditions[key] = value * (
                    1 + (year - get_current_year()) * 0.02
                )
            else:
                adjusted_conditions[key] = value

        print(f"Year {year} Conditions:")
        for key, value in adjusted_conditions.items():
            print(f"  {key}: {value:.2f}")

        print(
            f"\n{'Crop':<12} {'Yield (t/ha)':<15} {'Price ($/t)':<15} {'Production (t)':<15}"
        )
        print("-" * 60)

        for crop in crops:
            input_data = {"crop": crop, **adjusted_conditions}

            try:
                predictions = model.predict(input_data)
                yield_val = predictions["yield"][0]
                price_val = predictions["price"][0]
                production_val = predictions["production"][0]

                print(
                    f"{crop:<12} {yield_val:<15.2f} {price_val:<15.2f} {production_val:<15.0f}"
                )
            except Exception as e:
                print(f"{crop:<12} {'ERROR':<15} {'ERROR':<15} {'ERROR':<15}")


def run_rainfall_analysis(model, year):
    """
    Run detailed rainfall impact analysis for a specific year
    """
    print(f"\n{'=' * 60}")
    print(f"RAINFALL IMPACT ANALYSIS FOR YEAR {year}")
    print(f"{'=' * 60}")

    rainfall_levels = [400, 600, 800, 1000, 1200, 1400]
    crops = ["Rice", "Millet", "Groundnuts"]

    print(
        f"\n{'Rainfall (mm)':<15} {'Crop':<12} {'Yield (t/ha)':<15} {'Price ($/t)':<15} {'Production (t)':<15}"
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

            try:
                predictions = model.predict(input_data)
                yield_val = predictions["yield"][0]
                price_val = predictions["price"][0]
                production_val = predictions["production"][0]

                print(
                    f"{rainfall:<15} {crop:<12} {yield_val:<15.2f} {price_val:<15.2f} {production_val:<15.0f}"
                )
            except Exception as e:
                print(
                    f"{rainfall:<15} {crop:<12} {'ERROR':<15} {'ERROR':<15} {'ERROR':<15}"
                )


def run_future_trends_analysis(model, start_year, end_year):
    """
    Run analysis of trends over multiple future years
    """
    print(f"\n{'=' * 60}")
    print(f"FUTURE TRENDS ANALYSIS ({start_year} - {end_year})")
    print(f"{'=' * 60}")

    crops = ["Rice", "Groundnuts", "Vegetables"]
    years = range(start_year, end_year + 1)

    for crop in crops:
        print(f"\n📈 {crop.upper()} - Future Trends")
        print("-" * 40)
        print(
            f"{'Year':<8} {'Yield (t/ha)':<15} {'Price ($/t)':<15} {'Production (t)':<15}"
        )
        print("-" * 55)

        for year in years:
            # Adjust conditions for future
            year_factor = 1 + (year - get_current_year()) * 0.02

            input_data = {
                "crop": crop,
                "rainfall_mm": 800 * (1 + (year - get_current_year()) * 0.005),
                "temperature_c": 27 * (1 + (year - get_current_year()) * 0.01),
                "humidity_percent": 70,
                "soil_ph": 6.5,
                "fertilizer_use_kg_ha": 60 * (1 + (year - get_current_year()) * 0.03),
                "irrigation_area_percent": 20
                * (1 + (year - get_current_year()) * 0.03),
                "fuel_price_usd_liter": 1.3 * (1 + (year - get_current_year()) * 0.05),
                "labor_cost_usd_day": 16 * (1 + (year - get_current_year()) * 0.05),
                "market_demand_index": 100 * (1 + (year - get_current_year()) * 0.02),
            }

            try:
                predictions = model.predict(input_data)
                yield_val = predictions["yield"][0]
                price_val = predictions["price"][0]
                production_val = predictions["production"][0]

                print(
                    f"{year:<8} {yield_val:<15.2f} {price_val:<15.2f} {production_val:<15.0f}"
                )
            except Exception as e:
                print(f"{year:<8} {'ERROR':<15} {'ERROR':<15} {'ERROR':<15}")


def main():
    """
    Main function to run crop predictions
    """
    print("🌾 Gambia Crop Prediction Model")
    print("=" * 50)

    # Initialize model
    print("Loading and training model...")
    model = SeedModel()

    # Load real data and train
    real_data = model.load_real_data()
    model.train_models(real_data)
    print("✅ Model trained successfully!")

    current_year = get_current_year()
    print(f"Current year: {current_year}")

    # Run predictions for different years
    years_to_predict = [
        current_year,
        current_year + 1,
        current_year + 5,
        current_year + 10,
    ]

    for year in years_to_predict:
        if year == current_year:
            print(f"\n🎯 PREDICTIONS FOR CURRENT YEAR ({year})")
        elif year == current_year + 1:
            print(f"\n🔮 PREDICTIONS FOR NEXT YEAR ({year})")
        else:
            print(f"\n🚀 PREDICTIONS FOR FUTURE YEAR ({year})")

        run_predictions_for_year(model, year)

    # Run rainfall analysis for current year
    run_rainfall_analysis(model, current_year)

    # Run future trends analysis
    run_future_trends_analysis(model, current_year, current_year + 10)

    # Show feature importance
    print(f"\n{'=' * 60}")
    print("FEATURE IMPORTANCE ANALYSIS")
    print(f"{'=' * 60}")

    for target in ["yield", "price", "production"]:
        print(f"\n📊 Top 5 features for {target} prediction:")
        importance_df = model.get_feature_importance(target)
        print(importance_df.head().to_string(index=False))

    # Save model
    model.save_model("seed_model.pkl")
    print("\n✅ Model saved for future use!")

    print(f"\n{'=' * 60}")
    print("PREDICTION COMPLETE!")
    print(f"{'=' * 60}")
    print("📊 Predictions generated for multiple years")
    print("🌧️  Rainfall impact analysis completed")
    print("📈 Future trends analysis completed")
    print("🎯 Model ready for future predictions")


if __name__ == "__main__":
    main()
