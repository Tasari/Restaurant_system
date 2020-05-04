from tkinter import Button, Toplevel, Label, Entry

def order_creation():
    new_order_window = Toplevel()
    new_order_window.title("New order")
    add_product_to_order_button = Button(new_order_window, text = "Add new product to order",
                                                    height = 12,
                                                    width = 25,
                                                    command = add_product_to_order)
    add_product_to_order_button.grid(column=0, row=0)
    
    remove_product_from_order_button = Button(new_order_window, text = "Remove new product from order",
                                                    height = 12,
                                                    width = 25,
                                                    command = remove_product_from_order)
    remove_product_from_order_button.grid(column=0, row=0)
    return