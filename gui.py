#!/usr/bin/env python3

# File: gui.py  (graphical user interface using tKinter)

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

"""
Provides: so far- 
    yn
    func_menu
    text_menu
    update_mapping
"""

returned_choice = None  # a Global required by text_menu
global_res = {}  #  a Global required by update_mapping

def yn(title, message):
    """
    Returns True or False.
    Note: closing the window using the [x] button in the top right
    corner also returns false (same as hitting the "No" box.)
    """
    def show_yes_no_dialog():
        result = messagebox.askyesno(title, message)
        root.destroy()
        return result
    root = tk.Tk()
    root.withdraw()    # Hide the main window
    ret = show_yes_no_dialog()
    root.mainloop()
    return ret


def func_menu(funcs, header="Choose a Function to Run"):
    """
    <funcs> is a listing of functions.
    The one chosen is executed (unless user exits using [X].)
    """
    def destroyer(func):
        def wrapper(*args, **kwargs):
            res = func()
            root.destroy()
        return wrapper

    root = tk.Tk()
    root.title(header)
    root.geometry("400x300")

    # 1. Sidebar Frame
    sidebar = tk.Frame(root, bg="#2c3e50", width=150, height=300)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False) # Prevents frame from shrinking to button size

    # 2. Menu Buttons (Vertical Items)
    #menu_items = ["Dashboard", "Settings", "Profile", "Help"]
    #for item in menu_items:
    for func in funcs:
        # decorate each function to include root.destroy() 
        btn = tk.Button(
            sidebar, 
            text=func.__name__, 
            command= destroyer(func),
                    # ...decorate with a root.destroy() line
            bg="#2c3e50", 
            fg="white", 
            activebackground="#34495e", 
            activeforeground="white",
            bd=0, 
            padx=20, 
            pady=10, 
            anchor="w")
#       print(f"assigned {func.__name__}")
        btn.pack(fill="x") # Ensures buttons take full width of sidebar

    # 3. Main Content Area
#   main_area = tk.Frame(root, bg="white")
#   main_area.pack(side="right", expand=True, fill="both")

#   label = tk.Label(main_area,
#                    text="Select an option from the menu",
#                    bg="white")
#   label.pack(pady=50)

    root.mainloop()

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


def updated_mapping(mapping, root_title="Record Update"):
    """
    Provides a way of entering or modifying the values of a
    <mapping>, presented in a window labeled <root_title>.
    Returns None if closed without using the submit button.
    The <submit> button causes return of a new mapping with
    the visible values. The original mapping is left unchanged.
    Retrieval depends on <global_res> which must exist globally.
    """
    def submit_data():
        global global_res
        for key in mapping.keys():
            global_res[key] = str_vars[key].get()
        root.destroy()

    root = tk.Tk()
    root.title(root_title)

    keys = mapping.keys()
    labels = {}
    str_vars = {}
    values = {}

    row = 0;

    for key, value in mapping.items():
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
    return global_res


def checkYN():
    title = "Exit Application"
    message = """This could be a very long message.
        Several lines long, infact!
        Do you really want to exit?"""
    if yn(title, message):
        print("Returning True")
    else:
        print("Returning False")

def ck_func_menu():
    def func1():
        print(f"Executing func1")
        return "f1"
    def func2():
        print(f"Executing func2")
    def func3():
        print(f"Executing func3")
    def func4():
        print(f"Executing func4")
        return "f4"
    def func5():
        print(f"Executing func5")
    def func6():
        print(f"Executing func6")
    funcs = (func1, func2, func3, func4, func5, func6 )
    
    print(f"Running func_menu...")
    func_menu(funcs)

def ck_text_menu():
    root_title = "Root Title"
    # List of choices
    choices = ["AppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleApple",
               "BananaBananaBananaBananaBananaBananaBananaBanana",
               "CherryCherryCherryCherryCherryCherryCherryCherryCherryCherryCherryCherryCherry",
               "DateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDateDate",
               "ElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberryElderberry"]
    ret = text_menu(choices, root_title)
    
    print("Your choice...")
    print(repr(ret))


def ck_updated_mapping():
    mapping = {
            "First": "Joe",
            "Last": "Blow", 
            "Phone": "333/333-3333",
             }
    root_title = "People Entry"
    res = updated_mapping(mapping, root_title)
    if res:
        for key, value in res.items():
            print(f"{key}: {value}")
    else:
        print(f"Entry aborted (returned {res=})")


if __name__ == "__main__":
    test_funcs = (checkYN,
                  ck_func_menu,
                  ck_text_menu,
                  ck_updated_mapping)
    print("Choose which function to test:")
    for index, func in enumerate(test_funcs, start=1):
        print(f"  {index:>3}  {func.__name__}")
    choice = input(f"Which one? (1..{len(test_funcs)}) ")
    func_index = int(choice) -1
    func = test_funcs[func_index]
    print(f"Testing {func.__name__}...")
    func()
    print(f"...finished testing {func.__name__}...")




