# user.py
class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses  # dictionary with keys: utilities, entertainment, school_fees, shopping, healthcare

    def to_csv_row(self):
        """Return user data as a list matching CSV columns."""
        return [
            self.age,
            self.gender,
            self.income,
            self.expenses.get("utilities", 0),
            self.expenses.get("entertainment", 0),
            self.expenses.get("school_fees", 0),
            self.expenses.get("shopping", 0),
            self.expenses.get("healthcare", 0),
        ]
