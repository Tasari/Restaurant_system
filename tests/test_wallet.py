from wallet import Wallet

def test_wallet_creation():
    '''
    Tests valid creation of wallet
    '''
    wallet = Wallet(5000)
    assert wallet.money == 5000

def test_wallet_add_money():
    '''
    Tests adding money to wallet
    '''
    wallet = Wallet(5000)
    wallet.add_money(2500)
    assert wallet.money == 7500