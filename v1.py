#!/usr/bin/env python3

# File: v1.py

import tkinter as tk

def submit_data():
    name = name_entry_var.get()
    email = email_entry_var.get()
    return (f"{name=}, {email=}")

root = tk.Tk()
root.title("User Info")

# Name Entry
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_entry_var)
name_entry.grid(row=0, column=1)

# Email Entry
email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0)
email_entry_var = tk.StringVar()
email_entry = tk.Entry(root, textvariable=email_entry_var)
email_entry.grid(row=1, column=1)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=2, column=1)

root.mainloop()
