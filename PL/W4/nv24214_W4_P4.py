import csv
from pathlib import Path

FILE_NAME = "PL/W4/nv24214_DATA.csv"

if not Path(FILE_NAME).exists():
    print(f"Error: '{FILE_NAME}' not found.")
    print("Please run Program 1 first to create the CSV file.")
else:
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    device_ids = []
    device_names = []
    stock_values = []
    prices = []

    for row in rows[1:]:
        device_ids.append(row[0])
        device_names.append(row[1])
        stock_values.append(int(row[2]))
        prices.append(float(row[3]))

    print("Rebuilt lists from CSV:")
    print(f"Device IDs: {device_ids}")
    print(f"Device Names: {device_names}")
    print(f"Stock Values: {stock_values}")
    print(f"Prices: {prices}")
    print(f"\nTotal records rebuilt: {len(device_ids)}")
