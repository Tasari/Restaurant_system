import tkinter as tk
from pathlib import Path
class AmountSelector(tk.Frame):
    def __init__(self, parent, item_name):
        super().__init__(parent)
        self.minus_image = tk.PhotoImage(file = ".\images\minus.png")
        self.plus_image = tk.PhotoImage(file = ".\images\plus.png")
        self.item_name = tk.Label(self, borderwidth=1, text=item_name, font = ("Courier", 15))
        self.subtract_button = tk.Button(self, image=self.minus_image)
        self.entry = tk.Entry(self, font = ("Courier", 35), width=2)
        self.add_button = tk.Button(self, image = self.plus_image)

        self.item_name.grid(column=0, row=0)
        self.subtract_button.grid(column=1, row=0)
        self.entry.grid(column=2, row=0)
        self.add_button.grid(column=3, row=0)


    def get_entry(self):
        return self.entry.get()