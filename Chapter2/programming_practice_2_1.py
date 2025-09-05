# Mad Libs: Song of the Open Road
# Author: David Szczepanik (Modified)
# Based on Walt Whitman's "Song of the Open Road"

print("Welcome to Mad Libs: Song of the Open Road!")
print("Please provide the following words to create your personalized poem:\n")

# Getting input from the user
adjective1 = input("Enter an adjective (like happy, excited): ")
adjective2 = input("Enter another adjective (like strong, brave): ")
noun1 = input("Enter a noun (like mountain, river): ")
color = input("Enter a color: ")
verb1 = input("Enter a verb ending in -ing (like running, singing): ")
noun2 = input("Enter a plural noun (like books, computers): ")
adjective3 = input("Enter an adjective describing emotion (like cheerful, worried): ")
place = input("Enter a place (like library, park): ")
noun3 = input("Enter a plural noun (like stars, flowers): ")
verb2 = input("Enter a verb (like dance, laugh): ")

print("\n" + "="*50)
print("Here's your personalized poem!")
print("="*50 + "\n")

# Printing the modified poem with user variables
print("Song of the Open Road, by Walt Whitman (Mad Libs Version)\n")

print("Afoot and " + adjective1 + " I take to the open road,")
print(adjective2 + ", free, the " + noun1 + " before me,")
print("The long " + color + " path before me leading wherever I choose.\n")

print("Henceforth I ask not good-fortune, I myself am good-fortune,")
print("Henceforth I " + verb1 + " no more, postpone no more, need nothing,")
print("Done with indoor complaints, " + noun2 + ", " + adjective3 + " criticisms,")
print("Strong and content I travel the open road.\n")

print("The " + place + ", that is sufficient,")
print("I do not want the " + noun3 + " any nearer,")
print("I know they are very well where they are,")
print("I know they suffice for those who belong to them.\n")

print("(Still here I carry my old delicious burdens,")
print("I carry them, men and women, I carry them with me wherever I " + verb2 + ",")
print("I swear it is impossible for me to get rid of them,")
print("I am filled with them, and I will fill them in return.)\n")

print("Thank you for playing Mad Libs!")