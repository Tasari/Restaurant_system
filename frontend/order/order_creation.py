from tkinter import Button, Toplevel, Label, Entry, Frame, Scrollbar, Canvas
from tools import get_all_items_from_table
from tables.products import Product
from frontend.tools.amount_selector import AmountSelector

def order_creation():
    items = get_all_items_from_table(Product)
    ordered_items = []
    new_order_window = Toplevel()
    new_order_window.title("New order")
    test = AmountSelector(new_order_window, 'test')
    test.pack()
    return

def add_product_to_order():
    return
def remove_product_from_order(master):
    return

def onFrameConfigure(das):
    return