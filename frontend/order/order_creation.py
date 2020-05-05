from tkinter import Button, Toplevel, Label, Entry, Frame, Scrollbar, Canvas

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def order_creation():
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


    for i in range(25):
        label = Label(order_frame, text="Test{}".format(i))
        label.grid(row=i, column=0)

    return

def add_product_to_order(master):
    return
def remove_product_from_order(master):
    return