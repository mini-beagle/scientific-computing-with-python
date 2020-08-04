class Category:
    test = 'x'
    def __init__(self, category):
        self.cat_name = category
        self.ledger = []
        self.cat_name = category.capitalize()
        self.balance = 0
    
    def deposit(self, amount, description=''):
        self.test = amount
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            amount = -amount
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.balance -= amount
            category.balance += amount
            amount = amount
            self.ledger.append({"amount": -amount, "description": 'Transfer to ' + category.cat_name})
            category.ledger.append({"amount": amount, "description": 'Transfer from ' + self.cat_name})
            return True
        else:
            return False
    
    def __str__(self):
        asterisks = int((30 - len(self.cat_name)) / 2)
        title = '*'*asterisks + self.cat_name + '*'*asterisks
        printout = title + '\n'

        for item in self.ledger:
            description = item['description'][:23]
            amount = item['amount']
            amount = f'{amount:.2f}'[:7]
            spaces = 30 - len(description) - len(amount)
            printout += description + ' '*spaces + amount + '\n'

        printout += 'Total: ' + str(self.balance)            
        return printout

def create_spend_chart(categories):
    printout = 'Percentage spent by category\n'
    totals = []
    total_spend = 0

    for cat in categories:
        spend = 0
        for item in cat.ledger:
            if item['amount'] < 0:      # withdrawals only
                spend += (-item['amount'])
        totals.append(spend)

    for amount in totals:
        total_spend += amount
    
    percentages = []
    for amount in totals:
        amount = (amount / total_spend) * 100
        rem = amount % 10
        amount -= rem
        percentages.append(amount)

    row = 100
    while row >= 0:
        printout += ' '*(3-len(str(row))) + str(row) + '|'
        for per in percentages:
            if per >= row:
                printout += ' o '
            else:
                printout += '   '
        printout += ' \n'
        row -= 10
    width = 3 * len(categories)
    printout += '    ' + '-'*width + '-\n'

    longest = 0
    for cat in categories:
        if len(cat.cat_name) > longest:
            longest = len(cat.cat_name)
    i = 0
    while i < longest:
        printout += '    '
        for cat in categories:
            if len(cat.cat_name) < i+1:
                printout += '   '
            else:
                printout += ' ' + cat.cat_name[i] + ' '
        printout += ' \n'
        i += 1
    printout = printout.rstrip('\n')

    return printout