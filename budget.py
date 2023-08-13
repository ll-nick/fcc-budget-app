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
    

def create_spend_chart(categories):