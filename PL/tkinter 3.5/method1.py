import tkinter
if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry("400x300")
    lfname = tkinter.Label(window, text="First Name")
    lfname.grid(row=0, column=0)
    efname = tkinter.Entry(window)
    efname.grid(row=0, column=1)
    llname = tkinter.Label(window, text="Last Name")
    llname.grid(row=1, column=0)
    elname = tkinter.Entry(window)
    elname.grid(row=1, column=1)
    bsubmit = tkinter.Button(window, text="Submit")
    bsubmit.grid(row=2, column=0, columnspan=2, rowspan=2)

    rows = 3
    columns = 3
    for i in range(rows):
        window.grid_rowconfigure(i, weight=1)
    for i in range(columns):
        window.grid_columnconfigure(i, weight=1)
    window.mainloop()