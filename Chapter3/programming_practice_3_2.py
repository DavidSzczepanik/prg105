# Credit Score Analyzer
# This program evaluates a user's credit score and categorizes it according to
# standard credit rating ranges used by financial institutions

print("Credit Score Analyzer")
print("=" * 25)

# Get credit score input from user (valid range: 300-850)
credit_score = int(input("What is your credit score? Please enter an integer between 300 and 850: "))

# Determine credit rating category based on score ranges
if 300 <= credit_score <= 579:
    rating = "poor"
elif 580 <= credit_score <= 669:
    rating = "fair"
elif 670 <= credit_score <= 739:
    rating = "good"
elif 740 <= credit_score <= 799:
    rating = "very good"
elif 800 <= credit_score <= 850:
    rating = "excellent"
else:
    # Handle invalid scores outside the 300-850 range
    rating = "invalid"

# Display the credit score analysis result
if rating == "invalid":
    print("\nError: Please enter a valid credit score between 300 and 850.")
else:
    print(f"\nWith a credit score of {credit_score}, you have a {rating} credit rating.")
    
    # Provide additional context about what each rating means
    print("\nCredit Rating Guide:")
    print("• Poor (300-579): Difficulty getting approved for credit")
    print("• Fair (580-669): May qualify for some credit with higher rates")
    print("• Good (670-739): Likely to be approved for credit at reasonable rates")
    print("• Very Good (740-799): Eligible for better interest rates and terms")
    print("• Excellent (800-850): Qualify for the best rates and premium credit products")