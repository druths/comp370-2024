# myapp.py

from random import random

import math

from bokeh.layouts import column
from bokeh.models import Button, Dropdown
from bokeh.plotting import figure, curdoc

X = [x for x in range(0, 100)]

Y_up = [x for x in X]
Y_down = [-x for x in X]

# create a plot and style its properties
p = figure(
    x_range=(min(X), max(X)),
    y_range=(min(Y_down), max(Y_up)),
    toolbar_location=None,
)

# add a text renderer to the plot (no data yet)
r = p.line(x=X, y=Y_up)

ds = r.data_source


# create a callback that adds a number in a random location
next_Y = Y_down


def callback():
    global next_Y

    curr_y = ds.data["y"]

    new_data = dict()
    new_data["x"] = X
    new_data["y"] = next_Y
    ds.data = new_data

    next_Y = curr_y


def callback_item(event):
    new_data = dict()
    new_data["x"] = X
    new_data["y"] = Y_up if event.item == "Y_up" else Y_down
    ds.data = new_data


# add a button widget and configure with the call back
button = Button(label="Press Me")
button.on_event("button_click", callback)

menu = [("Up", "Y_up"), ("Down", "Y_down")]
dropdown = Dropdown(label="Dropdown button", menu=menu)
dropdown.on_event("menu_item_click", callback_item)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, p, dropdown))
