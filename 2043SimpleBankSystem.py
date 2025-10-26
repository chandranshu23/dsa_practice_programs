class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        n = len(balance)
        self.accounts = set(range(1,n+1))

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 not in self.accounts or account2 not in self.accounts:
            return False
        else:
            if self.balance[account1 - 1] < money:
                return False
            else:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True
                
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account not in self.accounts:
            return False
        else:
            self.balance[account - 1] += money
            return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account not in self.accounts:
            return False
        else:
            if self.balance[account - 1] < money:
                return False
            else:
                self.balance[account - 1] -= money
                return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)