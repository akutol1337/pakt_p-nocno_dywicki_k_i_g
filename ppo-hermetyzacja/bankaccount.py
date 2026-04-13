class BankAccount:
    def __init__(self, account_name):
        self.account_name = account_name
        self._operations = 0
        self._account_balance = 0

    def deposit_money(self, amount):
        self._account_balance += amount
        self._operations += 1
        print(f"You deposited ${amount}")

    def withdraw_money(self, amount):
        if amount > self._account_balance:
            raise ValueError("You don't have enough money!")
        
        self._account_balance -= amount
        self._operations += 1
        print(f"You withdraw ${amount}")

    def get_balance(self):
        print(f"You have ${self._account_balance} in your account")


if __name__ == '__main__':
    my_account = BankAccount("My private account")
    my_account.get_balance()
    my_account.deposit_money(10000000)
    my_account.get_balance()
    my_account.withdraw_money(5000)
    my_account.get_balance()
    print("Number of operations:", my_account._operations)