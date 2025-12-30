#!/usr/bin/env python3

# File: choose_text.py

import tkinter as tk

root_title = "Root Title"
# List of choices
choices = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

returned_choice = "No selection made"

def text_menu(choices=choices, rootTitle=root_title):

    def show_selection(event):
        # Get the index of the selected item
        global returned_choice
        selection_index = listbox.curselection()
        if selection_index:
            # Get the value of the selected item
            selected_item = listbox.get(selection_index[0])
            label.config(text=f"Selected: {selected_item}")
            returned_choice = selected_item
#           print(f"Selected: {selected_item}")
            root.quit()

    # --- Main Application ---
    root = tk.Tk()
    root.title("Listbox Menu Example")

    # Create a Listbox widget
    listbox = tk.Listbox(root, selectmode=tk.SINGLE)
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

if __name__ == "__main__":
    print(f"Returning '{text_menu()}'")

