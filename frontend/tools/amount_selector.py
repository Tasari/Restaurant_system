import tkinter as tk
from pathlib import Path
class AmountSelector(tk.Frame):
    def __init__(self, parent, item):
        super().__init__(parent)
        self.minus_image = tk.PhotoImage(file = ".\images\minus.png")
        self.plus_image = tk.PhotoImage(file = ".\images\plus.png")
        self.item = item
        self.item_name = tk.Label(self, borderwidth=1, text=item.name, font = ("Courier", 15), width=15)
        self.subtract_button = tk.Button(self, image=self.minus_image, command = self.subtract_one)
        self.entry = tk.Entry(self, font = ("Courier", 35), width=3)
        self.add_button = tk.Button(self, image = self.plus_image, command = self.add_one)
        self.entry.insert(0, "0")
        self.item_name.grid(column=0, row=0)
        self.subtract_button.grid(column=1, row=0)
        self.entry.grid(column=2, row=0)
        self.add_button.grid(column=3, row=0)

    def add_one(self):
        amount = int(self.entry.get())+1
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(amount))

    def subtract_one(self):
        amount = int(self.entry.get())-1
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(amount))

    def get_entry(self):
        return self.entry.get()