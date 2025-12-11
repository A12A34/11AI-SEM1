import tkinter as tk
from matplotlib import table
import numpy as np
import os
import json
import datetime
import pandas as pd
from pathlib import Path
base_dir = Path(os.getcwd())

background_color = "#F0F0F0"
text_color = "#333333"
button_fg_color = "#FFFFFF"
button_bg_color = "#007BFF"
entry_bg_color = "#FFFFFF"
entry_fg_color = "#333333"

current_input_frame_content = None
current_table_frame_content = None


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x400")
    window.configure(bg=background_color)
    input_frame = tk.Frame(window, bg=background_color)
    input_frame.pack(pady=20,side="left")
    table_frame = tk.Frame(window, bg=background_color)
    table_frame.pack(pady=20,side="right")
    window.mainloop()


    class Device:
        def __init__(self,id, device_id, device_name, category_id, category, stock, price, used, date_old):
            self.id = id
            self.device_id = device_id
            self.device_name = device_name
            self.category_id = category_id
            self.category = category
            self.stock = stock
            self.price = price
            self.used = used
            self.date_old = date_old
    class Phone(Device):
        def __init__(self,id, device_id, device_name, category_id, category, stock, price, used, date_old, camera_pixel=0):
            super().__init__(id,device_id, device_name, category_id, category, stock, price, used, date_old)
            self.camera_pixel = camera_pixel

    class Laptop(Device):
        def __init__(self,id, device_id, device_name, category_id, category, stock, price, used, date_old, keyboard_languge=None):
            super().__init__(id,device_id, device_name, category_id, category, stock, price, used, date_old)
            self.keyboard_languge = keyboard_languge