from tkinter import Tk, Label, Button
from tkinter.ttk import Notebook, Frame
from frontend.order_creation import order_creation
def main_menu(user):
    main_menu = Tk()
    main_menu.title("Main Menu")
    tabs = Notebook(main_menu)
    tabs.grid(column=0, row=0, columnspan=25, rowspan=25, sticky="NEWS")
    
    tab_Order = Frame(tabs)
    new_order_button = Button(tab_Order, text = "Create new order", 
                            height=12,
                            width=25,
                            command = order_creation)
    new_order_button.grid(column=0, row=0)

    tab_Products = Frame(tabs)
    
    tab_Stock = Frame(tabs)
    
    tab_Workers = Frame(tabs)
    
    tabs.add(tab_Order, text="Order")
    tabs.add(tab_Products, text="Products")
    tabs.add(tab_Stock, text="Stock")
    tabs.add(tab_Workers, text="Workers")
    main_menu.mainloop()
