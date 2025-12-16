#!/usr/bin/env python3

# File: akYN.py

import tkinter as tk
from tkinter import messagebox

def show_yes_no_dialog():
    # The askyesno function returns True for 'Yes' and False for 'No'
#   result = messagebox.askyesno("Question Title", "Do you want to proceed?")
    result = messagebox.askyesno("Exit Application",
        """This could be a very long message.
Several lines long, infact!
Do you really want to exit?""")

    if result:
        print("User clicked Yes (True)")
        # Add your 'Yes' logic here
    else:
        print("User clicked No (False)")
        # Add your 'No' logic here

    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

# Hide the main window if you only want the dialog box to appear immediately
# root.withdraw()

# Button to trigger the dialog box
#button = tk.Button(root, text="Click to show Yes/No Dialog", command=show_yes_no_dialog)
#button.pack(pady=50)
show_yes_no_dialog()
#result = messagebox.askyesno("Question Title", "Do you want to proceed?")
#if result:
#    print("User clicked Yes (True)")
#    # Add your 'Yes' logic here
#else:
#    print("User clicked No (False)")
#    # Add your 'No' logic here
root.quit()

# Start the Tkinter event loop
root.mainloop()

