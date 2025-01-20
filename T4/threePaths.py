# Start

# Initialize variable
user_Number = 0

# Prompt user for input
user_Number = int(input("Please enter a integer: "))

# Check if Zero, Negative, or Positive
if (user_Number == 0):
    print("Your number is equal to Zero")
else:
    if (user_Number < 0):
        print("Your number is less than Zero")
    else:
        print("Your number is greater than Zero")

# End