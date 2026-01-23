#!/usr/bin/env python3

# File: cli.py    command line interface: alternative to gui.py

"""
Provides command line interfaces to the following... 
    yn
    func_menu
    text_menu
    update_mapping
"""

def yn(title='', message="Answer yY)es or nN)o"):
    """
    Returns True or False.
    <title> (ignored if None or empty) serves as a
    header which is printed and underlined ("=");
    """
    if title:
        print(title)
        print("=" * len(title))
    print(message)
    yn = input("Yes or No? (y/n) ")
    if yn and yn[0] in "yY":
        return True



def func_menu(funcs, header="Choose a Function to Run..."):
    """
    <funcs> is a listing of functions.
    The one chosen is executed (unless user responds
    with an invalid index.)
    <header> (if evaluates to True) is printed and underlined.
    """
    if header:
        print(header)
        print("=" * len(header))
    for index, func in enumerate(funcs, start=1):
        print(f"  {index:>3}  {func.__name__}")
    choice = input(f"Which one? (1..{len(funcs)}) ")
    try:
        choice = int(choice)
    except ValueError:
        print("Choice must evaluate to an integer!")
        return
    if choice<1 or choice>len(funcs):
        print(f"{choice} is out of range.")
        return
    funcs[choice-1]()
#   func_index = choice - 1
#   func = funcs[func_index]
#   func()

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


def text_menu(choices, rootTitle):
    """
    Returns text chosen from list of <choices>.
    Returns empty string if no choice is made.
    """
    pass


def updated_mapping(mapping, root_title="Record Update"):
    """
    Returns <mapping> as modified by user leaving the original mapping
    unchanged.
    Key/Value pairs are presented under the header <root_title>.
    Allows for aborting in which case returns None.
    """
    pass


def checkYN():
    title = "Answer Yes or No please..."
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
#   print(f"Running func_menu...")
    func_menu(funcs, "Available functions:")

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




