#!/usr/bin/env python3

# File: akfYN.py

import tkinter as tk
from tkinter import messagebox

def yn(title, message):

    def show_yes_no_dialog():
        result = messagebox.askyesno(title, message)
        root.quit()
        root.destroy()
        if result:
            return True
        else:
            return False

    # Create the main application window
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200")
    root.withdraw()    # Hide the main window
    ret = show_yes_no_dialog()
    root.mainloop()
    return ret

def checkYN():
    title = "Exit Application"
    message = """This could be a very long message.
        Several lines long, infact!
        Do you really want to exit?"""

    if yn(title, message) == True:
        print("Returning True")
    else:
        print("Returning False")

if __name__ == "__main__":
    checkYN()

