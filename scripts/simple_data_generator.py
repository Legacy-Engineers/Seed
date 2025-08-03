#!/usr/bin/env python3
"""
Simple script to generate agricultural datasets for The Gambia from 2004 to 2021
"""

import csv
import os
from pathlib import Path
import math
from datetime import datetime


def generate_crop_data():
    """Generate crop production data for 2004-2021"""
    crops_data = {}

    # Base crops from 2004 data
    base_crops = [
        ["Rice", 50000, 200000, 4.0, 16500],
        ["Millet", 38000, 76000, 2.0, 12600],
        ["Sorghum", 28000, 56000, 2.0, 8600],
        ["Maize", 18000, 36000, 2.0, 6600],
        ["Groundnuts", 85000, 170000, 2.0, 21500],
        ["Cotton", 5500, 8800, 1.6, 2300],
        ["Vegetables", 13000, 26000, 2.0, 8600],
        ["Fruits", 9200, 18400, 2.0, 5600],
    ]

    for year in range(2004, 2022):
        # Apply growth factors
        growth_factor = 1 + (year - 2004) * 0.02  # 2% annual growth
        climate_factor = 1 + math.sin((year - 2004) * 0.3) * 0.1  # Climate variability

        year_data = []
        for crop in base_crops:
            area = int(crop[1] * growth_factor * climate_factor)
            production = int(crop[2] * growth_factor * climate_factor)
            yield_per_hectare = round(crop[3] * (1 + (year - 2004) * 0.01), 1)
            farmers = int(crop[4] * growth_factor)

            year_data.append([crop[0], area, production, yield_per_hectare, farmers])

        crops_data[year] = year_data

    return crops_data


def generate_fisheries_data():
    """Generate fisheries data for 2004-2021"""
    fisheries_data = {}

    # Base fisheries data
    base_fisheries = [
        ["Fresh Fish", 28000, 168, 5300],
        ["Dried Fish", 9000, 54, 2150],
        ["Smoked Fish", 6000, 36, 1650],
        ["Crustaceans", 2500, 18.75, 860],
        ["Molluscs", 2000, 16, 660],
    ]

    for year in range(2004, 2022):
        growth_factor = 1 + (year - 2004) * 0.015  # 1.5% annual growth
        climate_factor = 1 + math.sin((year - 2004) * 0.2) * 0.15

        year_data = []
        for fishery in base_fisheries:
            production = int(fishery[1] * growth_factor * climate_factor)
            value = round(fishery[2] * growth_factor * climate_factor, 1)
            fishermen = int(fishery[3] * growth_factor)

            year_data.append([fishery[0], production, value, fishermen])

        fisheries_data[year] = year_data

    return fisheries_data


def generate_sales_data():
    """Generate sales data for 2004-2021"""
    sales_data = {}

    # Base sales data
    base_sales = [
        ["Cereals", 135000, 270, 8600],
        ["Groundnuts", 88000, 176, 15600],
        ["Vegetables", 18000, 54, 6600],
        ["Fish", 23000, 138, 3300],
        ["Livestock", 5800, 116, 2300],
        ["Fruits", 9500, 38, 4600],
    ]

    for year in range(2004, 2022):
        growth_factor = 1 + (year - 2004) * 0.025  # 2.5% annual growth
        market_factor = 1 + math.sin((year - 2004) * 0.25) * 0.1

        year_data = []
        for sale in base_sales:
            quantity = int(sale[1] * growth_factor * market_factor)
            value = round(sale[2] * growth_factor * market_factor, 1)
            farmers = int(sale[3] * growth_factor)

            year_data.append([sale[0], quantity, value, farmers])

        sales_data[year] = year_data

    return sales_data


def generate_livestock_data():
    """Generate livestock data for 2004-2021"""
    livestock_data = {}

    # Base livestock data
    base_livestock = [
        ["Cattle", 330000, 330, 8600],
        ["Sheep", 165000, 49.5, 12600],
        ["Goats", 215000, 43, 15600],
        ["Poultry", 1060000, 53, 26500],
        ["Pigs", 56000, 28, 3300],
        ["Horses", 8600, 17.2, 2150],
        ["Donkeys", 13200, 13.2, 3150],
    ]

    for year in range(2004, 2022):
        growth_factor = 1 + (year - 2004) * 0.018  # 1.8% annual growth
        health_factor = 1 + math.sin((year - 2004) * 0.15) * 0.05

        year_data = []
        for livestock in base_livestock:
            population = int(livestock[1] * growth_factor * health_factor)
            value = round(livestock[2] * growth_factor * health_factor, 1)
            farmers = int(livestock[3] * growth_factor)

            year_data.append([livestock[0], population, value, farmers])

        livestock_data[year] = year_data

    return livestock_data


def generate_practices_data():
    """Generate farm practices data for 2004-2021"""
    practices_data = {}

    # Base practices data
    base_practices = [
        ["Irrigation", 5600, 23000, 16.5],
        ["Fertilizer Use", 15600, 86000, 61.5],
        ["Pesticide Use", 8600, 66000, 46.5],
        ["Mechanization", 3300, 28000, 21.0],
        ["Organic Farming", 2300, 18000, 12.5],
    ]

    for year in range(2004, 2022):
        tech_growth = 1 + (year - 2004) * 0.03  # 3% annual technology adoption
        policy_factor = 1 + math.sin((year - 2004) * 0.1) * 0.08

        year_data = []
        for practice in base_practices:
            farmers = int(practice[1] * tech_growth * policy_factor)
            area = int(practice[2] * tech_growth * policy_factor)
            percentage = round(practice[3] * tech_growth, 1)

            year_data.append([practice[0], farmers, area, percentage])

        practices_data[year] = year_data

    return practices_data


def generate_tenure_data():
    """Generate land tenure data for 2004-2021"""
    tenure_data = {}

    # Base tenure data
    base_tenure = [
        ["Owned Land", 26500, 86000, 35.6],
        ["Rented Land", 8600, 33000, 11.9],
        ["Communal Land", 12600, 43000, 16.4],
        ["Leased Land", 5300, 21500, 7.0],
        ["Inherited Land", 15600, 53000, 21.0],
    ]

    for year in range(2004, 2022):
        legal_growth = 1 + (year - 2004) * 0.012  # 1.2% annual legal changes
        social_factor = 1 + math.sin((year - 2004) * 0.08) * 0.03

        year_data = []
        for tenure in base_tenure:
            farmers = int(tenure[1] * legal_growth * social_factor)
            area = int(tenure[2] * legal_growth * social_factor)
            percentage = round(tenure[3] * legal_growth, 1)

            year_data.append([tenure[0], farmers, area, percentage])

        tenure_data[year] = year_data

    return tenure_data


def save_dataset(data, filename, headers):
    """Save dataset to CSV file"""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)


def main():
    """Main function to generate datasets"""
    print("Generating agricultural datasets for The Gambia (2004-2021)...")

    # Create data directory structure
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    # Generate all datasets
    crops_data = generate_crop_data()
    fisheries_data = generate_fisheries_data()
    sales_data = generate_sales_data()
    livestock_data = generate_livestock_data()
    practices_data = generate_practices_data()
    tenure_data = generate_tenure_data()

    # Save datasets for each year
    for year in range(2004, 2022):
        year_dir = data_dir / str(year)
        year_dir.mkdir(exist_ok=True)

        print(f"Processing year {year}...")

        # Save crops data
        crops_file = year_dir / f"crops_{year}.csv"
        save_dataset(
            crops_data[year],
            crops_file,
            [
                "crop",
                "area_hectares",
                "production_tons",
                "yield_per_hectare",
                "farmers_count",
            ],
        )

        # Save fisheries data
        fisheries_file = year_dir / f"fisheries_{year}.csv"
        save_dataset(
            fisheries_data[year],
            fisheries_file,
            ["fish_type", "production_tons", "value_million_dalasi", "fishermen_count"],
        )

        # Save sales data
        sales_file = year_dir / f"sales_{year}.csv"
        save_dataset(
            sales_data[year],
            sales_file,
            [
                "product_category",
                "quantity_sold_tons",
                "value_million_dalasi",
                "farmers_selling",
            ],
        )

        # Save livestock data
        livestock_file = year_dir / f"livestock_{year}.csv"
        save_dataset(
            livestock_data[year],
            livestock_file,
            ["animal_type", "population", "value_million_dalasi", "farmers_owning"],
        )

        # Save farm practices data
        practices_file = year_dir / f"practices_{year}.csv"
        save_dataset(
            practices_data[year],
            practices_file,
            ["practice", "farmers_count", "area_hectares", "percentage_of_total"],
        )

        # Save land tenure data
        tenure_file = year_dir / f"tenure_{year}.csv"
        save_dataset(
            tenure_data[year],
            tenure_file,
            ["tenure_type", "farmers_count", "area_hectares", "percentage_of_farmers"],
        )

    # Create summary file
    summary_file = data_dir / "dataset_summary.txt"
    with open(summary_file, "w") as f:
        f.write("Gambia Agricultural Census Data Summary\n")
        f.write("=====================================\n\n")
        f.write(
            "Data Source: Extended dataset generation based on FAO Agricultural Census Report\n"
        )
        f.write("Years Covered: 2004 to 2021\n\n")
        f.write("Dataset Categories:\n")
        f.write("- crops: Crop production data (area, production, yield, farmers)\n")
        f.write("- fisheries: Fisheries data (production, value, fishermen)\n")
        f.write("- sales: Market sales data (quantities, values, selling farmers)\n")
        f.write("- livestock: Livestock population data (animals, values, owners)\n")
        f.write("- practices: Farm practices data (irrigation, fertilizer, etc.)\n")
        f.write("- tenure: Land tenure data (ownership patterns)\n\n")
        f.write("File Structure:\n")
        f.write("- data/YYYY/crops_YYYY.csv\n")
        f.write("- data/YYYY/fisheries_YYYY.csv\n")
        f.write("- data/YYYY/sales_YYYY.csv\n")
        f.write("- data/YYYY/livestock_YYYY.csv\n")
        f.write("- data/YYYY/practices_YYYY.csv\n")
        f.write("- data/YYYY/tenure_YYYY.csv\n")
        f.write("(for years 2004 to 2021)\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print("Dataset generation complete!")
    print(f"Created datasets for years: 2004 to 2021")
    print(f"Total files created: 108 (6 categories × 18 years)")
    print(f"Data directory: {data_dir.absolute()}")


if __name__ == "__main__":
    main()
