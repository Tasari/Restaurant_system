from tools import get_all_items_from_table
from tables.products import Product
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

