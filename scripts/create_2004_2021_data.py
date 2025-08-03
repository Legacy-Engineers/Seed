#!/usr/bin/env python3
import csv
import os

# Create data directories
for year in range(2004, 2022):
    os.makedirs(f"data/{year}", exist_ok=True)

# Base data for 2004
crops_2004 = [
    ["Rice", 50000, 200000, 4.0, 16500],
    ["Millet", 38000, 76000, 2.0, 12600],
    ["Sorghum", 28000, 56000, 2.0, 8600],
    ["Maize", 18000, 36000, 2.0, 6600],
    ["Groundnuts", 85000, 170000, 2.0, 21500],
    ["Cotton", 5500, 8800, 1.6, 2300],
    ["Vegetables", 13000, 26000, 2.0, 8600],
    ["Fruits", 9200, 18400, 2.0, 5600],
]

fisheries_2004 = [
    ["Fresh Fish", 28000, 168, 5300],
    ["Dried Fish", 9000, 54, 2150],
    ["Smoked Fish", 6000, 36, 1650],
    ["Crustaceans", 2500, 18.75, 860],
    ["Molluscs", 2000, 16, 660],
]

sales_2004 = [
    ["Cereals", 135000, 270, 8600],
    ["Groundnuts", 88000, 176, 15600],
    ["Vegetables", 18000, 54, 6600],
    ["Fish", 23000, 138, 3300],
    ["Livestock", 5800, 116, 2300],
    ["Fruits", 9500, 38, 4600],
]

livestock_2004 = [
    ["Cattle", 330000, 330, 8600],
    ["Sheep", 165000, 49.5, 12600],
    ["Goats", 215000, 43, 15600],
    ["Poultry", 1060000, 53, 26500],
    ["Pigs", 56000, 28, 3300],
    ["Horses", 8600, 17.2, 2150],
    ["Donkeys", 13200, 13.2, 3150],
]

practices_2004 = [
    ["Irrigation", 5600, 23000, 16.5],
    ["Fertilizer Use", 15600, 86000, 61.5],
    ["Pesticide Use", 8600, 66000, 46.5],
    ["Mechanization", 3300, 28000, 21.0],
    ["Organic Farming", 2300, 18000, 12.5],
]

tenure_2004 = [
    ["Owned Land", 26500, 86000, 35.6],
    ["Rented Land", 8600, 33000, 11.9],
    ["Communal Land", 12600, 43000, 16.4],
    ["Leased Land", 5300, 21500, 7.0],
    ["Inherited Land", 15600, 53000, 21.0],
]

# Generate data for each year
for year in range(2004, 2022):
    print(f"Creating data for {year}...")

    # Calculate growth factors
    growth_factor = 1 + (year - 2004) * 0.02

    # Generate crops data
    crops_data = []
    for crop in crops_2004:
        area = int(crop[1] * growth_factor)
        production = int(crop[2] * growth_factor)
        yield_per_hectare = round(crop[3] * (1 + (year - 2004) * 0.01), 1)
        farmers = int(crop[4] * growth_factor)
        crops_data.append([crop[0], area, production, yield_per_hectare, farmers])

    # Save crops data
    with open(f"data/{year}/crops_{year}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "crop",
                "area_hectares",
                "production_tons",
                "yield_per_hectare",
                "farmers_count",
            ]
        )
        writer.writerows(crops_data)

    # Generate fisheries data
    fisheries_data = []
    for fishery in fisheries_2004:
        production = int(fishery[1] * growth_factor)
        value = round(fishery[2] * growth_factor, 1)
        fishermen = int(fishery[3] * growth_factor)
        fisheries_data.append([fishery[0], production, value, fishermen])

    # Save fisheries data
    with open(f"data/{year}/fisheries_{year}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["fish_type", "production_tons", "value_million_dalasi", "fishermen_count"]
        )
        writer.writerows(fisheries_data)

    # Generate sales data
    sales_data = []
    for sale in sales_2004:
        quantity = int(sale[1] * growth_factor)
        value = round(sale[2] * growth_factor, 1)
        farmers = int(sale[3] * growth_factor)
        sales_data.append([sale[0], quantity, value, farmers])

    # Save sales data
    with open(f"data/{year}/sales_{year}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "product_category",
                "quantity_sold_tons",
                "value_million_dalasi",
                "farmers_selling",
            ]
        )
        writer.writerows(sales_data)

    # Generate livestock data
    livestock_data = []
    for livestock in livestock_2004:
        population = int(livestock[1] * growth_factor)
        value = round(livestock[2] * growth_factor, 1)
        farmers = int(livestock[3] * growth_factor)
        livestock_data.append([livestock[0], population, value, farmers])

    # Save livestock data
    with open(f"data/{year}/livestock_{year}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["animal_type", "population", "value_million_dalasi", "farmers_owning"]
        )
        writer.writerows(livestock_data)

    # Generate practices data
    practices_data = []
    for practice in practices_2004:
        farmers = int(practice[1] * growth_factor)
        area = int(practice[2] * growth_factor)
        percentage = round(practice[3] * growth_factor, 1)
        practices_data.append([practice[0], farmers, area, percentage])

    # Save practices data
    with open(f"data/{year}/practices_{year}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["practice", "farmers_count", "area_hectares", "percentage_of_total"]
        )
        writer.writerows(practices_data)

    # Generate tenure data
    tenure_data = []
    for tenure in tenure_2004:
        farmers = int(tenure[1] * growth_factor)
        area = int(tenure[2] * growth_factor)
        percentage = round(tenure[3] * growth_factor, 1)
        tenure_data.append([tenure[0], farmers, area, percentage])

    # Save tenure data
    with open(f"data/{year}/tenure_{year}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["tenure_type", "farmers_count", "area_hectares", "percentage_of_farmers"]
        )
        writer.writerows(tenure_data)

print("Data generation complete!")
print("Created datasets for years 2004-2021")
print("Total files: 108 (6 categories × 18 years)")
