# 11AI Ali Alhasan
from pathlib import Path
import tkinter
path_output = Path("PL/W5/NV24214_W5_P2_output.txt")
if __name__ == "__main__":
    window = tkinter.Tk()
    print("This is Ali Alhasan's second Tkinter window!")
    window.title("Ali Alhasan, Tkinter Program 2")
    window.geometry("720x480")
    NV24214_frame = window  # Renamed frame variable
    label_name = tkinter.Label(NV24214_frame, text="Name", fg="red", bg="lightblue", width=50)
    label_name.pack()
    textentry = tkinter.Entry(NV24214_frame, bg="yellow", width=50)
    textentry.insert(0, "enter your name")
    textentry.pack()
    def submit_name():
        name_entered = textentry.get()
        message = f"Hello {name_entered}, welcome to Ali Alhasan's second Tkinter Program!"
        print(message)
        with open(path_output, "w") as f:
            f.write(name_entered + "\n")
    button = tkinter.Button(NV24214_frame, text="Submit Name", bg="green", fg="white", command=submit_name)
    button.pack()
    print(str(button))
    print(str(label_name))
    label_creator = tkinter.Label(NV24214_frame, text="Created by: Ali Alhasan", fg="blue")
    label_creator.pack(side="bottom")
    window.mainloop()
    print("Text entry content written to NV24214_W5_P2_output.txt")
    print("End of program.")
# 11AI Ali Alhasan