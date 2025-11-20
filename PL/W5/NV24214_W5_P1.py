#11AI Ali Alhasan NV24214 W5 P1
import tkinter
def greet():
    print("Hello, Ali Alhasan's")
if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Ali Alhasan first GUI")
    window.geometry("1280x720")
    label = tkinter.Label(window, text="Hello, World!")
    label.pack()
    button = tkinter.Button(window, text="Click Me", command=greet)
    button.pack()
    label2 = tkinter.Label(window, text="Created by:Ali Alhasan's.")
    label2.pack()
    window.mainloop()
    print("This is Ali Alhasan's first GUI program.")

    
#11AI Ali Alhasan NV24214 W5 P1