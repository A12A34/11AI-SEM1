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

        ids = [row[0] for row in rows[1:]]
        names = [row[1] for row in rows[1:]]
        int_values = [int(row[2]) for row in rows[1:]]
        float_values = [float(row[3]) for row in rows[1:]]

        print("IDs:", ids)
        print("Names:", names)
        print("Integer values:", int_values)
        print("Float values:", float_values)
        print(f"\nTotal records rebuilt: {len(ids)}")
except Exception as e:
    print(f"Error rebuilding lists from file: {e}")
