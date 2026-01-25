#!/usr/bin/env python3

# File: commands.py

"""
Provides routines to interact with Bolinas Rod & Boat
Club data base.  Can use either gui or cli by choosing
which to import "as interface."
"""

import routines

import gui as interface     # choose one (graphical)
#import cli as interface     # or the other (command line)

def add_person():
    """
    Add a person to the people table.
    """
#   keys = routines.keys_from_schema("People", brackets=(1,0))
    keys = ("first", "last", "phone",)
    mapping = {key: "" for key in keys}
    ret = interface.updated_mapping(mapping,
            root_title="Enter demographics")
    if not ret:
        print("mission aborted")
        return
    keys = tuple([key for key in ret.keys()])
    values = tuple([value for value in ret.values()])
    query = f"""INSERT INTO People {keys} values {values};"""
    print(f"{query}")

def select_person():
    """
    Provide cluse to be given choices from which
    to select a person.
    """
    while True:
        keys = ("first", "last", )
        mapping = {key: "" for key in keys}
        ret = interface.updated_mapping(mapping,
                    root_title="Enter clues using % wildcard:")
        if not ret:
            if interface.yn(title="Abort?!?"): return
            else: continue
        ret4query = {}
        for key, value in ret.items():
            if value:
                ret4query[key] = value
        if not ret4query:
            if interface.yn(title = "Abort!?!?"):  # use default message
                return
            else: continue
        break
    res = {key: value for key, value in ret4query.items() if value}
    condition = [f'{key} LIKE "{value}"' for key, value
                 in res.items() if value]
    condition = ' and '.join(condition)
    query = f'''SELECT personID, first, last from People
            WHERE {condition}; ''';
    print(query)
    for line in routines.fetch(query, from_file=False):
        print(line)
    


def write_query():
    ret = {
            "first": "Alex", "last": "Kleider", "phone": "911",
            "email": "alex@kleider.ca",                      }
    keys = tuple([key for key in ret.keys()])
    values = tuple([value for value in ret.values()])
    query = f"""INSERT INTO People {keys} values {values};"""
    print(f"{query}")
    

def add_applicant():
    """
    Assumes applicant is already in the People table.
    Creates entry in the Applicant and Person_Status tables.
    Collects sponsors and available dates.
    """
    pass

if __name__ == "__main__":
#   write_query()
#   add_person()
    select_person()

