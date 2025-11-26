#!/usr/bin/env python3
import csv
FILE_NAME = "PL/W4/nv24214_DATA.csv"

device_ids = ["AA52554", "AA53565", "AA54576", "AA55587", "AA56598"]
device_names = ["iPhone 11", "iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15"]
stock_values = [45, 65, 25, 15, 5]
prices = [200.0, 200.0, 200.0, 200.0, 200.0]

with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Stock", "Price"])
    for i in range(len(device_ids)):
        writer.writerow([device_ids[i], device_names[i], stock_values[i], prices[i]])

print(f"Data has been written to {FILE_NAME}")
