from tkinter import Tk, Label, Entry, Button, Frame, Toplevel
from base_template import Session
import tables.worker
import tables.order

def login_with_data(window, username, password):
    session=Session()
    global user
    user = session.query(tables.worker.Worker).\
        filter(tables.worker.Worker.username == username and tables.worker.Worker.password == password).first()
    if user is None:
        Label(window, text="Invalid data").grid(row=4, column=1)
    else:
        window.destroy()
def log_in():
    window = Tk()
    window.title("Shop System")
    window.geometry("250x155")
    Label(window, text="Login", font=('Arial', 25)).grid(row=0, column=1)

    Label(window, text="Username").grid(row=1, column=0)
    username = Entry(window, bd=2, width=28)
    username.grid(row=1, column=1, columnspan=2)

    Label(window, text="Password").grid(row=2, column=0)
    password = Entry(window, bd=2, width=28)
    password.grid(row=2, column=1, columnspan=2)

    buttons_frame = Frame(window)
    buttons_frame.grid(row=3, column=1)

    login_button = Button(buttons_frame, text = "Log in", 
                            height=2,
                            width=6,
                            command = lambda: 
                            login_with_data(window, username.get(), password.get()))
    login_button.grid(row=0, column = 0)

    guest_button = Button(buttons_frame, text = "Log in \nas guest",
                            height=2,
                            width=6,
                            command = lambda: 
                            login_with_data(window, "guest", "guest"))
    guest_button.grid(row=0, column = 1)
    window.mainloop()
    return user