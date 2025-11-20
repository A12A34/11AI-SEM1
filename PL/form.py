import tkinter
from pathlib import Path
import os
from turtle import clear
path_output = Path("PL\\form.csv")
bg = "gray"
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def display_data():
    if path_output.exists():
        with open(path_output, "r") as f:
            data = f.read()
            print("Current form data:")
            for line in data.splitlines():
                fn, ln, email, pas, pasc, phone = line.split(",")
                print(f"First Name: {fn}, Last Name: {ln}, Email: {email}, Password: {pas}, Confirm Password: {pasc}, Phone Number: {phone}")
    else:
        print("No form data found.")
def clear_data():
    if path_output.exists():
        with open(path_output, "w") as f:
            f.write("")
    else:
        print("No form data to clear.")
if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Form")
    window.geometry("1280x720")
    def save_form():
        with open(path_output, "a") as f:
            f.write(f"{fnentry.get()},{lnentry.get()},{eentry.get()},{pasentry.get()},{pascentr.get()},{pentry.get()}\n")
        print("Form data saved to form.csv")
        print("First Name:", fnentry.get())
        print("Last Name:", lnentry.get())
        print("Email:", eentry.get())
        print("Password:", pasentry.get())
        print("Confirm Password:", pascentr.get())
        print("Phone Number:", pentry.get())
    fnlabel = tkinter.Label(window, text="First Name:",width=50)
    fnlabel.pack()
    fnentry = tkinter.Entry(window, bg=bg, width=50)
    fnentry.pack()
    lnlabel = tkinter.Label(window, text="Last Name:",width=50)
    lnlabel.pack()
    lnentry = tkinter.Entry(window, bg=bg, width=50)
    lnentry.pack()
    elabel = tkinter.Label(window, text="Email:",width=50)
    elabel.pack()
    eentry = tkinter.Entry(window, bg=bg, width=50)
    eentry.pack()
    paslabel = tkinter.Label(window, text="Password:",width=50)
    paslabel.pack()
    pasentry = tkinter.Entry(window, bg=bg, width=50, show="*")
    pasentry.pack()
    pasclabel = tkinter.Label(window, text="Confirm Password:",width=50)
    pasclabel.pack()
    pascentr = tkinter.Entry(window, bg=bg, width=50, show="*")
    pascentr.pack()
    plabel = tkinter.Label(window, text="Phone Number:",width=50)
    plabel.pack()
    pentry = tkinter.Entry(window, bg=bg, width=50)
    pentry.pack()
    sbutton = tkinter.Button(window, text="Submit",bg="green", command=save_form)
    sbutton.pack()
    showbutton = tkinter.Button(window, text="Show Data",bg="green", command=display_data)
    showbutton.pack()
    cldtbutton = tkinter.Button(window, text="Clear Screen",bg="green", command=clear_data)
    cldtbutton.pack()
    tkinter.mainloop()