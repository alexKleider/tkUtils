#!/usr/bin/env python3

# File: gui.py  (graphical user interface using tKinter)

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

default_func_menu_header = "Choose a Function to Run"

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


def func_menu(funcs, header=default_func_menu_header):
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
    
    func_menu(funcs)


if __name__ == "__main__":
    test_funcs = (checkYN, ck_func_menu, )
    print("Choose which function to test:")
    for index, func in enumerate(test_funcs, start=1):
        print(f"  {index:>3}  {func.__name__}")
    choice = input(f"Which one? (1..{len(test_funcs)}) ")
    func_index = int(choice) -1
    test_funcs[func_index]()

