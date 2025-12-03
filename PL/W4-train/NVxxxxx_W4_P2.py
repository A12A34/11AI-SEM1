from pathlib import Path
import csv
file_name = "PL/W4-train/NVxxxxx_W4_D1.csv"
mode = "a" if Path(file_name).exists() else "w"
with open(file_name,mode,newline="",encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)
header = rows[0]
for row in rows[1:]:
    print()