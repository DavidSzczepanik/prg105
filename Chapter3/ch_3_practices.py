# 3.1 Relational Operators
# 1) Write a statement using the variables below and a greater-than sign that will evaluate to true.
# 2) Write a statement using the variables below that compares two of the variables to see if they are equal.
# 3) Write a statement using the variables below that compares two of the variables to see if they are not equal.
# 4) Write a statement using the variables below that uses the less than or equal to operator.
# - Write individual print statements that contain the statements above.

# variables
a = 6
b = 8
c = 5

# 1
print(a > c)
# 2
print (a == b)
# 3
print(a != b)
# 4
print(a <= b)

# 3.2 The if else statement
# Add code below to determine if age is greater than or equal to 18. Depending on the answer, display the appropriate statement:
# - "You are old enough to vote" or "You are not old enough to vote"
# - Use the if-else strcture

age = int(input("What is your age?"))
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

# 3.3 Comparing strings
# Complete the code below so that if the user input matches the password. 
# - It will display "that is correct" otherwise display "that is not correct"

password = "narwhals"
user_input = input("Please enter the password: ")
if user_input == password:
    print("That is correct.")
else:
    print("That is not correct.")

# 3.4 If - elif - else
# Complete the code to accept a number between 1 and 5 from the user and display a roman numeral for that number.
# If the number entered is not between 1 and 5, have the else statement display "That is not a valid number".

number = int(input("Enter a number between 1 and 5: "))
if number == 1:
    print("I")
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number == 5:
    print("V")
else:
    print("That is not a valid number.")

# 3.5 A series of conditions
# Buffet prices are based on the persons age.
# - If the person is a senior citizen (62 or over), the charge is $9.89.
# - If the person is age 12-61, the charge is $12.89.
# - If the person is a child of under age 3, they eat for free
# - If the child is between 4 and 11 they are charged $0.99 for each year of age
# Complete the code below.

age = int(input("Enter the age of the person: "))
if age >= 62:
    print("The charge is $9.89.")
elif age >= 12:
    print("The charge is $12.89.")
elif age <= 3:
    print("The child eats for free.")
elif age >= 4 and age <= 11:
    print("The charge is $" + str(age * 0.99) + ".")

# 3.5 Logical Operators
# Using the variables below, combine relational comparisons using logical operators
# 1) Write a print statement using the and operator that will evaluate to true
# 2) Write a print statement using the or operator that will evaluate to true
# 3) Write a print statement using the not operator that will evaluate to true

d = 10
e = 10
f = 12
print(d < 15 and f > 5)
print(d == 10 or e < 8)
print(d != 11)

# 3.6 Boolean variables
# You are programming a baby doll. 
# - If the baby doll is tired, it will close its eyes
# - If it is hungry, it will cry.
# Write code to print "Eyes open" or "Eyes closed" on the tired value
# Then print "Crying" or "Quiet" depending on the hungry value

tired = False
hungry = True

if tired:
    print("Eyes closed")
else:
    print("Eyes open")

if hungry:
    print("Crying")
else:
    print("Quiet")