#!/usr/bin/env python3
import csv
import os
from pathlib import Path
player_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
games_played = [15, 22, 18, 30, 12]
filepath = "PL/W4_SP_Data.csv"
with open(filepath, "w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Player Name", "Games Played"])
    for i in range(len(player_names)):
        writer.writerow([player_names[i], games_played[i]])
print("Data written to", filepath)

with open(filepath, "r",encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)
    for row in rows:
        print(row)

def display_data():
    headers = rows[0]
    print(f"{headers[0]:<15} | {headers[1]:<12}")
    print("-" * 30)
    for row in rows[1:]:
        print(f"{row[0]:<15} | {row[1]:<12}")
    print("-" * 30)
    print(f"Total Players: {len(rows) - 1}")
display_data()

while True:
    print("Menu:")
    print("1. View Data")
    print("2. Exit")
    choice = input("Enter your choice (1-2): ")
    if choice == '1':
        display_data()
    elif choice == '2':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")