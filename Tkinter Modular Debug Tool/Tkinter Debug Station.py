#Import tkinter
import tkinter as tk

#Create the debug window
window = tk.Tk()

#Create a Label, and pack the label into the window
debug_greeting = tk.Label(
    text="Debug Station + Unit Test Module",
    width=30,
    height=2)
debug_greeting.pack()

#Create button to run tests (Currently Placeholder)
button = tk.Button(
    text="Run Debug",
    width = 10,
    height=2)
button.pack()


#mainloop tells python to run Tkinter event loop, checking for code
window.mainloop()