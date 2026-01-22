#!/usr/bin/env python3

# File: choose_text.py

import tkinter as tk

returned_choice = None

def text_menu(choices, rootTitle):
    """
    Relies on presence of the global "returned_choice".
    Returns None if window is closed using the (top right) [X]
    """
    def show_selection(event):
        # Get the index of the selected item
        global returned_choice
        selection_index = listbox.curselection()
        if selection_index:
            # Get the value of the selected item
            returned_choice = listbox.get(selection_index[0])
            label.config(text=f"Selected: {returned_choice}")
        else:
            returned_choice = None
#           print(f"Selected: {returned_choice}")
        root.quit()

    # --- Main Application ---
    root = tk.Tk()
    root.title("Listbox Menu Example")

    # Create a Listbox widget
    listbox = tk.Listbox(root,
                         selectmode=tk.SINGLE,
                         width=0)
    listbox.pack(padx=10, pady=10)

    # Populate the Listbox with choices
    for item in choices:
        listbox.insert(tk.END, item)

    # Bind the selection event to a function
    listbox.bind('<<ListboxSelect>>', show_selection)

    # Label to display the selected item
    label = tk.Label(root, text="Select an item")
    label.pack(pady=10)

    root.mainloop()

    return returned_choice

def ck_text_menu():
    root_title = "Root Title"
    # List of choices
    choices = ["AppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleApple",
               "BananaBananaBananaBananaBananaBananaBananaBanana",
               "CherryCherryCherryCherryCherryCherryCherryCherryCherryCherryCherryCherryCherry",
               "DateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDate",
               "ElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberry"]
    ret = text_menu(choices, root_title)
    print("Returning....")
    print(repr(ret))

if __name__ == "__main__":
    ck_text_menu()

