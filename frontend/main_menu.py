from tkinter import Tk, Label, Button
from tkinter.ttk import Notebook, Frame
from frontend.order.order_tab import order_tab_menu
from frontend.products.product_add import product_add
from frontend.products.product_modify import product_modify
from frontend.products.product_remove import product_remove
from frontend.stock.stock_add import stock_add
from frontend.stock.stock_modify import stock_modify
from frontend.stock.stock_remove import stock_remove
from frontend.workers.worker_add import worker_add
from frontend.workers.worker_modify import worker_modify
from frontend.workers.worker_remove import worker_remove

def main_menu(user):
    main_menu = Tk()
    main_menu.title("Main Menu")
    tabs = Notebook(main_menu)
    tabs.grid(column=0, row=0, columnspan=25, rowspan=25, sticky="NEWS")
    
    tab_Order = Frame(tabs)
    order_tab_menu(tab_Order)
    tab_Products = Frame(tabs)
    new_product_button = Button(tab_Products, text = "Create new product", 
                            height=12,
                            width=25,
                            command = product_add)
    new_product_button.grid(column=0, row=0)

    tab_Stock = Frame(tabs)
    new_product_button = Button(tab_Stock, text = "Create new stock", 
                            height=12,
                            width=25,
                            command = stock_add)
    new_product_button.grid(column=0, row=0)    
    
    tab_Workers = Frame(tabs)
    new_worker_button = Button(tab_Workers, text = "Create new worker", 
                            height=12,
                            width=25,
                            command = worker_add)
    new_worker_button.grid(column=0, row=0)    

    tabs.add(tab_Order, text="Order")
    tabs.add(tab_Products, text="Products")
    tabs.add(tab_Stock, text="Stock")
    tabs.add(tab_Workers, text="Workers")
    main_menu.mainloop()
