from frontend.login import log_in
from frontend.main_menu import main_menu
user = log_in()
print(user)
main_menu(user)