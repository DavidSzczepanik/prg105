# Financial Aid Eligibility Checker
# This program determines if a student qualifies for financial aid based on:
# - New students automatically qualify
# - Current students must meet all criteria: GPA >= 2.0, no drug-related criminal history,
#   enrolled in > 6 credit hours, and yearly income < $50,000

print("Financial Aid Eligibility Checker")
print("=" * 35)

# Check if student is new (new students automatically qualify)
student_status = input("Are you a new student? Enter yes or no: ").lower()

if student_status == "yes":
    print("\nYou are eligible for financial aid.")
else:
    # For current students, check all eligibility requirements
    print("\nPlease answer the following questions to determine your eligibility:")
    
    # Check GPA requirement (must be 2.0 or higher)
    gpa = float(input("Enter your GPA: "))
    
    if gpa >= 2.0:
        # Check criminal history requirement (no drug-related convictions)
        criminal_history = input("Do you have a criminal history involving drugs? Enter yes or no: ").lower()
        
        if criminal_history == "no":
            # Check credit hours requirement (must be more than 6)
            credit_hours = int(input("Enter your credit hours for next semester: "))
            
            if credit_hours > 6:
                # Check income requirement (must be less than $50,000)
                yearly_income = int(input("Enter your yearly income: $"))
                
                if yearly_income < 50000:
                    print("\nYou are eligible for financial aid.")
                else:
                    print("\nYou are not eligible for financial aid.")
                    print("Reason: Your yearly income is $50,000 or higher.")
            else:
                print("\nYou are not eligible for financial aid.")
                print("Reason: You must enroll in more than 6 credit hours.")
        else:
            print("\nYou are not eligible for financial aid.")
            print("Reason: You have a criminal history involving drugs.")
    else:
        print("\nYou are not eligible for financial aid.")
        print("Reason: Your GPA is below 2.0.")