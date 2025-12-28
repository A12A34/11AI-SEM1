import os
import tkinter as tk
import json
from pathlib import Path

# ===================== FILE PATH =====================
BASE_DIR = Path(os.getcwd())
devices_file = Path("C:\\Users\\PC\\.vscode\\repos\\11AI\\PL\\devices_final\\devices_data.json")

# ===================== DATA FUNCTIONS =====================
def load_devices_data():
    if devices_file.exists():
        with open(devices_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_devices_data(data):
    with open(devices_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def add_device_data(device):
    data = load_devices_data()
    data.append(device)
    save_devices_data(data)

# ===================== UI FUNCTIONS =====================
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# --------------------- SHOW DEVICES ---------------------
def show_devices():
    clear_frame(frame_right)

    devices = load_devices_data()
    if not devices:
        tk.Label(frame_right, text="No devices found").pack()
        return

    row = 0
    for device in devices:
        for key, value in device.items():
            tk.Button(frame_right, text=f"{key}: {value}", anchor="w")\
                .grid(row=row, column=0, sticky="nsew", padx=5)
            row += 1
        tk.Label(frame_right, text="----------------").grid(row=row, column=0)
        row += 1

# --------------------- CREATE DEVICE ---------------------
def create_device():
    clear_frame(frame_right)

    DEVICE_FIELDS = ["device_id", "name", "type", "price"]
    entries = {}

    for row, field in enumerate(DEVICE_FIELDS):
        tk.Label(frame_right, text=field).grid(row=row, column=0, sticky="nsew", padx=5)
        entry = tk.Entry(frame_right)
        entry.grid(row=row, column=1, sticky="nsew", padx=5)
        entries[field] = entry

    frame_right.grid_columnconfigure(1, weight=1)

    def submit():
        device = {k: v.get().strip() for k, v in entries.items()}
        if "" in device.values():
            clear_frame(frame_top)
            tk.Label(frame_top, text="All fields are required").pack()
            return
        add_device_data(device)
        clear_frame(frame_top)
        tk.Label(frame_top, text="Device added successfully").pack()

    tk.Button(frame_right, text="Submit", command=submit)\
        .grid(row=len(DEVICE_FIELDS), column=0, columnspan=2, sticky="nsew", pady=5)

# --------------------- DELETE DEVICE ---------------------
def delete_device():
    clear_frame(frame_right)

    tk.Label(frame_right, text="Enter Device ID:").grid(row=0, column=0, sticky="nsew")
    entry = tk.Entry(frame_right)
    entry.grid(row=0, column=1, sticky="nsew")

    frame_right.grid_columnconfigure(1, weight=1)

    def confirm():
        devices = load_devices_data()
        device_id = entry.get().strip()

        for i, device in enumerate(devices):
            if device.get("device_id") == device_id:
                devices.pop(i)
                save_devices_data(devices)
                clear_frame(frame_top)
                tk.Label(frame_top, text="Device deleted").pack()
                return

        clear_frame(frame_top)
        tk.Label(frame_top, text="Device ID not found").pack()

    tk.Button(frame_right, text="Delete", command=confirm)\
        .grid(row=1, column=0, columnspan=2, sticky="nsew", pady=5)

# --------------------- SEARCH DEVICE ---------------------
def search_device():
    clear_frame(frame_right)

    devices = load_devices_data()
    if not devices:
        tk.Label(frame_right, text="No devices found").pack()
        return

    tk.Label(frame_right, text="Search value:").grid(row=0, column=0, sticky="e")
    search_entry = tk.Entry(frame_right)
    search_entry.grid(row=0, column=1, sticky="nsew")

    def search_by_key(key):
        clear_frame(frame_right)
        value = search_entry.get().strip()

        found = False
        row = 0
        for device in devices:
            if device.get(key) == value:
                found = True
                for k, v in device.items():
                    tk.Label(frame_right, text=f"{k}: {v}")\
                        .grid(row=row, column=0, sticky="nsew")
                    row += 1
                tk.Label(frame_right, text="----------------")\
                    .grid(row=row, column=0)
                row += 1

        if not found:
            tk.Label(frame_right, text="No matching device").pack()

    col = 0
    for key in devices[0].keys():
        tk.Button(
            frame_right,
            text=f"by {key}",
            command=lambda k=key: search_by_key(k)
        ).grid(row=1, column=col, padx=2, sticky="nsew")
        col += 1

# ===================== MAIN MENU =====================
def main_menu():
    tk.Button(frame_left, text="Show Devices", command=show_devices)\
        .grid(row=0, column=0, sticky="nsew")
    tk.Button(frame_left, text="Create Device", command=create_device)\
        .grid(row=1, column=0, sticky="nsew")
    tk.Button(frame_left, text="Delete Device", command=delete_device)\
        .grid(row=2, column=0, sticky="nsew")
    tk.Button(frame_left, text="Search Device", command=search_device)\
        .grid(row=3, column=0, sticky="nsew")

    frame_left.grid_columnconfigure(0, weight=1)

# ===================== WINDOW =====================
window = tk.Tk()
window.title("Devices Final")
window.geometry("800x600")

frame_left = tk.Frame(window)
frame_right = tk.Frame(window)
frame_top = tk.Frame(window)

frame_left.pack(side=tk.LEFT, fill=tk.Y)
frame_top.pack(side=tk.TOP, fill=tk.X)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

main_menu()
window.mainloop()
