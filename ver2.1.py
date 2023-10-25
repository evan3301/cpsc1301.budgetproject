from spendingCategories import spending_categories
from stateTaxes import tax_rates

class PersonalBudget:
    def __init__(self, spending_categories, tax_rates):
        # Initialize dictionary attributes
        self.spending_categories = spending_categories
        self.tax_rates = {state.lower(): tax_rates for state, tax_rates in tax_rates.items()}


    def usrInput(self):
        try:
            salary = float(input('Enter you expected annual salary: $'))
            state = input('Enter your state: ')
            return salary, state

        except ValueError:
            print('Invalid input, try again: ')
            return self.usrInput


    def calcBudget(self, salary, state):
        state = state.lower()
        
        # If state input not found in stateTaxes dictionary
        if state not in self.tax_rates:
            raise ValueError('State not found')

        # New empty dictionary to store budget calculations
        budget = {}

        # Get key-value pair (selected state: state tax rate)
        state_tax = self.tax_rates[state]
        post_tax = salary * (1 - (state_tax / 100))

        # Iterate over key-value pair (category, percentage) in spendingCategories dicitonary
        ## Store new calculated value with corresponding key in budget dictionary
        for category, percentage in self.spending_categories.items():
            budget[category] = (post_tax * percentage) / 12
        return budget


    def display(self, budget):
        print('Your personalized monthly budget:')

        # Iterate over key-value pair (category, amount) in budget dictionary and print each
        ## .items() function converts budget dictionary to iterable tuple
        for category, amount in budget.items():
            print(f'{category:}: ${round(amount, 2)}')


def main():
    budget_plan = PersonalBudget(spending_categories, tax_rates)

    try:
        salary, state = budget_plan.usrInput()
        budget = budget_plan.calcBudget(salary, state)

        budget_plan.display(budget)

    # If value error, display error message
    except ValueError as error:
        print(str(error))


if __name__ == '__main__':
    main()
