#!/usr/bin/env python3
"""
Verification script to show summary of all created datasets
"""

import os
from pathlib import Path


def count_files_in_directory(directory):
    """Count CSV files in a directory"""
    if not os.path.exists(directory):
        return 0
    return len([f for f in os.listdir(directory) if f.endswith(".csv")])


def main():
    print("=== Gambia Agricultural Datasets Verification ===\n")

    data_dir = Path("data")
    years = [2001, 2002, 2003, 2004]
    categories = ["crops", "fisheries", "sales", "livestock", "practices", "tenure"]

    total_files = 0

    for year in years:
        year_dir = data_dir / str(year)
        if year_dir.exists():
            file_count = count_files_in_directory(year_dir)
            total_files += file_count
            print(f"Year {year}: {file_count} datasets")

            # List the files
            for category in categories:
                csv_file = year_dir / f"{category}_{year}.csv"
                if csv_file.exists():
                    print(f"  ✓ {category}_{year}.csv")
                else:
                    print(f"  ✗ {category}_{year}.csv (missing)")
            print()

    print(f"Total datasets created: {total_files}")
    print(f"Expected datasets: {len(years) * len(categories)}")

    if total_files == len(years) * len(categories):
        print("✓ All datasets successfully created!")
    else:
        print("✗ Some datasets are missing")

    # Show summary file
    summary_file = data_dir / "dataset_summary.txt"
    if summary_file.exists():
        print(f"\n✓ Summary file created: {summary_file}")
        with open(summary_file, "r") as f:
            content = f.read()
            print(f"Summary file size: {len(content)} characters")

    print("\n=== Dataset Categories ===")
    print(
        "1. Crops: Rice, Millet, Sorghum, Maize, Groundnuts, Cotton, Vegetables, Fruits"
    )
    print("2. Fisheries: Fresh Fish, Dried Fish, Smoked Fish, Crustaceans, Molluscs")
    print("3. Sales: Cereals, Groundnuts, Vegetables, Fish, Livestock, Fruits")
    print("4. Livestock: Cattle, Sheep, Goats, Poultry, Pigs, Horses, Donkeys")
    print(
        "5. Farm Practices: Irrigation, Fertilizer Use, Pesticide Use, Mechanization, Organic Farming"
    )
    print(
        "6. Land Tenure: Owned Land, Rented Land, Communal Land, Leased Land, Inherited Land"
    )

    print("\n=== Data Sources ===")
    print("• FAO Agricultural Census Report 2001/2002")
    print("• GBOS (Gambia Bureau of Statistics) Data")
    print("• Years covered: 2001, 2002, 2003, 2004")


if __name__ == "__main__":
    main()
