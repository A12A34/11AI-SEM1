#!/usr/bin/env python3
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

    headers = rows[0]
    print(f"{headers[0]:<12} | {headers[1]:<15} | {headers[2]:<8} | {headers[3]:<8}")
    print("-" * 52)

    for r in rows[1:]:
        print(f"{r[0]:<12} | {r[1]:<15} | {r[2]:<8} | {r[3]:<8}")

    print(f"\nDisplayed {len(rows) - 1} device records.")
