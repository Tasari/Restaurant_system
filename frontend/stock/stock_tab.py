from tkinter import Button
from frontend.stock.stock_add import stock_add
from frontend.stock.stock_modify import stock_modify
from frontend.stock.stock_remove import stock_remove

def stock_tab_menu(master):
    new_stock_button = Button(master, text = "Create new stock", 
                            height=12,
                            width=25,
                            command = stock_add)
    new_stock_button.grid(column=0, row=0)   

    modify_stock_button = Button(master, text = "Modify stock", 
                            height=12,
                            width=25,
                            command = stock_modify)
    modify_stock_button.grid(column=1, row=0)

    remove_stock_button = Button(master, text = "Remove stock", 
                            height=12,
                            width=25,
                            command = stock_remove)
    remove_stock_button.grid(column=0, row=1)

 