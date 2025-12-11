from ast import main
import random
import os
import numpy as np
import json
import datetime

def save_data(filename):
    clear_screen()
    view_devices()
    global phones, laptops
    folder = "main/devices_pl/json_files_for_devices"
    file_type = ".json"
    os.makedirs(folder, exist_ok=True)
    full_path = os.path.join(folder, filename + file_type)
    data = {
        "phones": [p.__dict__ for p in phones],
        "laptops": [l.__dict__ for l in laptops]
    }
    with open(full_path, 'w') as f:
        json.dump(data, f, indent=4)
    clear_screen()
    view_devices()
    print(f"Data saved to {full_path} at {datetime.datetime.now()}")
    add_log(f"Data saved to {full_path}")

def load_data(filename):
    clear_screen()
    view_devices()
    if not os.path.exists(filename):
        return [], []
    with open(filename, 'r') as f:
        data = json.load(f)

    def clean_dict(d):
        allowed_keys_phone = {
            "device_id", "device_name", "category_id", "category",
            "stock", "price", "used", "date_old", "camera_pixel"
        }
        allowed_keys_laptop = {
            "device_id", "device_name", "category_id", "category",
            "stock", "price", "used", "date_old", "keyboard_language"
        }
        keys = allowed_keys_phone if "camera_pixel" in d else allowed_keys_laptop
        return {k: v for k, v in d.items() if k in keys}


    phones = [Phone(**clean_dict(p)) for p in data.get("phones", [])]
    laptops = [Laptop(**clean_dict(l)) for l in data.get("laptops", [])]

    clear_screen()
    print(f"Data loaded from {filename} at {datetime.datetime.now()}")
    add_log(f"Data loaded from {filename}")
    return phones, laptops

def display_json():
    clear_screen()
    full_path = input_nonempty("Enter full path to JSON file: ")
    if not os.path.exists(full_path):
        print(f"No file found at {full_path}.")
        return
    with open(full_path, 'r') as f:
        data = json.load(f)
    print(json.dumps(data, indent=4))
    input("Press Enter to continue...")



def input_nonempty(prompt, maxlen=None, err_msg=None):
    while True:
        s = input(prompt).strip()
        if not s:
            print(err_msg or "This field cannot be empty.")
            continue
        if maxlen is not None and len(s) > maxlen:
            print(err_msg or f"Value is too long (max {maxlen or '-inf'}).")
            continue
        return s


def input_int(prompt, min_value=None, max_value=None, err_msg=None):
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if (min_value is not None and n < min_value) or (max_value is not None and n > max_value):
                print(err_msg or f"Please enter a whole number in range [{min_value or '-inf'}, {max_value or 'inf'}].")
                continue
            return n
        except ValueError:
            print(err_msg or "Please enter a valid whole number.")


def input_float(prompt, min_value=None, max_value=None, err_msg=None):
    while True:
        s = input(prompt).strip()
        try:
            x = float(s)
            if (min_value is not None and x < min_value) or (max_value is not None and x > max_value):
                print(err_msg or f"Please enter a number in range [{min_value or '-inf'}, {max_value or 'inf'}].")
                continue
            return x
        except ValueError:
            print(err_msg or "Please enter a valid number.")


def input_yes_no(prompt, err_msg=None):
    while True:
        s = input(prompt + " [Y/N]: ").strip().upper()
        if not s and err_msg is not None:
            return err_msg
        if s in ("Y", "YES"):
            return True
        if s in ("N", "NO"):
            return False
        print("Please enter Y or N.")


class Device:
    def __init__(self, device_id, device_name, category_id, category, stock, price, used, date_old):
        self.device_id = device_id
        self.device_name = device_name
        self.category_id = category_id
        self.category = category
        self.stock = stock
        if self.stock < 0: raise ValueError("stock must be >= 0")
        self.price = price
        if self.price < 0: raise ValueError("price must be >= 0")
        self.used = bool(used)
        self.date_old = date_old
        if self.date_old < 0: raise ValueError("date_old must be >= 0")
        self.final_price = 0.0
        self.calc_price()

    def calc_price(self): self.final_price = float(self.price)

    def items_row(self):
        return [
            self.device_id,
            self.device_name,
            str(self.category_id),
            self.category,
            str(self.stock),
            f"{self.price:.2f}",
            "Yes" if self.used else "No",
            f"{self.date_old} days",
        ]


class Phone(Device):
    def __init__(self, device_id, device_name, category_id, category, stock, price, used, date_old, camera_pixel=0):
        super().__init__(device_id, device_name, category_id, category, stock, price, used, date_old)
        self.camera_pixel = int(camera_pixel)
        if self.camera_pixel < 0:
            raise ValueError("camera_pixel must be >= 0")
        self.calc_price()

    def calc_price(self):
        if self.used:
            depreciation_pct = (self.date_old / 5) / 100
            self.final_price = max(0.0, self.price * (1 - depreciation_pct))
        else: self.final_price = float(self.price)  # Inline assignment for single statement

    def items_row(self):
        base = super().items_row()
        base += [f"{self.camera_pixel} MP", f"{self.final_price:.2f}"]
        return base


class Laptop(Device):
    def __init__(self, device_id, device_name, category_id, category, stock, price, used, date_old, keyboard_language=""):
        super().__init__(device_id, device_name, category_id, category, stock, price, used, date_old)
        self.keyboard_language = keyboard_language
        self.calc_price()

    def calc_price(self):
        if self.used:
            depreciation_pct = (self.date_old / 10) / 100
            self.final_price = max(0.0, self.price * (1 - depreciation_pct))
        else: self.final_price = float(self.price)

    def items_row(self):
        base = super().items_row()
        base += [self.keyboard_language, f"{self.final_price:.2f}"]
        return base


phones = [
    Phone("AA52554", "iPhone 11", 1, "Phone", 45, 200, True, 150, 48),
    Phone("AA53565", "iPhone 12", 1, "Phone", 65, 200, True, 120, 36),
    Phone("AA54576", "iPhone 13", 1, "Phone", 25, 200, False, 30, 64),
    Phone("AA55587", "iPhone 14", 1, "Phone", 15, 200, False, 10, 108),
    Phone("AA56598", "iPhone 15", 1, "Phone", 5, 200, False, 5, 200),
    Phone("AA57599", "Samsung S22", 1, "Phone", 40, 180, True, 60, 50),
    Phone("AA58600", "Samsung S23", 1, "Phone", 20, 250, False, 15, 200),
    Phone("AA59601", "Google Pixel 7", 1, "Phone", 30, 220, True, 40, 64),
    Phone("AA60602", "OnePlus 11", 1, "Phone", 18, 210, False, 12, 108),
    Phone("AA61603", "Xiaomi 13 Pro", 1, "Phone", 10, 190, False, 8, 200),
]

laptops = [
    Laptop("AA80252", "Dell Pro 10", 2, "Laptop", 36, 150, False, 0, "En"),
    Laptop("AA20053", "Dell Pro 12", 2, "Laptop", 83, 150, True, 40, "En"),
    Laptop("AA30054", "Dell Pro 14", 2, "Laptop", 12, 150, True, 90, "En"),
    Laptop("AA40055", "Dell Pro 16", 2, "Laptop", 23, 150, True, 120, "En"),
    Laptop("AA50056", "Dell Pro 18", 2, "Laptop", 8, 150, False, 20, "En"),
    Laptop("AA60057", "HP EliteBook 840", 2, "Laptop", 40, 200, True, 60, "En"),
    Laptop("AA70058", "HP Spectre x360", 2, "Laptop", 25, 250, False, 10, "En"),
    Laptop("AA80059", "Lenovo ThinkPad X1", 2, "Laptop", 15, 220, True, 45, "En"),
    Laptop("AA90060", "Asus ZenBook Pro", 2, "Laptop", 10, 230, False, 5, "En"),
    Laptop("AA10061", "Apple MacBook Air M2", 2, "Laptop", 7, 350, False, 3, "En"),
]


def generate_device_id(used_ids):
    while True:
        new_id = "AA" + str(random.randint(10000, 99999))
        if new_id not in used_ids:
            add_log(f"Generated new device ID: {new_id}")
            return new_id


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_table(rows, header):
    rows_list = [list(map(str, r)) for r in rows]
    widths = [len(str(h)) for h in header]
    for r in rows_list:
        if len(r) > len(widths):
            widths.extend([0] * (len(r) - len(widths)))
        for idx, cell in enumerate(r):
            widths[idx] = max(widths[idx], len(cell))
    fmt = "  ".join([f"{{:<{w}}}" for w in widths])
    print(fmt.format(*header))
    print("-" * (sum(widths) + 2 * max(0, len(widths) - 1)))
    for r in rows_list:
        if len(r) < len(widths):
            r = list(r) + [""] * (len(widths) - len(r))
        print(fmt.format(*r))


def view_devices():
    clear_screen()
    phone_header = ["Device ID", "Name", "CatID", "Category", "Stock", "Price", "Used", "Age", "Camera (MP)", "Final Price"]
    laptop_header = ["Device ID", "Name", "CatID", "Category", "Stock", "Price", "Used", "Age", "Keyboard", "Final Price"]
    print("--- Phones ---")
    for p in phones:
        p.calc_price()
    phone_rows = [p.items_row() for p in phones]
    format_table(phone_rows, phone_header)
    print("--- Laptops ---")
    for l in laptops:
        l.calc_price()
    laptop_rows = [l.items_row() for l in laptops]
    format_table(laptop_rows, laptop_header)
    print("\n")


def add_device():
    all_ids = {p.device_id for p in phones} | {l.device_id for l in laptops}
    print("1. Phone")
    print("2. Laptop")
    choice = input_nonempty("Enter choice (1/2): ", maxlen=1)
    if choice == "1":
        device_id = generate_device_id(all_ids)
        device_name = input_nonempty("Enter Device Name: ", maxlen=100)
        category_id = 1
        category = "Phone"
        stock = input_int("Enter Stock (integer >=0): ", min_value=0)
        price = input_float("Enter Price: ", min_value=0.0)
        used = input_yes_no("Is it used?")
        date_old = input_int("Enter how many days old: ", min_value=0)
        camera_pixel = input_int("Enter Camera Pixel (MP): ", min_value=0)
        p1 = Phone(device_id, device_name, category_id, category, stock, price, used, date_old, camera_pixel)
        phones.append(p1)
        print(f"Phone added with ID {device_id} at {datetime.datetime.now()}.")
        add_log(f"Added new phone with ID {device_id}")
    elif choice == "2":
        device_id = generate_device_id(all_ids)
        device_name = input_nonempty("Enter Device Name: ", maxlen=100)
        category_id = 2
        category = "Laptop"
        stock = input_int("Enter Stock (integer >=0): ", min_value=0)
        price = input_float("Enter Price: ", min_value=0.0)
        used = input_yes_no("Is it used?")
        date_old = input_int("Enter how many days old: ", min_value=0)
        keyboard_language = input_nonempty("Enter Keyboard Language: ", maxlen=10)
        l1 = Laptop(device_id, device_name, category_id, category, stock, price, used, date_old, keyboard_language)
        laptops.append(l1)
        print(f"Laptop added with ID {device_id} at {datetime.datetime.now()}.")
        add_log(f"Added new laptop with ID {device_id}")
    else:
        print("Invalid choice.")



def find_device_by_id(dev_id):
    for d in phones + laptops:
        if d.device_id == dev_id:
            return d
    return None


def buy_device():
    clear_screen()
    view_devices()
    dev_id = input_nonempty("Enter Device ID to buy: ")
    qty = input_int("Enter quantity to buy: ", min_value=1)
    d = find_device_by_id(dev_id)
    if not d:
        print("Device not found.")
        return
    if d.stock >= qty:
        d.stock -= qty
        d.calc_price()
        print(f"Purchased {qty} of {d.device_name} at {d.final_price:.2f} each. Remaining stock: {d.stock} at {datetime.datetime.now()}.")
        add_log(f"Purchased {qty} of {d.device_name} (ID: {dev_id}) at {d.final_price:.2f} each. Remaining stock: {d.stock}")
    else:
        print("Not enough stock.")


def search_device():
    term = input_nonempty("Enter Device ID or Name to search: ")
    term_lower = term.lower()
    found = False
    for d in phones + laptops:
        if d.device_id.lower() == term_lower or d.device_name.lower() == term_lower:
            print("Found device:")
            d.calc_price()
            print(d.items_row())
            found = True
    if not found:
        print("No device found.")


def delete_device():
    clear_screen()
    view_devices()
    dev_id = input_nonempty("Enter Device ID to delete: ")
    for collection in (phones, laptops):
        for idx, d in enumerate(collection):
            if d.device_id == dev_id:
                del collection[idx]
                print(f"Device {dev_id} removed at {datetime.datetime.now()}.")
                add_log(f"Deleted device with ID {dev_id}")
                return
    print("Device not found.")


def min_price():
    all_devices = phones + laptops
    if all_devices:
        for d in all_devices:
            d.calc_price()
        cheapest = min(all_devices, key=lambda x: x.final_price)
        print(f"Cheapest: {cheapest.device_name} (ID: {cheapest.device_id}) at {cheapest.final_price:.2f}")
    else:
        print("No devices.")


def max_price():
    all_devices = phones + laptops
    if all_devices:
        for d in all_devices:
            d.calc_price()
        most_expensive = max(all_devices, key=lambda x: x.final_price)
        print(f"Most Expensive: {most_expensive.device_name} (ID: {most_expensive.device_id}) at {most_expensive.final_price:.2f}")
    else:
        print("No devices.")


def filter_devices():
    print("1. Phone")
    print("2. Laptop")
    i2 = input_nonempty("Enter choice (1/2): ", maxlen=1)
    if i2 == "1":
        header = ["Device ID", "Name", "CatID", "Category", "Stock", "Price", "Used", "Age", "Camera (MP)", "Final Price"]
        print("Filter by:")
        print("1. name")
        print("2. price (<=)")
        print("3. stock (>=)")
        print("4. used (Y/N)")
        print("5. age (<= days)")
        print("6. camera_pixel (>= MP)")
        i3 = input_nonempty("Enter choice (1-6): ", maxlen=1)
        rows = []
        if i3 == "1":
            name = input_nonempty("Enter name to filter: ").lower()
            rows = [p.items_row() for p in phones if p.device_name.lower() == name]
        elif i3 == "2":
            price = input_float("Enter maximum price: ", min_value=0.0)
            rows = [p.items_row() for p in phones if p.final_price <= price]
        elif i3 == "3":
            stock = input_int("Enter minimum stock: ", min_value=0)
            rows = [p.items_row() for p in phones if p.stock >= stock]
        elif i3 == "4":
            used = input_yes_no("Filter used? (Y for used, N for new): ")
            rows = [p.items_row() for p in phones if p.used == used]
        elif i3 == "5":
            days = input_int("Enter maximum age in days: ", min_value=0)
            rows = [p.items_row() for p in phones if p.date_old <= days]
        elif i3 == "6":
            mp = input_int("Enter minimum camera pixel: ", min_value=0)
            rows = [p.items_row() for p in phones if p.camera_pixel >= mp]
        else:
            print("Invalid choice.")
            return
        format_table(rows, header)
    elif i2 == "2":
        header = ["Device ID", "Name", "CatID", "Category", "Stock", "Price", "Used", "Age", "Keyboard", "Final Price"]
        print("Filter by:")
        print("1. name")
        print("2. price (<=)")
        print("3. stock (>=)")
        print("4. used (Y/N)")
        print("5. age (<= days)")
        print("6. keyboard_language")
        i3 = input_nonempty("Enter choice (1-6): ", maxlen=1)
        rows = []
        if i3 == "1":
            name = input_nonempty("Enter name to filter: ").lower()
            rows = [l.items_row() for l in laptops if l.device_name.lower() == name]
        elif i3 == "2":
            price = input_float("Enter maximum price: ", min_value=0.0)
            rows = [l.items_row() for l in laptops if l.final_price <= price]
        elif i3 == "3":
            stock = input_int("Enter minimum stock: ", min_value=0)
            rows = [l.items_row() for l in laptops if l.stock >= stock]
        elif i3 == "4":
            used = input_yes_no("Filter used? (Y for used, N for new): ")
            rows = [l.items_row() for l in laptops if l.used == used]
        elif i3 == "5":
            days = input_int("Enter maximum age in days: ", min_value=0)
            rows = [l.items_row() for l in laptops if l.date_old <= days]
        elif i3 == "6":
            lang = input_nonempty("Enter keyboard language to filter: ").lower()
            rows = [l.items_row() for l in laptops if l.keyboard_language.lower() == lang]
        else:
            print("Invalid choice.")
            return
        format_table(rows, header)
    else:
        print("Invalid choice.")


def edit_device():
    clear_screen()
    view_devices()
    dev_id = input_nonempty("Enter Device ID to edit: ")
    d = find_device_by_id(dev_id)
    if not d:
        print("Device not found.")
        return
    print("Editing device. Press enter to keep current value.")
    new_name = input(f"Current Name ({d.device_name}): ") or d.device_name
    try:
        new_stock = input(f"Current Stock ({d.stock}): ")
        new_stock = int(new_stock) if new_stock else d.stock
        new_price = input(f"Current Price ({d.price}): ")
        new_price = float(new_price) if new_price else d.price
        new_used_raw = input(f"Is it used (Y/N) ({'Y' if d.used else 'N'}): ").strip().upper()
        new_used = d.used if new_used_raw == "" else (new_used_raw == "Y")
        new_date_old = input(f"Current Age in days ({d.date_old}): ")
        new_date_old = int(new_date_old) if new_date_old else d.date_old
    except ValueError:
        print("Invalid input. Aborting edit.")
        return
    d.device_name = new_name
    d.stock = new_stock
    d.price = new_price
    d.used = new_used
    d.date_old = new_date_old
    if isinstance(d, Phone):
        try:
            new_camera_pixel = input(f"Current Camera Pixel ({d.camera_pixel}): ")
            d.camera_pixel = int(new_camera_pixel) if new_camera_pixel else d.camera_pixel
        except ValueError:
            print("Invalid camera pixel. Keeping old value.")
    elif isinstance(d, Laptop):
        new_keyboard_language = input(f"Current Keyboard Language ({d.keyboard_language}): ") or d.keyboard_language
        d.keyboard_language = new_keyboard_language
    d.calc_price()
    print(f"Device updated at {datetime.datetime.now()}.")
    add_log(f"Updated device with ID {dev_id}")

def points_devices(inid):
    average_price = np.average([d.final_price for d in phones + laptops])
    average_camera = np.average([p.camera_pixel for p in phones])
    average_age = np.average([d.date_old for d in phones + laptops])
    d = find_device_by_id(inid)
    if not d:
        print("Device not found.")
        return
    price_point = d.final_price / average_price
    camera_point = d.camera_pixel / average_camera if d.category == "Phone" else 0
    total_points = price_point + camera_point
    print(f"Points for Device ID {inid}:")
    print(f"Price Point: {price_point:.2f}")
    print(f"Camera Point: {camera_point:.2f}")
    print(f"Total Points: {total_points:.2f}")



def show_analytics():
    clear_screen()
    view_devices()
    print("\n")
    inid = input_nonempty("Enter Device ID to show analytics: ")
    d = find_device_by_id(inid)
    if not d:
        print("Device not found.")
        return
    print(f"Analytics for Device ID {inid}:")
    print(f"Name: {d.device_name}")
    print(f"Category: {d.category}")
    print(f"Stock: {d.stock}")
    print(f"Price: {d.price:.2f}")
    print(f"Used: {'Yes' if d.used else 'No'}")
    print(f"Age: {d.date_old} days")
    points_devices(inid)

def show_stats():
    clear_screen()
    view_devices()
    all_devices = phones + laptops
    if not all_devices:
        print("No devices available.")
        return
    prices = [d.final_price for d in all_devices]
    stocks = [d.stock for d in all_devices]
    ages = [d.date_old for d in all_devices]
    print("Device Statistics:")
    print(f"Average Price: {np.mean(prices):.2f}")
    print(f"Median Price: {np.median(prices):.2f}")
    print(f"Price Range: {np.ptp(prices):.2f}")
    print(f"Price Std Dev: {np.std(prices):.2f}")
    print(f"Average Stock: {np.mean(stocks):.2f}")
    print(f"Median Stock: {np.median(stocks):.2f}")
    print(f"Stock Range: {np.ptp(stocks):.2f}")
    print(f"Stock Std Dev: {np.std(stocks):.2f}")
    print(f"Average Age (days): {np.mean(ages):.2f}")
    print(f"Median Age (days): {np.median(ages):.2f}")
    print(f"Age Range (days): {np.ptp(ages):.2f}")
    print(f"Age Std Dev (days): {np.std(ages):.2f}")

def show_logs():

    folder = "main/devices_pl/logs_files_for_devices"
    os.makedirs(folder, exist_ok=True)
    default_log = os.path.join(folder, "device_logs.txt")

    # Ask user which file to open
    use_default = input_yes_no("Use default log file?")  # existing helper in your code

    if use_default:
        log_file = default_log
        if not os.path.exists(log_file):
            # create default file with header
            with open(log_file, "w") as f:
                f.write(f"Log created at {datetime.datetime.now()}\n")
    else:
        name = input_nonempty("Enter new log file name (without extension): ", maxlen=100)
        log_file = os.path.join(folder, name + ".txt")
        if not os.path.exists(log_file):
            with open(log_file, "w") as f:
                f.write(f"Log created at {datetime.datetime.now()}\n")

    # Read and print logs safely
    try:
        with open(log_file, "r") as f:
            logs = f.readlines()
    except FileNotFoundError:
        print(f"No log file found at {log_file}.")
        return

    print(f"Device Logs ({os.path.basename(log_file)}):")
    if not logs:
        print("[empty]")
    else:
        for line in logs:
            print(line.rstrip())

def add_log(message):
    folder = "main/devices_pl/logs_files_for_devices"
    os.makedirs(folder, exist_ok=True)
    log_file = os.path.join(folder, "device_logs.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def clear_logs():
    folder = "main/devices_pl/logs_files_for_devices"
    os.makedirs(folder, exist_ok=True)
    log_file = os.path.join(folder, "device_logs.txt")
    with open(log_file, "w") as f:
        f.write(f"Log cleared at {datetime.datetime.now()}\n")
    print("Logs cleared.")

def manage_data_menu():
    print("1. Save data")
    print("2. Load data")
    print("3. show logs")
    print("4. Clear logs")
    print("5. display JSON file")
    choice = input_nonempty("Enter choice (1-5): ", maxlen=1)
    if choice == "1":
        save_data(input_nonempty("Enter filename to save data: "))
    elif choice == "2":
        load_data(input_nonempty("Enter file path to load data: "))
    elif choice == "3":
        show_logs()
    elif choice == "4":
        clear_logs()
    elif choice == "5":
        display_json()
    else:
        main_menu()


def main_menu():
    while True:
        clear_screen()  # clear screen every loop for cleaner view
        print("\n=== Device Management Menu ===")
        print("1. View all devices")
        print("2. Add device")
        print("3. Buy device")
        print("4. Search device")
        print("5. Delete device")
        print("6. Show cheapest device")
        print("7. Show most expensive device")
        print("8. Filter devices")
        print("9. Edit device")
        print("10. Show device analytics")
        print("11. Show statistics")
        print("12. Clear screen")
        print("13. Manage data (Save/Load/Download/Logs)")
        print("15. Exit")
        choice = input_nonempty("Enter your choice: ", maxlen=2)
        if choice == "1":
            view_devices()
        elif choice == "2":
            add_device()
        elif choice == "3":
            buy_device()
        elif choice == "4":
            search_device()
        elif choice == "5":
            delete_device()
        elif choice == "6":
            min_price()
        elif choice == "7":
            max_price()
        elif choice == "8":
            filter_devices()
        elif choice == "9":
            edit_device()
        elif choice == "10":
            show_analytics()
        elif choice == "11":
            show_stats()
        elif choice == "12":
            clear_screen()
        elif choice == "13":
            manage_data_menu()  # added data management option
        elif choice == "15":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    clear_screen()
    main_menu()