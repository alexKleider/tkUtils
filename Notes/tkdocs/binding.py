#!/usr/bin/env python3

# File: binding.py

"""
For events that don't have a widget-specific callback configuration
option associated with them, you can use Tk's bind to capture any
event and then (like with callbacks) execute an arbitrary piece of code.
Here's a (silly) example showing a label responding to different events.
When an event occurs, a description of the event is displayed in the label.
"""

from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
# a <ButtonPress-1> event. Here, the <ButtonPress> is the actual
# event, but the -1 is an event detail specifying the left button.

l.bind('<3>', lambda e: l.configure(text='Clicked third mouse button'))
# This next binding looks for a <3> event which is a shorthand for
# <ButtonPress-3> which responds to events generated when the third
# mouse button is clicked.
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# <Double-1> (shorthand for <Double-ButtonPress-1>) adds another
# modifier, Double, making it respond to a left mouse double click.
l.bind('<B3-Motion>', lambda e: l.configure(
                        text=f'third button drag to {e.x},{e.y}'))
# <B3-Motion>) captures mouse movement (Motion), but only when the
# third mouse button (B3) is held down.
# Example of event parameter usage. Many events carry additional
# information, e.g., the position of the mouse when
# it's clicked. Tk provides access to these parameters in Tcl callback
# scripts through the use of percent substitutions. These percent
# substitutions let you capture them so they can be used in your script.
# We'll see percent substitutions used later in another context, entry
# widget validation.
# Tkinter abstracts away these percent substitutions and instead
# encapsulates all the event parameters in an event object.
# Above, we used the x and y fields to retrieve the mouse position.
# A function must be provided as the event callback.
# Often lambdas are used in 'one of' situations.
# "event object" = callback function??

root.mainloop()

