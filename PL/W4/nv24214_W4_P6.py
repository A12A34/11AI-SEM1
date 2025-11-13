import csv
from pathlib import Path

FILE_NAME = Path("PL/W4/nv24214_DATA.csv")

try:
    if not FILE_NAME.exists():
        print(f"{FILE_NAME} not found. Run Program 5 (CSV Write) first.")
    else:
        with FILE_NAME.open("r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)

        headers = rows[0]
        print(f"{headers[0]:<12} | {headers[1]:<15} | {headers[2]:<8} | {headers[3]:<8}")
        print("-" * 52)

        for row in rows[1:]:
            print(f"{row[0]:<12} | {row[1]:<15} | {row[2]:<8} | {row[3]:<8}")
except Exception as e:
    print(f"Error reading file: {e}")
