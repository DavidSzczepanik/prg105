# Theater Ticket Sales System
# This program calculates ticket prices for a school play based on customer category
# and applies volume discounts for bulk purchases

print("SCHOOL PLAY TICKET SALES")
print("=" * 30)

# Define ticket prices for each customer category
STUDENT_PRICE = 5.00
VETERAN_PRICE = 7.00
SPONSOR_PRICE = 2.00
RETIREE_PRICE = 6.00
GENERAL_PRICE = 10.00

# Display pricing menu to customer
print("\nPLAY PRICES PER TICKET")
print("1. Student: $" + format(STUDENT_PRICE, '.2f'))
print("2. Veteran: $" + format(VETERAN_PRICE, '.2f'))
print("3. Show Sponsor: $" + format(SPONSOR_PRICE, '.2f'))
print("4. Retiree: $" + format(RETIREE_PRICE, '.2f'))
print("5. General Public: $" + format(GENERAL_PRICE, '.2f'))

# Get customer category selection
category = int(input("\nPlease enter the number of the category you fit for purchasing tickets: "))

# Determine base ticket price based on customer category
if category == 1:
    base_price = STUDENT_PRICE
elif category == 2:
    base_price = VETERAN_PRICE
elif category == 3:
    base_price = SPONSOR_PRICE
elif category == 4:
    base_price = RETIREE_PRICE
elif category == 5:
    base_price = GENERAL_PRICE
else:
    print("Invalid category selection.")
    base_price = GENERAL_PRICE  # Default to general admission for invalid input

# Get number of tickets requested
num_tickets = int(input("How many tickets would you like to buy? "))

# Calculate volume discount based on quantity purchased
# 4-8 tickets: 10% discount, 9-15 tickets: 15% discount, 16+ tickets: 20% discount
if 4 <= num_tickets <= 8:
    discount_rate = 0.10
    discount_multiplier = 0.90
elif 9 <= num_tickets <= 15:
    discount_rate = 0.15
    discount_multiplier = 0.85
elif num_tickets > 15:
    discount_rate = 0.20
    discount_multiplier = 0.80
else:
    discount_rate = 0.00
    discount_multiplier = 1.00

# Calculate costs
original_total = base_price * num_tickets
discounted_total = original_total * discount_multiplier
price_per_ticket = discounted_total / num_tickets

# Display pricing summary
print("\n" + "=" * 40)
print("PRICING SUMMARY")
print("=" * 40)
print("Cost before any discounts were applied: $" + format(original_total, '.2f'))
print("Your price after all discounts were applied is: $" + format(discounted_total, '.2f'))
print("Your price is $" + format(price_per_ticket, '.2f') + " per ticket.")

# Display discount information if applicable
if discount_rate > 0:
    savings = original_total - discounted_total
    print("You saved $" + format(savings, '.2f') + " with a " + format(discount_rate * 100, '.0f') + "% volume discount!")