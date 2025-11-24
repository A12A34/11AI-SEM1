#!/usr/bin/env python3
import csv
from pathlib import Path

FILE_NAME = Path("PL/W4/nv24214_DATA.csv")

new_record = ["AA55587", "iPhone 14", 15, 200.0]

try:
    if not FILE_NAME.exists():
        print(f"{FILE_NAME} not found. Run Program 5 first to create the file.")
    else:
        with FILE_NAME.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(new_record)

        print(f"New record {new_record} has been successfully added to {FILE_NAME}")

        with FILE_NAME.open("r", newline="", encoding="utf-8") as f:
            total_lines = sum(1 for line in f)
        print(f"File now contains {total_lines} lines (including header).")
except Exception as e:
    print(f"Error appending to file: {e}")
