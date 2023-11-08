import tkinter as tk
from spendingCategories import spending_categories
from stateTaxes import tax_rates

class PersonalBudget:
    def __init__(self, spending_categories, tax_rates):
        self.spending_categories = spending_categories
        self.tax_rates = tax_rates

    def usrInput(self):
        try:
            salary = int(input('Enter your expected annual salary to the nearest dollar: $'))
            state = input('Enter your state: ')
            return salary, state

        except ValueError:
            print('Invalid input, try again: ')
            return self.usrInput()

    def calcBudget(self, salary, state):
        if state not in self.tax_rates:
            raise ValueError('State not found')

        budget = {}
        state_tax = self.tax_rates[state]
        post_tax = salary * (1 - (state_tax / 100))

        for category, percentage in self.spending_categories.items():
            budget[category] = (post_tax * percentage) / 12

        return budget

    def display(self, budget):
        print('Your personalized monthly budget:')
        for category, amount in budget.items():
            print(f'{category}: ${round(amount, 2)}')

class PersonalBudgetGUI(tk.Tk):
    def __init__(self, spending_categories, tax_rates):
        super().__init__()
        self.title("Personal Budget Calculator")
        self.budget_plan = PersonalBudget(spending_categories, tax_rates)

        self.salary_label = tk.Label(self, text="Enter your expected annual salary to the nearest dollar: $")
        self.salary_label.pack()

        self.salary_entry = tk.Entry(self)
        self.salary_entry.pack()

        self.state_label = tk.Label(self, text="Enter your state: ")
        self.state_label.pack()

        self.state_entry = tk.Entry(self)
        self.state_entry.pack()

        self.calculate_button = tk.Button(self, text="Calculate Budget", command=self.calculate_and_display)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def calculate_and_display(self):
        try:
            salary = int(self.salary_entry.get())
            state = self.state_entry.get().strip()

            budget = self.budget_plan.calcBudget(salary, state)

            result_text = "Your personalized monthly budget:\n"
            for category, amount in budget.items():
                result_text += f"{category}: ${round(amount, 2)}\n"

            self.result_label.config(text=result_text)

        except ValueError as error:
            self.result_label.config(text=str(error))

def main():
    app = PersonalBudgetGUI(spending_categories, tax_rates)
    app.mainloop()

main()
