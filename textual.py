#!/usr/bin/env python3

# File: ~/Git/TK/textual.py

import tkinter as tk
from tkinter import messagebox
import routines

"""
global_choice = None  # used globally to collect
global_res = {}         # info from the gui window
"""
# the following function should be elsewhere!?!
# is it even needed?
junk = '''
def get_stati(personID):
    """
    ## Was called get_mode(
    collects Person_Status table entries for person IDed.
    """
    ps_fields = routines.keys_from_schema("Person_Status")
    res = routines.fetch(f"""SELECT * FROM Person_Status
            WHERE personID = {personID}; """, from_file=False)
#   _ = input(repr(res))  #!# <res> is NOT USED!!!
'''

def keys_from_schema(table, brackets=(0,0)):
    """
    ## needs to be imported from routines ##
    query comes from: https://stackoverflow.com/questions/11996394/is-there-a-way-to-get-a-schema-of-a-database-from-within-python
    <brackets> provides ability to ignore first brackets[0]
    and last brackets[1] primary keys such as 'personID' (in
    which case it can be set to (1,0).
    Tested in tests/test_routines.py
    """
    query =  f"pragma table_info({table})"
    res = routines.fetch(query, from_file=False)
    begin = brackets[0]
    end = len(res) - brackets[1]
    return  [item[1] for item in res[begin:end]]
    # item[1] is the column/key.

# File: akfYN.py

def yn(title, message):
    """
    basic tk method to get a yes or no answer
    """
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

def yes_no(text, title="Run query?"):
    """Code base version"""
    return yn(message, title)

def checkYN():
    """tests yn and yes_no"""
    title = "Exit Application"
    message = """This could be a very long message.
        Several lines long, infact!
        Do you really want to exit?"""

    if yn(title, message) == True:
        print("Returning True")
    else:
        print("Returning False")
#====================================
# File: choose_text.py
global_choice = None  # used globally

def text_menu(choices, rootTitle):
    """
    basic tk menu
    Returns a choice selected from <choices>, a list of strings.
    """
    def show_selection(event):
        # Get the index of the selected item
        global global_choice
        selection_index = listbox.curselection()
        if selection_index:
            # Get the value of the selected item
            selected_item = listbox.get(selection_index[0])
            label.config(text=f"Selected: {selected_item}")
            global_choice = selected_item
            root.quit()
    root = tk.Tk()
    root.title("Listbox Menu Example")
    listbox = tk.Listbox(root, selectmode=tk.SINGLE)
    listbox.pack(padx=10, pady=10)
    for item in choices:
        listbox.insert(tk.END, item)
    listbox.bind('<<ListboxSelect>>', show_selection)
    label = tk.Label(root, text="Select an item")
    label.pack(pady=10)
    root.mainloop()
    return global_choice

#====================================
# File: collector.py
""" Provides function <updated_mapping>.  """
global_res = {}  # collects info from the gui window

def updated_mapping(entries, root_title="Record Update"):
    """
    Provides a way of entering or modifying the values of a
    <mapping>, presented in a window labeled <root_title>.
    Returns an empty dict if closed without using the submit button.
    The <submit> button causes return of a new mapping with
    the visible values. The original mapping is left unchanged.
    Retrieval depends on <global_res> which must exist globally.
    """
    def submit_data():
        global global_res
        for key in entries.keys():
            global_res[key] = str_vars[key].get()
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
    return global_res


def get_fields(fields, header="Enter values for each key"):
    # third param <font> redacted!
    # replaces change_mapping, change_or_add_values, get_fields4
    """
    Prompts user to supply values for each field.
    Returns None if user aborts, otherwise...
    Returns a dict keyed by <fields>,
    values are the entered (possibly empty) strings
    # Has been tested.
    # Best to use <change_mapping> instead?
    """
    return updated_mapping(fields, root_title=header)


def edit_person_status():
    _ = input("edit_person_status hasn't been 'translated'!")


def get_demographics(header="Enter demographic data",
                     applicant=True):
    """
    Collects all demographic data to populate the People table
    AND (unless <applicant> is set to <False>) also collect entries
    for two sponsor names and app_rcvd and fee_rcvd fields.
    Returns a dict or None (if user aborts.)
    Client is code/data_entry.py
    """
    keys = keys_from_schema("People", brackets=(1,0))
    if applicant:
        header = "Enter applicant demographics"
        keys.extend(["sponsor1", "sponsor2", "app_rcvd", "fee_rcvd"])
    mapping = {}
    for key in keys:
        mapping[key] = ""
    return get_fields(mapping, header)


def people_choices(header_prompt="Enter hints: % = wild card"):
    """
    Returns a list of people records based on hints provided.
    Use '%' wild card for selection.
    Returns an empty list if none match.
    1st step in providing 
    code/routines/pick_People_record functionality!
    """
    keys = routines.keys_from_schema("People")
    fields = keys[1:4]
    mapping = {}
    for key in fields:
        mapping[key] = ''
    data = get_fields(mapping,
          header = 'Enter hints using "%" as wild cards:')
#   _ = input(f"values: {[value for value in data.values() if value]}")
    if not [value for value in data.values() if value]: return
    query_lines = [
        "SELECT *",
            "FROM People WHERE ", ]
    additional_lines = []
    if data['first']:
        additional_lines.append(
            f"""first LIKE "{data['first']}" """)
    if data['last']:
        additional_lines.append(
            f"""last LIKE "{data['last']}" """)
    if data['suffix']:
        additional_lines.append(
            f"""suffix LIKE "{data['suffix']}" """)
    additional_lines = " AND ".join(additional_lines)
    query_lines.append(additional_lines)
    query = ' '.join(query_lines)
    query = query+"ORDER BY last, first"+';'
#   _ = input(query)
    ret = routines.query2dict_listing(query, keys,
            from_file=False)
    return ret


def pick(query, format_string,
                header="CHOOSE ONE",
                subheader="Choices are...",
                report=None):
    """
    Uses <query> to collect a list of dicts and presents
    user with a list of choices dictated by
    the format_string.
    Returns chosen dict or None (if none available or
    user aborts/cancels.)
    """
    mappings = routines.query2dicts(query)
    if not mappings:
        return
    options = [format_string.format(**rec)
            for rec in mappings]
    listing = zip(range(len(options)), options)
    for_display = [f"{item[0]:>2}: {item[1]}"
                for item in listing]
    #===================================
    layout=[[sg.Text(subheader,size=(50,1),
#           font='Lucida',justification='left'
            )],
            [sg.Listbox(values=for_display,
                select_mode='extended',
                key='CHOICE', size=(50,len(mappings)))],
            [sg.Button('SELECT',
#               font=('Times New Roman',12)
                ),
            sg.Button('CANCEL',
#                   font=('Times New Roman',12)
                    )
            ]]
    win =sg.Window(header,layout)
    e, v = win.read()
    win.close()
    if not v["CHOICE"]:
        return
    chosen_item = v['CHOICE'][0].strip().split()[0][:-1]
    if (e != "SELECT") or not v['CHOICE']:
        helpers.add2report(report,
            "pick returning None", also_print=True)
        return
    else:
        helpers.add2report(report,
            ["code.textual.pick:",
            "  line chosen...",
            f"    {repr(v['CHOICE'])}",
            "  record returned:",
            f"    {repr(mappings[int(chosen_item)])}"],
            also_print=False)
        return mappings[int(chosen_item)]


## Testing follows....

def run_updated_mapping():
    entries = {
            "First": "Joe",
            "Last": "Blow", 
            "Phone": "333/333-3333",
             }
    root_title = "User Info"
    res = updated_mapping(entries, root_title)
    print(f"{res=}")
    if res:
        for key, value in res.items():
            print(f"{key}: {value}")

def run_get_demographics():
    data = get_demographics()
    if data:
        print("get_demographics yields the following:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Execution of get_demographics aborted.")

def run_people_choices():
    ret = people_choices(header_prompt="Enter hints: % = wild card")
    if ret:
        print("Collected the following records...")
        for item in ret:
            print([value for value in item.values()])
    else:
        print("No matches found")

def pick_person(header='Hints (use "%" as wild card)',
                subheader=""):
    """
    Returns a person record from the People table
        or None.
    Used to obtain a record
    """
    while True:
        # 1st collect the 'hints' ==> data:
        fields = routines.keys_from_schema(
                        "People", brackets=(1,7))
        hints = {}
        for field in fields:
            hints[field] = ""
        while True:
            res = updated_mapping(hints, root_title=header)
            values = [value if value for value in res.values()]
            if not values:  # checking for an empty list
                print("Got an empty list; try again.")
                continue
        query_lines = [
            "Select personID, first, last, suffix",
                "from People where ", ]
        additional_lines = []
        if data['first']:
            additional_lines.append(
                f"""first like "{data['first']}" """)
        if data['last']:
            additional_lines.append(
                f"""last like "{data['last']}" """)
        if data['suffix']:
            additional_lines.append(
                f"""suffix like "{data['suffix']}" """)
        if not additional_lines:
            print("No clues provided; going again")
            continue
        additional_lines = " AND ".join(additional_lines)
        query_lines.append(additional_lines)
        query = ' '.join(query_lines)
        query = query+';'
#       _ = input(query)
        ret = routines.fetch(query, from_file=False)
        if not ret: continue
#       _ = input(repr(ret))
#       for item in ret:
#           print(item)
        choices = ["{0!s:>3} {1:} {2:} {3:}".format(*item) 
            for item in ret]

        #define layout
        layout=[[sg.Text(subheader,size=(30,1),
                )],
                [sg.Combo(choices,
                    default_value=choices[0],
                    key='choice')],
                [sg.Button('SELECT',
                    ),
                sg.Button('CANCEL',
                        )
                ]]

#       layout=[[sg.Text(choice), sg.InputText()]
#               for choice in choices]
#       layout.append([sg.Button('OK'),
#           sg.Button('Cancel')])
        #Define Window
        win =sg.Window(header,layout)
        #Read  values entered by user
        e, v = win.read()
        #close first window
        win.close()
        #access the selected value in the list box
        #and add them to a string
#       print(f"e returns {e}")
        if e == "CANCEL":
            continue
        elif e == None:
            return
        else:
    #       print("you chose: ",end='')
    #       print(repr(v['choice']))
            return routines.get_rec_by_ID(
                int(v['choice'].split()[0]))

def run_pick_person():
    while True:
        record = input(repr(pick_person()))
        print(repr(record))
        yn = input("Continue? (y/n) ")
        if not (yn and yn[0] in 'yY'):
            break



def run_text_menu():
    root_title = "Root Title"
    choices = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    print(f"Running test of text_menu...")
    print(f"Returning '{text_menu(choices, root_title)}'")


if __name__ == "__main__":
#   run_updated_mapping()
#   checkYN()
#   print(f"Returning '{text_menu()}'")
#   run_get_demographics()
#   run_people_choices()
#   run_text_menu()
    run_pick_person()




