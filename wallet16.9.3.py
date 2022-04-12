class Wallet:
    def __init__(self, firstname, secondname, balance):
        self.firstname = firstname
        self.secondname= secondname
        self.balance = balance

    def wallet(self):
        return f'(Клиент-{self.firstname} {self.secondname}; Баланс: {self.balance} руб.)'

new_wallet = Wallet('Никита', 'Пискунов', 100000)
print(new_wallet.wallet())
