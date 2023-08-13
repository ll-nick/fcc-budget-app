import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False
    
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, "Transfer to " + category.name)
        category.deposit(amount, "Transfer from " + self.name)
        return True

    def __str__(self):
        res = self.title_str()
        item_strings = (self.item_str(item) for item in self.ledger)
        res += "".join(item_strings)
        res += self.total_str()
        return res
    
    def title_str(self, title_length = 30):
        name_length = len(self.name)
        prefix = math.ceil((title_length - name_length) / 2) * "*"
        suffix = math.ceil((title_length - name_length) / 2) * "*"
        return prefix + self.name + suffix + "\n"
    
    def item_str(self, item, string_length = 30):
        name = item["description"][:23]
        amount = "{:.2f}".format(item["amount"])[:7]
        fill = (string_length - len(name) - len(amount)) * " "
        return name + fill + amount + "\n"
    
    def total_str(self):
        return "Total: " +  "{:.2f}".format((self.get_balance()))
    

def create_spend_chart(categories):
    pass