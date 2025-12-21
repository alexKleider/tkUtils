#!/usr/bin/env python3

# File: collector.py

import tkinter as tk

"""
Provides a way of setting up a mapping for modification or entry of
values.  These are collected into what must be a global value:
    <global_res>
"""

global_res = {}  # collects info from the gui window

def updated_mapping(entries, root_title="Record Update"):
    """
    <entries> is a mapping, the values of which can be updated
    in a window labeled <root_title> and retrieved.
    Retrieval depends on <global_res> which must exist globally.
    """
    def submit_data():
        res = {}
        for key in entries.keys():
            res[key] = str_vars[key].get()
        global global_res
        global_res = res
        root.destroy()

    root = tk.Tk()
    root.title(root_title)

    keys = entries.keys()
    labels = {}
    str_vars = {}
    values = {}

    row = 0;

    for key, value in entries.items():
        labels[key] = tk.Label(root, text=key)
        labels[key].grid(row=row, column=0)
        str_vars[key] = tk.StringVar(value=value)
        values[key] = tk.Entry(root, textvariable=str_vars[key])
        values[key].grid(row=row, column=1)
        row += 1;

    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=submit_data)
    submit_button.grid(row=row, column=1)

    root.mainloop()
#   print (f"{global_res=}")
    return global_res


def run_updated_mapping():
    entries = {
            "First": "Alex",
            "Last": "Kleider", 
            "Phone": "650/269-8936",
             }
    
    root_title = "User Info"
    

    for key, value in updated_mapping(entries, root_title).items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run_updated_mapping()

