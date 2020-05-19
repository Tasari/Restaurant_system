from frontend.login import log_in
from frontend.main_menu import main_menu
from wallet import Wallet
from tables import order
user = log_in()
print(user)
wallet = Wallet(99990)
main_menu(user, wallet)
