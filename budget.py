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
    
    def get_spendings(self):
        return sum(item["amount"] for item in self.ledger if item["amount"] < 0)
    
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
    res = "Percentage spent by category\n"
    columns = [create_column(category, percentage(category, categories)) for category in categories] 
    y_axis = "".join([("  " + str(10 * y))[-3:] + "|\n" for y in range(10, -1, -1)])
    columns.insert(0, y_axis)
    extra_underline = " \n" * 11 + "-\n"
    columns.append(extra_underline)
    res += concat_columns(columns)
    return remove_extra_lines_breaks(res)

def percentage(category, categories):
    total = sum([c.get_spendings() for c in categories])
    return 100 * category.get_spendings() / total

def create_column(category, percentage):
    rounded_percentage = math.floor(percentage / 10) * 10
    res = "".join(["   \n" for _ in range(100, rounded_percentage, -10)])
    res += "".join(" o \n" for _ in range(rounded_percentage, -1, -10))
    res += "---\n"
    res += "".join([" " + l + " \n" for l in category.name])
    
    return res

def concat_columns(columns):
    columns = extend_columns(columns)
    num_lines = len(columns[0].split("\n"))
    res = ""
    for line in range(num_lines):
        for column in columns:
            res += column.split("\n")[line]
        res += "\n"

    return res

def extend_columns(columns):
    max_num_lines = max([len(column.split("\n")) for column in columns])
    for idx, column in enumerate(columns):
        line_length = len(column.split("\n")[0])
        while len(column.split("\n")) < max_num_lines:
            column += line_length * " " + "\n"
        columns[idx] = column

    return columns

def remove_extra_lines_breaks(s):
    while s.endswith("\n"):
        s = s[:-1]
    return s