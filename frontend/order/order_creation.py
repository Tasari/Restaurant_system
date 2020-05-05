from tkinter import Button, Toplevel, Label, Entry, Frame, Scrollbar, Canvas
from tools import get_all_items_from_table
from tables.products import Product
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def order_creation():
    global items
    global ordered_items
    new_order_window = Toplevel()
    new_order_window.title("New order")
    button_frame = Frame(new_order_window)
    button_frame.pack()
    canvas = Canvas(new_order_window)
    order_frame = Frame(canvas)
    order_scrollbar = Scrollbar(new_order_window, orient="vertical", command = canvas.yview)
    canvas.configure(yscrollcommand=order_scrollbar.set)
    order_scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 2), window=order_frame, anchor="nw")
    order_frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    add_product_to_order_button = Button(button_frame, text = "Add new product to order",
                                                    height = 12,
                                                    width = 25,
                                                    command = add_product_to_order)
    add_product_to_order_button.grid(column=0, row=0)
    
    remove_product_from_order_button = Button(button_frame, text = "Remove new product from order",
                                                    height = 12,
                                                    width = 25,
                                                    command = lambda: remove_product_from_order(order_frame))
    remove_product_from_order_button.grid(column=1, row=0)

    items = get_all_items_from_table(Product)
    ordered_items= []

    for i in ordered_items:
        label = Label(order_frame, text=i.name)
        label.pack()

    return

def add_product_to_order():
    global items
    global ordered_items
    add_prod_window = Toplevel()
    add_prod_window.title("New order")
    button_frame = Frame(add_prod_window)
    canvas = Canvas(add_prod_window)
    order_frame = Frame(canvas)
    order_scrollbar = Scrollbar(add_prod_window, orient="vertical", command = canvas.yview)
    canvas.configure(yscrollcommand=order_scrollbar.set)
    order_scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 2), window=order_frame, anchor="nw")
    order_frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    button_frame.pack()
    add_product_to_order_button = Button(button_frame, text = "Add product",
                                                    height = 12,
                                                    width = 25,
                                                    command = add_product_to_order)
    add_product_to_order_button.grid(column=0, row=0)
    
    remove_product_from_order_button = Button(button_frame, text = "Cancel",
                                                    height = 12,
                                                    width = 25,
                                                    command = lambda: remove_product_from_order(order_frame))
    remove_product_from_order_button.grid(column=1, row=0)
    for i in items:
        label = Label(order_frame, text=i.name)
        label.pack()
    return
def remove_product_from_order(master):
    return