"""
Machine Learning Model for Crop Prediction in The Gambia
Predicts crop growth, price, and yield based on environmental and economic factors
Uses real datasets from data/ directory
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib
import warnings
from pathlib import Path
import os

warnings.filterwarnings("ignore")


class SeedModel:
    """
    Machine Learning model for predicting crop performance in The Gambia
    Uses real datasets from data/ directory
    """

    def __init__(self):
        self.models = {"yield": None, "price": None, "production": None}
        self.scalers = {}
        self.label_encoders = {}
        self.feature_names = []
        self.is_trained = False
        self.data_dir = Path("data")

    def load_real_data(self, years=None):
        """
        Load real agricultural data from data/ directory
        """
        if years is None:
            years = range(2001, 2022)  # All available years

        all_data = []

        for year in years:
            year_dir = self.data_dir / str(year)
            if not year_dir.exists():
                continue

            # Load crops data
            crops_file = year_dir / f"crops_{year}.csv"
            if crops_file.exists():
                crops_df = pd.read_csv(crops_file)
                crops_df["year"] = year
                crops_df["data_type"] = "crops"

                # Add environmental features (synthetic but realistic)
                for idx, row in crops_df.iterrows():
                    # Generate realistic environmental data based on year and crop
                    rainfall = self._generate_rainfall(year, row["crop"])
                    temperature = self._generate_temperature(year, row["crop"])
                    humidity = self._generate_humidity(year, row["crop"])
                    soil_ph = self._generate_soil_ph(row["crop"])
                    fertilizer_use = self._generate_fertilizer_use(year, row["crop"])
                    irrigation_area = self._generate_irrigation_area(year, row["crop"])

                    # Economic factors
                    fuel_price = self._generate_fuel_price(year)
                    labor_cost = self._generate_labor_cost(year)
                    market_demand = self._generate_market_demand(year, row["crop"])

                    # Add to data
                    data_row = {
                        "year": year,
                        "crop": row["crop"],
                        "rainfall_mm": rainfall,
                        "temperature_c": temperature,
                        "humidity_percent": humidity,
                        "soil_ph": soil_ph,
                        "fertilizer_use_kg_ha": fertilizer_use,
                        "irrigation_area_percent": irrigation_area,
                        "fuel_price_usd_liter": fuel_price,
                        "labor_cost_usd_day": labor_cost,
                        "market_demand_index": market_demand,
                        "yield_per_hectare": row["yield_per_hectare"],
                        "area_hectares": row["area_hectares"],
                        "production_tons": row["production_tons"],
                        "farmers_count": row["farmers_count"],
                    }
                    all_data.append(data_row)

        return pd.DataFrame(all_data)

    def _generate_rainfall(self, year, crop):
        """Generate realistic rainfall data"""
        base_rainfall = 800  # mm/year average
        year_factor = 1 + (year - 2001) * 0.01  # Slight trend
        crop_factors = {
            "Rice": 1.1,  # Rice needs more water
            "Millet": 0.9,  # Millet is drought-resistant
            "Sorghum": 0.85,
            "Maize": 1.0,
            "Groundnuts": 0.95,
            "Cotton": 1.05,
            "Vegetables": 1.15,
            "Fruits": 1.1,
        }
        factor = crop_factors.get(crop, 1.0)
        return np.random.normal(base_rainfall * factor * year_factor, 150)

    def _generate_temperature(self, year, crop):
        """Generate realistic temperature data"""
        base_temp = 27  # Celsius average
        year_factor = 1 + (year - 2001) * 0.002  # Climate change trend
        crop_factors = {
            "Rice": 1.0,
            "Millet": 1.05,  # Millet tolerates higher temps
            "Sorghum": 1.05,
            "Maize": 1.02,
            "Groundnuts": 1.03,
            "Cotton": 1.04,
            "Vegetables": 0.98,
            "Fruits": 0.97,
        }
        factor = crop_factors.get(crop, 1.0)
        return np.random.normal(base_temp * factor * year_factor, 3)

    def _generate_humidity(self, year, crop):
        """Generate realistic humidity data"""
        base_humidity = 70  # % average
        year_factor = 1 + (year - 2001) * 0.005
        crop_factors = {
            "Rice": 1.15,  # Rice needs high humidity
            "Millet": 0.9,
            "Sorghum": 0.9,
            "Maize": 1.0,
            "Groundnuts": 0.95,
            "Cotton": 1.0,
            "Vegetables": 1.1,
            "Fruits": 1.05,
        }
        factor = crop_factors.get(crop, 1.0)
        return np.random.normal(base_humidity * factor * year_factor, 10)

    def _generate_soil_ph(self, crop):
        """Generate realistic soil pH data"""
        base_ph = 6.5
        crop_factors = {
            "Rice": 6.0,  # Rice prefers slightly acidic
            "Millet": 6.8,
            "Sorghum": 6.7,
            "Maize": 6.5,
            "Groundnuts": 6.2,  # Groundnuts prefer acidic
            "Cotton": 6.3,
            "Vegetables": 6.8,
            "Fruits": 6.6,
        }
        target_ph = crop_factors.get(crop, base_ph)
        return np.random.normal(target_ph, 0.5)

    def _generate_fertilizer_use(self, year, crop):
        """Generate realistic fertilizer use data"""
        base_fertilizer = 60  # kg/ha
        year_factor = 1 + (year - 2001) * 0.02  # Increasing use over time
        crop_factors = {
            "Rice": 1.2,  # Rice uses more fertilizer
            "Millet": 0.8,
            "Sorghum": 0.8,
            "Maize": 1.1,
            "Groundnuts": 0.9,
            "Cotton": 1.3,  # Cotton uses most fertilizer
            "Vegetables": 1.4,
            "Fruits": 1.1,
        }
        factor = crop_factors.get(crop, 1.0)
        return np.random.normal(base_fertilizer * factor * year_factor, 15)

    def _generate_irrigation_area(self, year, crop):
        """Generate realistic irrigation area data"""
        base_irrigation = 20  # % of total area
        year_factor = 1 + (year - 2001) * 0.03  # Increasing irrigation
        crop_factors = {
            "Rice": 1.5,  # Rice needs irrigation
            "Millet": 0.5,  # Millet is rain-fed
            "Sorghum": 0.6,
            "Maize": 0.8,
            "Groundnuts": 0.7,
            "Cotton": 1.2,
            "Vegetables": 1.8,  # Vegetables need irrigation
            "Fruits": 1.6,
        }
        factor = crop_factors.get(crop, 1.0)
        return np.random.normal(base_irrigation * factor * year_factor, 8)

    def _generate_fuel_price(self, year):
        """Generate realistic fuel price data"""
        base_price = 1.2  # USD/liter
        year_factor = 1 + (year - 2001) * 0.05  # Increasing fuel prices
        return np.random.normal(base_price * year_factor, 0.3)

    def _generate_labor_cost(self, year):
        """Generate realistic labor cost data"""
        base_cost = 15  # USD/day
        year_factor = 1 + (year - 2001) * 0.03  # Increasing labor costs
        return np.random.normal(base_cost * year_factor, 3)

    def _generate_market_demand(self, year, crop):
        """Generate realistic market demand data"""
        base_demand = 100  # index
        year_factor = 1 + (year - 2001) * 0.02  # Increasing demand
        crop_factors = {
            "Rice": 1.2,  # High demand for rice
            "Millet": 0.9,
            "Sorghum": 0.8,
            "Maize": 1.0,
            "Groundnuts": 1.1,
            "Cotton": 0.7,
            "Vegetables": 1.3,  # High demand for vegetables
            "Fruits": 1.4,  # High demand for fruits
        }
        factor = crop_factors.get(crop, 1.0)
        return np.random.normal(base_demand * factor * year_factor, 20)

    def prepare_features(self, df):
        """
        Prepare features for machine learning
        """
        # Create additional features
        df["rainfall_squared"] = df["rainfall_mm"] ** 2
        df["temperature_humidity_interaction"] = (
            df["temperature_c"] * df["humidity_percent"]
        )
        df["fertilizer_irrigation_interaction"] = (
            df["fertilizer_use_kg_ha"] * df["irrigation_area_percent"]
        )

        # Encode categorical variables
        le_crop = LabelEncoder()
        df["crop_encoded"] = le_crop.fit_transform(df["crop"])
        self.label_encoders["crop"] = le_crop

        # Select features for modeling
        feature_columns = [
            "rainfall_mm",
            "temperature_c",
            "humidity_percent",
            "soil_ph",
            "fertilizer_use_kg_ha",
            "irrigation_area_percent",
            "fuel_price_usd_liter",
            "labor_cost_usd_day",
            "market_demand_index",
            "rainfall_squared",
            "temperature_humidity_interaction",
            "fertilizer_irrigation_interaction",
            "crop_encoded",
        ]

        self.feature_names = feature_columns
        return df[feature_columns]

    def train_models(self, df, test_size=0.2, random_state=42):
        """
        Train models for yield, price, and production prediction
        """
        X = self.prepare_features(df)

        # Define targets
        targets = {
            "yield": df["yield_per_hectare"],
            "price": self._calculate_price_per_ton(
                df
            ),  # Calculate price from available data
            "production": df["production_tons"],
        }

        # Train models for each target
        for target_name, y in targets.items():
            print(f"\nTraining model for {target_name} prediction...")

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )

            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            self.scalers[target_name] = scaler

            # Try different models and select the best one
            models = {
                "Random Forest": RandomForestRegressor(
                    n_estimators=100, random_state=random_state
                ),
                "Gradient Boosting": GradientBoostingRegressor(
                    n_estimators=100, random_state=random_state
                ),
                "Ridge Regression": Ridge(alpha=1.0),
                "Linear Regression": LinearRegression(),
            }

            best_model = None
            best_score = -np.inf

            for name, model in models.items():
                # Cross-validation score
                cv_scores = cross_val_score(
                    model, X_train_scaled, y_train, cv=5, scoring="r2"
                )
                mean_cv_score = cv_scores.mean()

                print(
                    f"  {name}: CV R² = {mean_cv_score:.4f} (+/- {cv_scores.std() * 2:.4f})"
                )

                if mean_cv_score > best_score:
                    best_score = mean_cv_score
                    best_model = model

            # Train the best model
            best_model.fit(X_train_scaled, y_train)

            # Evaluate on test set
            y_pred = best_model.predict(X_test_scaled)
            test_r2 = r2_score(y_test, y_pred)
            test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            test_mae = mean_absolute_error(y_test, y_pred)

            print(f"  Best model: {type(best_model).__name__}")
            print(f"  Test R² = {test_r2:.4f}")
            print(f"  Test RMSE = {test_rmse:.4f}")
            print(f"  Test MAE = {test_mae:.4f}")

            self.models[target_name] = best_model

        self.is_trained = True
        print("\nAll models trained successfully!")

    def _calculate_price_per_ton(self, df):
        """
        Calculate price per ton based on production and market factors
        """
        # Use a combination of production volume and market demand to estimate price
        # Higher production typically leads to lower prices (supply-demand)
        # Higher market demand leads to higher prices

        base_prices = {
            "Rice": 300,
            "Millet": 250,
            "Sorghum": 240,
            "Maize": 280,
            "Groundnuts": 400,
            "Cotton": 800,
            "Vegetables": 500,
            "Fruits": 600,
        }

        prices = []
        for _, row in df.iterrows():
            base_price = base_prices.get(row["crop"], 300)

            # Adjust price based on production volume (inverse relationship)
            production_factor = 1 / (1 + row["production_tons"] / 100000)

            # Adjust price based on market demand
            demand_factor = row["market_demand_index"] / 100

            # Add some random variation
            random_factor = np.random.normal(1, 0.1)

            price = base_price * production_factor * demand_factor * random_factor
            prices.append(max(100, price))  # Ensure minimum price

        return pd.Series(prices)

    def predict(self, input_data):
        """
        Make predictions for new data
        """
        if not self.is_trained:
            raise ValueError("Models must be trained before making predictions")

        # Prepare input data
        if isinstance(input_data, dict):
            input_df = pd.DataFrame([input_data])
        else:
            input_df = input_data.copy()

        # Add derived features
        input_df["rainfall_squared"] = input_df["rainfall_mm"] ** 2
        input_df["temperature_humidity_interaction"] = (
            input_df["temperature_c"] * input_df["humidity_percent"]
        )
        input_df["fertilizer_irrigation_interaction"] = (
            input_df["fertilizer_use_kg_ha"] * input_df["irrigation_area_percent"]
        )

        # Encode crop if needed
        if "crop" in input_df.columns:
            input_df["crop_encoded"] = self.label_encoders["crop"].transform(
                input_df["crop"]
            )

        # Select features
        X = input_df[self.feature_names]

        # Make predictions
        predictions = {}
        for target_name, model in self.models.items():
            X_scaled = self.scalers[target_name].transform(X)
            predictions[target_name] = model.predict(X_scaled)

        return predictions

    def get_feature_importance(self, target="yield"):
        """
        Get feature importance for a specific target
        """
        if not self.is_trained:
            raise ValueError("Models must be trained before getting feature importance")

        model = self.models[target]
        if hasattr(model, "feature_importances_"):
            importance = model.feature_importances_
        else:
            # For linear models, use absolute coefficients
            importance = np.abs(model.coef_)

        feature_importance_df = pd.DataFrame(
            {"feature": self.feature_names, "importance": importance}
        ).sort_values("importance", ascending=False)

        return feature_importance_df

    def save_model(self, filepath):
        """
        Save the trained model
        """
        model_data = {
            "models": self.models,
            "scalers": self.scalers,
            "label_encoders": self.label_encoders,
            "feature_names": self.feature_names,
            "is_trained": self.is_trained,
        }
        joblib.dump(model_data, filepath)
        print(f"Model saved to {filepath}")

    def load_model(self, filepath):
        """
        Load a trained model
        """
        model_data = joblib.load(filepath)
        self.models = model_data["models"]
        self.scalers = model_data["scalers"]
        self.label_encoders = model_data["label_encoders"]
        self.feature_names = model_data["feature_names"]
        self.is_trained = model_data["is_trained"]
        print(f"Model loaded from {filepath}")
