from tkinter import Button, Toplevel, Listbox, MULTIPLE
from tools import get_all_items_from_table, string_to_object_from_table
from tables.products import Product
from frontend.tools.amount_selector import AmountSelector
from frontend.tools.scrollable_frame import ScrollFrame
from tables.order import Order

class PreOrder():
    def __init__(self):
        self.possible_to_order = get_all_items_from_table(Product)
        self.ordered = []

    def add_to_ordered(self, product):
        try:
            assert product in self.possible_to_order
            self.possible_to_order.remove(product)
            self.ordered.append(product)
        except AssertionError:
            print("That product is not possible to order")

    def remove_from_ordered(self, product):
        try:
            assert product in self.ordered
            self.ordered.append(product)
            self.possible_to_order.remove(product)

        except AssertionError:
            print("That product is not ordered")

    def finish_preorder(self, amount_selectors_list, wallet, user):
        final_order = Order()
        for amount_selector in amount_selectors_list:
            final_order.add_product_to_order(amount_selector.item, amount_selector.get_entry())
        user.finish_order(wallet, final_order)

def order_creation(user, wallet):
    preorder = PreOrder()
    create_order_window(preorder)
    return

def create_order_window(preorder, to_destroy=None):
    if to_destroy != None:
        to_destroy.destroy()
    new_order_window = Toplevel()
    new_order_window.title("New order")
    add_to_order_button = Button(new_order_window, text="Add new item to order", command = lambda: edit_order(new_order_window, preorder, "Add"))
    add_to_order_button.grid(row=0, column=0)
    remove_from_order_button = Button(new_order_window, text="Remove item from order", command = lambda: edit_order(new_order_window, preorder, "Remove"))
    remove_from_order_button.grid(row=0, column=1)
    all_items_in_order = ScrollFrame(new_order_window)
    amount_selectors_list = []
    for item in preorder.ordered:
        amount_selector = AmountSelector(all_items_in_order.viewPort, item)
        amount_selectors_list.append(amount_selector)
        amount_selector.pack()
    all_items_in_order.grid(row=1, columnspan=2)


def edit_order(master, preorder, mode):
    master.destroy()
    listbox_window = Toplevel()
    listbox = Listbox(listbox_window, selectmode=MULTIPLE)
    if mode=='Add':
        items_to_show = preorder.possible_to_order
    else:
        items_to_show = preorder.ordered
    for item in enumerate(items_to_show):
        listbox.insert(item[0], item[1].name) 
    listbox.grid(row=0, rowspan=2, columnspan=2)
    ok_button = Button(listbox_window, text=mode, command=lambda: modify_preorder(preorder, mode, listbox_window, listbox))
    cancel_button = Button(listbox_window, text="Cancel", command=lambda: create_order_window(preorder, listbox_window))
    ok_button.grid(row=2, column=0)
    cancel_button.grid(row=2, column=1)

def modify_preorder(preorder, mode, listbox_window, listbox):
    selected = listbox.curselection()
    if mode == "Add":
        for item in selected:
            item_object = string_to_object_from_table(listbox.get(item), Product)
            preorder.ordered.append(item_object)
            for to_remove in preorder.possible_to_order:
                if item_object.name == to_remove.name:
                    preorder.possible_to_order.remove(to_remove)
    else:
        for item in selected:
            item_object = string_to_object_from_table(listbox.get(item), Product)
            preorder.possible_to_order.append(item_object)
            for to_remove in preorder.ordered:
                if item_object.name == to_remove.name:
                    preorder.ordered.remove(to_remove)
    create_order_window(preorder, listbox_window)
