#!/usr/bin/env python3
import csv
from pathlib import Path

FILE_NAME = "PL/W4/nv24214_DATA.csv"

if not Path(FILE_NAME).exists():
    print(f"Error: '{FILE_NAME}' not found.")
    print("Please run Program 1 first to create the CSV file.")
else:
    new_record = ["AA57599", "Samsung S22", 40, 180.0]

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(new_record)

    print(f"New record appended successfully to {FILE_NAME}")

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    total_records = len(rows) - 1
    print(f"Total records (excluding header): {total_records}")
