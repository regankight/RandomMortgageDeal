import random

# Mortgage package database
mortgage_packages = [
    {"name": "Standard 30-year Fixed", "rate": 3.5, "min_credit_score": "good", "min_down_payment": 10},
    {"name": "15-year Fixed Deal", "rate": 2.9, "min_credit_score": "excellent", "min_down_payment": 20},
    {"name": "5/1 ARM (Adjustable)", "rate": 3.2, "min_credit_score": "fair", "min_down_payment": 5},
    {"name": "Low Down Payment Special", "rate": 4.1, "min_credit_score": "poor", "min_down_payment": 3},
]

print("Welcome to the Mortgage Deal Picker!")
loan_amount = float(input("Enter your desired loan amount: "))
credit_score = input("Enter your credit score rating (excellent/good/fair/poor): ").lower()
down_payment_percentage = float(input("Enter your down payment percentage: "))

# Filter options based on user input
eligible_packages = [
    package for package in mortgage_packages
    if package["min_credit_score"] <= credit_score and package["min_down_payment"] <= down_payment_percentage
]

if eligible_packages:
    # Pick a random eligible package
    selected_package = random.choice(eligible_packages)
    print(f"We recommend: {selected_package['name']} with a rate of {selected_package['rate']}%")
else:
    print("No exact matches found.")
    # Suggest a random package from the full list
    random_deal = random.choice(mortgage_packages)
    print(f"Random special deal: {random_deal['name']} at {random_deal['rate']}% interest.")
monthly_payment = (loan_amount * selected_package["rate"] / 100) / 12
print(f"Estimated monthly payment: ${monthly_payment:.2f}")
