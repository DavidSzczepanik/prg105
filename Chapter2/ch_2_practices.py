# 2.3 display output with the string function 
# Write two lines of code:
# the first one displays your name
# the second one displays your major

print("David Szczepanik")
print("Computer Science")

# 2.3 using quotes 
# Write a statement that displays
# The dog says "woof!"

print('The dog says "woof!"')

# 2.4 working with variables and printing their values
# 1) Declare a variable named age, and set the initial value to your age
# 2) Print the variable value
# 3) Print the word age with a space and the variable value, example: age 25
# 4) Assign 42 to the age variable
# 5) Print the word age with a space and the variable value, age 42

age = 19
print(age)
print("age", age)
age = 42
print("age", age)

# 2.6 Keyboard input
# 1) Get the user to enter their name using an input statemtn and assign it to a variable called name
# 2) Print a line that greets the user by name. Example: Hello, Meri

name = input('What is your name?')
concat = "Hello, " + name
print(concat)

# 2.6 - 2.7 numeric input, performing calculations
# 1) Get the user to enter their age, store it as an integer. Use int() to convert a string to an integer.
# 2) Print the age in a sentence using a comma in the print statement to seperate items (when using a comma in a print statemnt, you can mix numbers and strings)
# 3) Add 1 to the age: age = age + 1
# 4) Print the result using concatenation in the print statement: Remember - when concatenating a variable that holds numbers you need to convert it to a string: str(variable)
# example: "Next year you will be " + str(age)

age = int(input("What is your age?"))
print("You are", age, "years old.")
age = age + 1
print("Next year you will be " + str(age))

# 2.7 performing calculations
# 1) Calculate 7 divided by 2, print the equation and the result
# 2) Calculate the remainder of 7 divided by 2, use the modulus operator, print the equation and the result

num = 7 / 2
print("7 / 2 =", num)
num = 7 % 2
print("7 % 2 =", num)


# 2.7 data conversion
# Write the equation as described below, the addition equation has been done as a sample
# Note: you don't need to assign the result to a variable when the result will only be displayed
# Sample:
# 0) Write an equation that adds an integer to an integer, display the equation and the rsult with a print statement

print("5 + 3 =", str(5 + 3))

# 1) Write an equation that divides an integer by an integer, display the equation and the result with a print statement

print("8 / 2 =", str(8 / 2))

# 2) Write an equation that divides a float by a float, display the equation and the result with a print statement

print("8.0 / 2.0 =", str(8.0 / 2.0))

# 3) Write an equation that divides a float by an integer, display the equation and the result with a print statement

print("8.0 / 2 =", str(8.0 / 2))

# 2.8 Using print statement options
# Modify the following code to display on one line, without merging the lines of code.
# Seperate the words with a hyphen, example result: one-two-three
# DO NOT MERGE INTO ONE LINE OF CODE< use print statement options
print('one', end='-')
print('two', end='-')
print('three')

# 2.8 Using escape codes
# Modify the following line of code to add tabs between the days of the week
print("Sunday\tMonday\tTuesday\tWednesday\tThursday\tFriday\tSaturday")

# 2.8 Concatenating strings (Displaying Multiple Items with the + Operator)
# 1) Have the user enter their name
# 2) Greet the user, concatenate hello and their name into one string

name = input("What is your name?")
print("Hello, " + name)

# 2.8 Formatting numbers
# Modify the print statement to format the number
# - to display a minimum field width of 30
# - to include commas
# - with only two numbers showing to the right of the decimal point
# example: 6,548,974,897.57
number = 6548974897.5687979797
print(format(number, '30,.2f'))

# 2.8 Formatting percentage
# Format the following as a percentage with 2 as the precision
# Sample:
# - percent = .25834
# - print(format(percent, '%'))
percentage = .7654
print(format(percentage, '%'))