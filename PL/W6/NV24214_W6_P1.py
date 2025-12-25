#11AI Ali Alhasan Nv24214 W6 P1

import tkinter as tk
from turtle import pen
if __name__ == "__main__":
    def calculate_total_price():
        price = int(pentry.get())
        number_of_items = int(nentry.get())
        total_price = price * number_of_items
        tentry.delete(0, tk.END)
        tentry.insert(0, str(total_price))
    window = tk.Tk()
    window.title("Ali Alhasan, Tkinter Program 3")
    window.geometry("1280x720")
    NV24214_frame = tk.Frame(window)
    plabel = tk.Label(NV24214_frame, text="Enter price:")
    pentry = tk.Entry(NV24214_frame)
    nlabel = tk.Label(NV24214_frame, text="Enter amount of items:")
    nentry = tk.Entry(NV24214_frame)
    tlabel = tk.Label(NV24214_frame, text="Total Price:")
    tentry = tk.Entry(NV24214_frame)
    cbutton = tk.Button(NV24214_frame, text="Calculate Total Price", command=calculate_total_price)

    NV24214_frame.grid(row=0, column=0, sticky="nsew")
    plabel.grid(row=0, column=0, sticky="nsew")
    pentry.grid(row=0, column=1, sticky="nsew")
    nlabel.grid(row=1, column=0, sticky="nsew")
    nentry.grid(row=1, column=1, sticky="nsew")
    tlabel.grid(row=2, column=0, sticky="nsew")
    tentry.grid(row=2, column=1, sticky="nsew")
    cbutton.grid(row=3, column=0, columnspan=2, sticky="nsew")

    window.mainloop()
    print("This is Ali's third Tkinter window")

#11AI Ali Alhasan Nv24214 W6 P1