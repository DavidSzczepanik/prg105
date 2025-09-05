# Chicken Cordon Bleu Recipe Calculator
# This program displays a recipe for 6 servings, then adjusts quantities based on user input

# Base ingredient quantities for Chicken Cordon Bleu (serves 6)
chicken_breasts = 4
garlic_powder = 1
onion_powder = 1
swiss_cheese = 16
ham = 0.5
flour_chicken = 1
eggs = 4
breadcrumbs = 2

# Base ingredient quantities for Creamy Dijon Sauce (serves 6)
butter = 3
garlic_cloves = 2
flour_sauce = 3
milk = 2
dijon_mustard = 0.25
parmesan = 1

# Display original recipe for 6 servings
print("CHICKEN CORDON BLEU RECIPE")
print("=" * 40)
print("Original Recipe - Serves 6 People\n")

print("\t\tChicken Cordon Bleu")
print("-" * 40)
print("Boneless, Skinless Chicken Breasts: " + str(chicken_breasts) + " breast(s)")
print("Salt and Pepper: To taste")
print("Garlic Powder: " + str(garlic_powder) + " tablespoon(s)")
print("Onion Powder: " + str(onion_powder) + " tablespoon(s)")
print("Swiss Cheese: " + str(swiss_cheese) + " thin slices")
print("Ham: " + str(ham) + " pound(s)")
print("Peanut or Vegetable Oil: For frying")
print("All-Purpose Flour: " + str(flour_chicken) + " cup(s)")
print("Eggs: " + str(eggs) + " egg(s), beaten")
print("Panko Bread Crumbs: " + str(breadcrumbs) + " cup(s)")

print("\n\t\tCreamy Dijon Sauce")
print("-" * 40)
print("Butter: " + str(butter) + " tablespoon(s)")
print("Garlic Cloves: " + str(garlic_cloves) + " clove(s), minced")
print("All-Purpose Flour: " + str(flour_sauce) + " tablespoon(s)")
print("Milk: " + str(milk) + " cup(s)")
print("Dijon Mustard: " + str(dijon_mustard) + " cup(s)")
print("Parmesan Cheese: " + str(parmesan) + " cup(s), shredded")
print("Salt and Pepper: To taste\n")

# Get desired serving size from user
serving_size = 6
print("=" * 40)
wanted_serving_size = int(input("How many servings would you like to make? "))

# Calculate adjustment multiplier
ingredient_adjuster = wanted_serving_size / serving_size

# Display adjusted recipe quantities
print("\nADJUSTED RECIPE")
print("=" * 40)
print("Custom Recipe - Serves " + str(wanted_serving_size) + " People\n")

print("\t\tChicken Cordon Bleu")
print("-" * 40)
print("Boneless, Skinless Chicken Breasts: " + str(format(chicken_breasts * ingredient_adjuster, ".1f")) + " breast(s)")
print("Salt and Pepper: To taste")
print("Garlic Powder: " + str(format(garlic_powder * ingredient_adjuster, ".1f")) + " tablespoon(s)")
print("Onion Powder: " + str(format(onion_powder * ingredient_adjuster, ".1f")) + " tablespoon(s)")
print("Swiss Cheese: " + str(format(swiss_cheese * ingredient_adjuster, ".1f")) + " thin slices")
print("Ham: " + str(format(ham * ingredient_adjuster, ".1f")) + " pound(s)")
print("Peanut or Vegetable Oil: For frying")
print("All-Purpose Flour: " + str(format(flour_chicken * ingredient_adjuster, ".1f")) + " cup(s)")
print("Eggs: " + str(format(eggs * ingredient_adjuster, ".1f")) + " egg(s), beaten")
print("Panko Bread Crumbs: " + str(format(breadcrumbs * ingredient_adjuster, ".1f")) + " cup(s)")

print("\n\t\tCreamy Dijon Sauce")
print("-" * 40)
print("Butter: " + str(format(butter * ingredient_adjuster, ".1f")) + " tablespoon(s)")
print("Garlic Cloves: " + str(format(garlic_cloves * ingredient_adjuster, ".1f")) + " clove(s), minced")
print("All-Purpose Flour: " + str(format(flour_sauce * ingredient_adjuster, ".1f")) + " tablespoon(s)")
print("Milk: " + str(format(milk * ingredient_adjuster, ".1f")) + " cup(s)")
print("Dijon Mustard: " + str(format(dijon_mustard * ingredient_adjuster, ".1f")) + " cup(s)")
print("Parmesan Cheese: " + str(format(parmesan * ingredient_adjuster, ".1f")) + " cup(s), shredded")
print("Salt and Pepper: To taste\n")

print("Enjoy your homemade Chicken Cordon Bleu!")