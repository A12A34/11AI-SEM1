import os
import tkinter as tk
import json
from pathlib import Path

# ===================== FILE PATH =====================
BASE_DIR = Path(__file__).parent
devices_file = BASE_DIR / "devices_data.json"

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
        tk.Label(frame_right, text="No devices found", fg="gray").pack(pady=20)
        clear_frame(table_frame)
        return

    # Show info in right frame
    tk.Label(frame_right, text="All Devices", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(frame_right, text=f"Total devices: {len(devices)}", fg="gray").pack()
    
    # Display table in bottom frame
    display_table(devices)

# --------------------- CREATE DEVICE ---------------------
def create_device():
    clear_frame(frame_right)
    clear_frame(table_frame)

    data = load_devices_data()
    if not data:
        tk.Label(frame_right, text="No template found. Please add at least one device manually first.").pack()
        return

    fields = list(data[0].keys())
    entries = []

    for row, field in enumerate(fields):
        label = tk.Label(frame_right, text=f"{field}:")
        label.grid(row=row, column=0, sticky="w")

        entry = tk.Entry(frame_right)
        entry.grid(row=row, column=1, sticky="ew")
        entries.append(entry)

    frame_right.grid_columnconfigure(1, weight=1)

    def submit():
        device = {}
        for field, entry in zip(fields, entries):
            value = entry.get().strip()
            if not value:
                tk.Label(frame_right, text=f"Please fill in all fields", fg="red").grid(row=len(fields)+1, column=0, columnspan=2)
                return
            device[field] = value
        
        add_device_data(device)
        clear_frame(frame_right)
        tk.Label(frame_right, text="Device added successfully!", fg="green", font=("Arial", 12, "bold")).pack(pady=20)
        tk.Button(frame_right, text="Add Another", command=create_device, font=("Arial", 10), padx=10, pady=5).pack(pady=5)
        
        # Refresh table if showing devices
        devices = load_devices_data()
        display_table(devices)

    submit_button = tk.Button(frame_right, text="Submit", command=submit)
    submit_button.grid(row=len(fields), column=0, columnspan=2, sticky="ew", pady=5)


# --------------------- DELETE DEVICE ---------------------
def delete_device():
    clear_frame(frame_right)
    clear_frame(table_frame)

    tk.Label(frame_right, text="Enter Device ID:").grid(row=0, column=0, sticky="nsew")
    entry = tk.Entry(frame_right)
    entry.grid(row=0, column=1, sticky="nsew")

    frame_right.grid_columnconfigure(1, weight=1)

    def confirm():
        devices = load_devices_data()
        device_id = entry.get().strip()
        
        if not device_id:
            tk.Label(frame_right, text="Please enter a device ID", fg="red").grid(row=2, column=0, columnspan=2)
            return

        for i, device in enumerate(devices):
            if device.get("device_id") == device_id:
                devices.pop(i)
                save_devices_data(devices)
                clear_frame(frame_right)
                tk.Label(frame_right, text="Device deleted successfully!", fg="green", font=("Arial", 12, "bold")).pack(pady=20)
                
                # Refresh table if showing devices
                updated_devices = load_devices_data()
                if updated_devices:
                    display_table(updated_devices)
                return

        tk.Label(frame_right, text="Device ID not found", fg="red").grid(row=2, column=0, columnspan=2)

    tk.Button(frame_right, text="Delete", command=confirm)\
        .grid(row=1, column=0, columnspan=2, sticky="nsew", pady=5)

# --------------------- SEARCH DEVICE ---------------------
def search_device():
    clear_frame(frame_right)
    clear_frame(table_frame)

    devices = load_devices_data()
    if not devices:
        tk.Label(frame_right, text="No devices found", fg="gray").pack(pady=20)
        return

    # Search input section in right frame
    input_frame = tk.Frame(frame_right)
    input_frame.pack(fill=tk.X, pady=10)
    
    tk.Label(input_frame, text="Search value:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=5)
    search_entry = tk.Entry(input_frame, font=("Arial", 10))
    search_entry.grid(row=0, column=1, sticky="ew", padx=5)
    input_frame.grid_columnconfigure(1, weight=1)

    def search_by_key(key):
        search_value = search_entry.get().strip().lower()
        if not search_value:
            clear_frame(table_frame)
            tk.Label(table_frame, text="Please enter a search value", fg="red", font=("Arial", 10)).pack(pady=20)
            canvas_bottom.update_idletasks()
            canvas_bottom.configure(scrollregion=canvas_bottom.bbox("all"))
            return
        
        matching_devices = []
        for device in devices:
            device_value = str(device.get(key, "")).lower()
            if search_value in device_value:
                matching_devices.append(device)
        
        if not matching_devices:
            clear_frame(table_frame)
            tk.Label(table_frame, text="No matching device found", fg="red", font=("Arial", 10)).pack(pady=20)
            canvas_bottom.update_idletasks()
            canvas_bottom.configure(scrollregion=canvas_bottom.bbox("all"))
            return
        
        # Display results in table format in bottom frame
        tk.Label(frame_right, text=f"Search Results: {len(matching_devices)} device(s) found", 
                font=("Arial", 10, "bold"), fg="green").pack(pady=5)
        display_table(matching_devices)
        
    # Search buttons in right frame
    buttons_frame = tk.Frame(frame_right)
    buttons_frame.pack(fill=tk.X, pady=10)
    
    tk.Label(buttons_frame, text="Search by:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    for key in devices[0].keys():
        btn = tk.Button(buttons_frame, text=f"{key}", command=lambda k=key: search_by_key(k),
                       font=("Arial", 9), relief=tk.RAISED, padx=10, pady=5)
        btn.pack(side=tk.LEFT, padx=2)


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
window.geometry("1000x700")

# Create main container frames
frame_left = tk.Frame(window, bg="#f0f0f0", relief=tk.RAISED, borderwidth=2)
frame_right = tk.Frame(window, bg="#f0f0f0")
frame_bottom = tk.Frame(window, bg="#f0f0f0", relief=tk.SUNKEN, borderwidth=2)

# Pack bottom frame first (so it stays at bottom)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))

# Pack left and right frames in main window (above bottom frame)
frame_left.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 5), pady=5)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(0, 5), pady=5)

# Configure bottom frame for scrollable table
canvas_bottom = tk.Canvas(frame_bottom, bg="white")
scrollbar_bottom = tk.Scrollbar(frame_bottom, orient="vertical", command=canvas_bottom.yview)
table_frame = tk.Frame(canvas_bottom, bg="white")

table_frame.bind(
    "<Configure>",
    lambda e: canvas_bottom.configure(scrollregion=canvas_bottom.bbox("all"))
)

canvas_bottom.create_window((0, 0), window=table_frame, anchor="nw")
canvas_bottom.configure(yscrollcommand=scrollbar_bottom.set)

canvas_bottom.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_bottom.pack(side=tk.RIGHT, fill=tk.Y)

# Define display_table function after table_frame is created
def display_table(devices_list):
    """Display devices in a table format in the bottom frame"""
    clear_frame(table_frame)
    
    if not devices_list:
        tk.Label(table_frame, text="No devices to display", fg="gray", font=("Arial", 10)).pack(pady=20)
        canvas_bottom.update_idletasks()
        canvas_bottom.configure(scrollregion=canvas_bottom.bbox("all"))
        return
    
    # Get all field names
    fields = list(devices_list[0].keys())
    
    # Create header row
    for col, field in enumerate(fields):
        header = tk.Label(table_frame, text=field, font=("Arial", 10, "bold"), 
                         relief=tk.RAISED, borderwidth=2, padx=5, pady=5, bg="#d3d3d3")
        header.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)
    
    # Create data rows
    for row, device in enumerate(devices_list, start=1):
        for col, field in enumerate(fields):
            value = str(device.get(field, ""))
            bg_color = "#f0f0f0" if row % 2 == 0 else "white"
            cell = tk.Label(table_frame, text=value, relief=tk.SUNKEN, 
                           borderwidth=1, padx=5, pady=5, anchor="w", bg=bg_color)
            cell.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
    
    # Configure column weights for proper sizing
    for col in range(len(fields)):
        table_frame.grid_columnconfigure(col, weight=1, minsize=100)
    
    canvas_bottom.update_idletasks()
    canvas_bottom.configure(scrollregion=canvas_bottom.bbox("all"))

main_menu()
window.mainloop()
