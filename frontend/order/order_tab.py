from tkinter import Button
from frontend.order.order_creation import order_creation
from frontend.order.order_show import order_show

def order_tab_menu(master):
    new_order_button = Button(master, text = "Create new order", 
                            height=12,
                            width=25,
                            command = order_creation)
    new_order_button.grid(column=0, row=0)

    all_orders_show_button = Button(master, text = "Show all orders list", 
                            height=12,
                            width=25,
                            command = order_show)
    all_orders_show_button.grid(column=1, row=0)