from pathlib import Path
import tkinter
path_output = Path("PL\\W5\\NV24214_W5_P2_output.txt")
if __name__ == "__main__":
    window = tkinter.Tk()
    def printheloow():
        print("text entry is:", textentry.get())
    def write_to_file():
        with open(path_output, "w") as f:
            f.write(textentry.get() + "\n")
    window.title("Ali Alhasan second GUI")
    window.geometry("1280x720")
    label = tkinter.Label(window, text="Hello, World!", fg="blue",width=50)
    label.pack()
    textentry = tkinter.Entry(window, bg="yellow", width=50)
    textentry.pack()
    button = tkinter.Button(window, text="Click Me",bg="green", command=write_to_file)
    button.pack()
    print(str(button))
    print(str(label))
    label2 = tkinter.Label(window, text="Created by: Ali Alhasan's.")
    label2.pack()
    window.mainloop()
    print("This is Ali Alhasan's second GUI program.")
    print("Text entry content written to NV24214_W5_P2_output.txt")
    print("End of program.")