#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, font
from pathlib import Path
import os
import csv

# Store CSV next to this script (cross-platform)
path_output = Path(__file__).parent / "form.csv"
bg = "gray"

def ensure_header():
    if not path_output.exists():
        path_output.parent.mkdir(parents=True, exist_ok=True)
        with open(path_output, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["first_name", "last_name", "email", "password", "phone_number"])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_data():
    if path_output.exists():
        with open(path_output, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["first_name", "last_name", "email", "password", "phone_number"])
        messagebox.showinfo("Cleared", "Form data cleared.")
    else:
        messagebox.showinfo("No Data", "No form data to clear.")


if __name__ == "__main__":
    clear_screen()
    ensure_header()

    window = tk.Tk()
    window.title("Form")
    window.geometry("640x480")
    lbl_width = 20
    entry_width = 40

    # Improve default font size
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=10)

    def save_form():
        fn = fnentry.get().strip()
        ln = lnentry.get().strip()
        email = eentry.get().strip()
        pas = pasentry.get()
        pasc = pascentr.get()
        phone = pentry.get().strip()

        if not fn or not ln or not email or not pas:
            messagebox.showerror("Missing", "Please fill in all required fields.")
            return
        if pas != pasc:
            messagebox.showerror("Password", "Passwords do not match.")
            return

        ensure_header()
        with open(path_output, "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([fn, ln, email, pas, phone])

        messagebox.showinfo("Saved", "Form data saved to form.csv")

    def display_data():
        if not path_output.exists():
            messagebox.showinfo("No Data", "No form data found.")
            return

        # Show data in a separate window using a monospace Text widget for aligned columns
        win = tk.Toplevel(window)
        win.title("Stored Form Data")
        txt = tk.Text(win, wrap='none', font=("Courier", 10))
        txt.pack(fill='both', expand=True)

        with open(path_output, "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            rows = list(reader)

        cols = ["first name", "last name", "email", "password", "phone number"]
        col_width = [25, 25, 30, 10, 15]
        # header
        sep = "+" + "+".join(["-" * w for w in col_width]) + "+\n"
        header_line = "|" + "|".join([c.ljust(w) for c, w in zip(cols, col_width)]) + "|\n"
        txt.insert("end", sep)
        txt.insert("end", header_line)
        txt.insert("end", sep)
        for row in rows:
            if len(row) < 5:
                continue
            fn, ln, email, pas, phone = row
            masked = "*" * len(pas)
            line = "|" + "|".join([
                fn.ljust(col_width[0]),
                ln.ljust(col_width[1]),
                email.ljust(col_width[2]),
                masked.ljust(col_width[3]),
                phone.ljust(col_width[4])
            ]) + "|\n"
            txt.insert("end", line)
        txt.insert("end", sep)
        txt.config(state='disabled')

    # Build form UI with consistent spacing
    fnlabel = tk.Label(window, text="First Name:", width=lbl_width, anchor='w')
    fnlabel.pack()
    fnentry = tk.Entry(window, bg=bg, width=entry_width)
    fnentry.pack()

    lnlabel = tk.Label(window, text="Last Name:", width=lbl_width, anchor='w')
    lnlabel.pack()
    lnentry = tk.Entry(window, bg=bg, width=entry_width)
    lnentry.pack()

    elabel = tk.Label(window, text="Email:", width=lbl_width, anchor='w')
    elabel.pack()
    eentry = tk.Entry(window, bg=bg, width=entry_width)
    eentry.pack()

    paslabel = tk.Label(window, text="Password:", width=lbl_width, anchor='w')
    paslabel.pack()
    pasentry = tk.Entry(window, bg=bg, width=entry_width, show="*")
    pasentry.pack()

    pasclabel = tk.Label(window, text="Confirm Password:", width=lbl_width, anchor='w')
    pasclabel.pack()
    pascentr = tk.Entry(window, bg=bg, width=entry_width, show="*")
    pascentr.pack()

    plabel = tk.Label(window, text="Phone Number:", width=lbl_width, anchor='w')
    plabel.pack()
    pentry = tk.Entry(window, bg=bg, width=entry_width)
    pentry.pack()
    sbutton = tk.Button(window, text="Submit", bg="green", command=save_form, width=12)
    sbutton.pack()
    showbutton = tk.Button(window, text="Show Data", bg="green", command=display_data, width=12)
    showbutton.pack()
    cldtbutton = tk.Button(window, text="Clear data", bg="green", command=clear_data, width=12)
    cldtbutton.pack()

    tk.mainloop()
