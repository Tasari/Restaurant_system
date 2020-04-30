from tkinter import Button
from frontend.products.product_add import product_add
from frontend.products.product_modify import product_modify
from frontend.products.product_remove import product_remove

def products_tab_menu(master):
    product_add_button = Button(master, text = "Create new product", 
                            height=12,
                            width=25,
                            command = product_add)
    product_add_button.grid(column=0, row=0)

    modify_product_button = Button(master, text = "Modify product", 
                            height=12,
                            width=25,
                            command = product_modify)
    modify_product_button.grid(column=1, row=0)

    remove_product_button = Button(master, text = "Remove product", 
                            height=12,
                            width=25,
                            command = product_remove)
    remove_product_button.grid(column=0, row=1)
