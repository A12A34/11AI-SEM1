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
    global fields, entries
    clear_frame(frame_right)

    data = load_devices_data()
    if not data:
        return

    fields = list(data[0].keys())
    entries = []

    for row, field in enumerate(fields):
        label = tk.Label(frame_right, text=f"{field}:")
        label.grid(row=row, column=0, sticky="w")

        entry = tk.Entry(frame_right)
        entry.grid(row=row, column=1, sticky="ew")
        entries.append(entry)

    submit_button = tk.Button(frame_right, text="Submit", command=submit)
    submit_button.grid(row=len(fields), column=0, columnspan=2, sticky="ew")

    frame_right.grid_columnconfigure(1, weight=1)


def submit():
    device = {}
    for field, entry in zip(fields, entries):
        device[field] = entry.get().strip()
    add_device_data(device)


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
        tk.Label(frame_right, text="No devices found").grid(row=0, column=0)
        return

    # Search input
    tk.Label(frame_right, text="Search value:").grid(row=0, column=0, sticky="w")
    search_entry = tk.Entry(frame_right)
    search_entry.grid(row=0, column=1, sticky="ew")

    frame_right.grid_columnconfigure(1, weight=1)

    # Frame for results ONLY
    result_frame = tk.Frame(frame_right)
    result_frame.grid(row=2, column=0, columnspan=10, sticky="nsew")

    def search_by_key(key):
        clear_frame(result_frame)

        value = search_entry.get().strip()
        found = False
        row = 0

        for device in devices:
            if device.get(key) == value:
                found = True
                for k, v in device.items():
                    tk.Button(result_frame, text=f"{k}: {v}").grid(row=row, column=0, sticky="w")
                    row += 1
                tk.Label(result_frame, text="----------------").grid(row=row, column=0)
                frame_right.grid_columnconfigure(row, weight=1)
                row += 1


        if not found:
            tk.Label(result_frame, text="No matching device").grid(row=0, column=0)
        
    # Search buttons
    for col, key in enumerate(devices[0].keys()):
        tk.Button(
            frame_right,
            text=f"by {key}",
            command=lambda k=key: search_by_key(k)).grid(row=1, column=col, sticky="nsew")


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
