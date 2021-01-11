#Import helper methods
import tkinter_helper_methods as thm
#Import tkinter
import tkinter as tk
import os

#Create the debug window
window = tk.Tk()

#Create a Label, and pack the label into the window
debug_greeting = tk.Label(
    text="Debug Station + Unit Test Module",
    width=30,
    height=2)
debug_greeting.pack()

#Listbox to list out all unit-tests in the directory the debugger is placed in
filenames = thm.testFileNames()
lbVar = tk.StringVar(value=filenames)
lbObject= tk.Listbox(
    listvariable=lbVar,
    height=5)

# Colorize alternating lines of the listbox
for i in range(0,len(filenames),2):
    lbObject.itemconfigure(i, background='#f0f0ff')
lbObject.pack()



#Create button to run tests (Currently Placeholder)
button = tk.Button(
    text="Run Debug",
    width = 10,
    height=2)
button.pack()

#Create a frame inside to simulate a console
textf = tk.Text(window, height=100, width=500)
textf.insert(tk.END, "Hello....." + '\n')
textf.insert(tk.END, "Bye Bye....." + '\n')
textf.pack(fill="both", expand="YES")



#mainloop tells python to run Tkinter event loop, checking for code
window.mainloop()


