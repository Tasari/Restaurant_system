from tkinter import Button
from frontend.workers.worker_add import worker_add
from frontend.workers.worker_modify import worker_modify
from frontend.workers.worker_remove import worker_remove

def workers_tab_menu(master):
    new_worker_button = Button(master, text = "Create new worker", 
                            height=12,
                            width=25,
                            command = worker_add)
    new_worker_button.grid(column=0, row=0)   

    modify_worker_button = Button(master, text = "Modify worker", 
                            height=12,
                            width=25,
                            command = worker_modify)
    modify_worker_button.grid(column=1, row=0)

    remove_worker_button = Button(master, text = "Remove worker", 
                            height=12,
                            width=25,
                            command = worker_remove)
    remove_worker_button.grid(column=0, row=1)

 