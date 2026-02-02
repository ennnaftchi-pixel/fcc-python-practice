"""
Budget App
Tracks spending by category and displays a percentage spend chart.

Part of the freeCodeCamp Scientific Computing with Python certification.
"""

class Category:
    """Represents a budget category with a transaction ledger."""

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Add funds to the category."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Withdraw funds if available."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Return the current balance."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """Transfer funds to another category."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Check if enough balance exists."""
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        lines = ""

        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            lines += desc + amt + "\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + lines + total


def create_spend_chart(categories):
    """Create a bar chart showing percentage spent by category."""
    chart = "Percentage spent by category\n"

    spent = []
    total_spent = 0

    for cat in categories:
        s = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(s)
        total_spent += s

    percentages = [(int((s / total_spent) * 100) // 10) * 10 for s in spent]

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            chart += (cat.name[i] if i < len(cat.name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")
