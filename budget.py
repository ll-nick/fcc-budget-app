class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []


    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False
    

def create_spend_chart(categories):