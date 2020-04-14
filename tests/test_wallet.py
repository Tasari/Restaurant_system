from wallet import Wallet

def test_wallet_creation():
    wallet = Wallet(5000)
    assert wallet.money == 5000

def test_wallet_add_money():
    wallet = Wallet(5000)
    wallet.add_money(2500)
    assert wallet.money == 7500