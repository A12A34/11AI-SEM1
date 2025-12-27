import os
import tkinter as tk
import json
from pathlib import Path

BASE_DIR = Path(os.getcwd())
devices_file = Path("C:\\Users\\PC\\.vscode\\repos\\11AI\\PL\\devices_final\\devices_data.json") if os.name == "nt" else Path(BASE_DIR / "devices_data.json")

def enter_boolen_check(entry_name, prompt, option):
    for widget in frame_top.winfo_children():
        widget.destroy()
    get_input = entry_name.get().strip().lower()
    if option != get_input:
        label = tk.Label(frame_top, text=prompt)
        label.grid(row=0, column=0, sticky="w")

def enter_number_check(entry_name, prompt, min_value, max_value):
    for widget in frame_top.winfo_children():
        widget.destroy()
    get_input = entry_name.get().strip()
    if not get_input.isdigit() or not (min_value <= int(get_input) <= max_value):
        label = tk.Label(frame_top, text=prompt)
        label.grid(row=0, column=0, sticky="w")

def entry_string_check(entry_name, prompt, min_length, max_length):
    for widget in frame_top.winfo_children():
        widget.destroy()
    get_input = entry_name.get().strip()
    if not (min_length <= len(get_input) <= max_length):
        label = tk.Label(frame_top, text=prompt)
        label.grid(row=0, column=0, sticky="w")

def load_devices_data():
    if os.path.exists(devices_file):
        with open(devices_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def add_device_data(device):
    devices_data = load_devices_data()
    devices_data.append(device)
    with open(devices_file, "w", encoding="utf-8") as file:
        json.dump(devices_data, file, indent=4)

def show_devices():
    for widget in frame_right.winfo_children():
        widget.destroy()

    devices_data = load_devices_data()

    if devices_data:
        label_row = 0
        for device in devices_data:
            label_column = 0
            for key, value in device.items():
                label = tk.Label(frame_right, text="|")
                label.grid(row=label_row, column=label_column, sticky="nsew")

                button = tk.Button(frame_right, text=f"{key}: {value}")
                button.grid(row=label_row, column=label_column + 1, sticky="nsew")

                frame_right.grid_columnconfigure(label_column, weight=0)
                frame_right.grid_columnconfigure(label_column + 1, weight=1)

                label_column += 2
            frame_right.grid_rowconfigure(label_row, weight=0)
            label_row += 1

def create_device():
    for widget in frame_right.winfo_children():
        widget.destroy()

    devices_data = load_devices_data()
    entry_row = 0

    for data in devices_data:
        for key, value in data.items():
            label = tk.Label(frame_right, text=key)
            entry = tk.Entry(frame_right)

            label.grid(row=entry_row, column=0, sticky="e")
            entry.grid(row=entry_row, column=1, sticky="nsew")

            frame_right.grid_columnconfigure(1, weight=1)
            entry_row += 1

        def collect_device_data():
            device = {}
            for i, (key, _) in enumerate(data.items()):
                entry_widget = frame_right.grid_slaves(row=i, column=1)[0]
                device[key] = entry_widget.get().strip()
            add_device_data(device)

        button = tk.Button(frame_right, text="Submit", command=collect_device_data)
        button.grid(row=entry_row, column=0, columnspan=2, sticky="nsew")
        break

def delete_device():
    for widget in frame_right.winfo_children():
        widget.destroy()

    label = tk.Label(frame_right, text="Enter Device ID:")
    label.grid(row=0, column=0, sticky="e")

    entry = tk.Entry(frame_right)
    entry.grid(row=0, column=1, sticky="nsew")

    frame_right.grid_columnconfigure(1, weight=1)

    def confirm_delete():
        devices_data = load_devices_data()
        device_id = entry.get().strip()
        for i, device in enumerate(devices_data):
            if device.get("device_id") == device_id:
                devices_data.pop(i)
                save_data(devices_data)
                return

    button = tk.Button(frame_right, text="Delete", command=confirm_delete)
    button.grid(row=1, column=0, columnspan=2, sticky="nsew")

def save_data(data):
    for widget in frame_right.winfo_children():
        widget.destroy()
    with open(devices_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def main_menu():
    button_show_devices = tk.Button(frame_left, text="Show Devices", command=show_devices)
    button_create_device = tk.Button(frame_left, text="Create Device", command=create_device)
    button_delete_device = tk.Button(frame_left, text="Delete Device", command=delete_device)

    button_show_devices.grid(row=0, column=0, sticky="nsew")
    button_create_device.grid(row=1, column=0, sticky="nsew")
    button_delete_device.grid(row=2, column=0, sticky="nsew")

    frame_left.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Devices Final")
    window.geometry("800x600")

    frame_left = tk.Frame(window)
    frame_right = tk.Frame(window)
    frame_top = tk.Frame(window)

    frame_left.pack(side=tk.LEFT, fill=tk.Y)
    frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    frame_top.pack(side=tk.TOP, fill=tk.X)

    main_menu()
    window.mainloop()
