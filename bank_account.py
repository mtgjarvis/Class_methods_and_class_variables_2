class BankAccount:
    
    interest_rate = 0.01
    accounts = []

    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, credit):
        self.balance += credit
        return self.balance

    def withdraw(self, debits):
        self.balance -= debits
        return self.balance

    # def __repr__(self): 
        return f'{self.balance}'

    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account

    @classmethod
    def total_funds(cls):
        return sum(account.balance for account in cls.accounts)

    # use the cls for calling callmethod level and 
    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance = account.balance * (1 + cls.interest_rate)
        return account.balance


# my_account = BankAccount.create()
# your_account = BankAccount.create()

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0

