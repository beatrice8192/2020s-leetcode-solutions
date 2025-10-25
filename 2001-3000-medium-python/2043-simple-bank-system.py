# https://leetcode.com/problems/simple-bank-system
class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if self.validAccount(account1) and self.validAccount(account2) and self.validBalance(account1, money):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.validAccount(account):
            self.balance[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if self.validAccount(account) and self.validBalance(account, money):
            self.balance[account - 1] -= money
            return True
        else:
            return False

    def validAccount(self, account):
        return account > 0 and account <= len(self.balance)

    def validBalance(self, account, money):
        return self.balance[account - 1] >= money

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

