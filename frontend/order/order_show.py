from tools import get_all_items_from_table
from tables.order import Order
from tkinter import Toplevel, Listbox, Button, Label
class AllOrders():
    def __init__(self):
        self.all_orders = get_all_items_from_table(Order)

    

def order_show():
    all_orders = get_all_items_from_table(Order)
    all_orders_window = Toplevel()
    all_orders_window.title("All orders")
    check_order_button = Button(all_orders_window, text="Check order")
    cancel_button = Button(all_orders_window, text="Cancel", command= lambda: cancel_show(all_orders_window))
    listbox = Listbox(all_orders_window)
    for order in enumerate(all_orders):
        listbox.insert(order[0], order[1].order)
    listbox.grid(column=0, row=0, rowspan=4, columnspan=4)
    check_order_button.grid(column=0, row=4, columnspan=2)
    cancel_button.grid(column=2, row=4, columnspan=2)

def cancel_show(master):
    master.destroy()