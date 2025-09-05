# Personal Budget Calculator
# This program helps users analyze their monthly spending by calculating
# what percentage of their income goes to different expense categories

print("Personal Budget Calculator")
print("=" * 30)
print("Enter your monthly income and expenses to see your budget breakdown.\n")

# Collect user input for monthly income and expenses
# Note: Converting to float as required by assignment specifications
income = float(input("What is your total net monthly income? "))
housing = float(input("How much do you spend on housing each month? "))
food = float(input("How much do you spend on food each month? "))
transportation = float(input("How much do you spend on transportation each month? "))
phone = float(input("How much do you spend on your phone bill each month? "))
utilities = float(input("How much do you spend on your utilities each month? "))
clothing = float(input("How much do you spend on clothing each month? "))

# Calculate the percentage of income spent on each expense category
housing_budget = housing / income
food_budget = food / income
transportation_budget = transportation / income
phone_budget = phone / income
utilities_budget = utilities / income
clothing_budget = clothing / income

# Calculate remaining money after all expenses
remaining_money = income - housing - food - transportation - phone - utilities - clothing

# Display budget analysis results
print("\n" + "=" * 40)
print("BUDGET BREAKDOWN")
print("=" * 40)
print("Housing takes up " + format(housing_budget, '.2%') + " of your monthly budget.")
print("Food takes up " + format(food_budget, '.2%') + " of your monthly budget.")
print("Transportation takes up " + format(transportation_budget, '.2%') + " of your monthly budget.")
print("Phone takes up " + format(phone_budget, '.2%') + " of your monthly budget.")
print("Utilities takes up " + format(utilities_budget, '.2%') + " of your monthly budget.")
print("Clothing takes up " + format(clothing_budget, '.2%') + " of your monthly budget.")
print("\nYou have $" + format(remaining_money, ',.2f') + " left from your income after paying these monthly expenses.")