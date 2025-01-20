import random

# Initialize variables
user_Guess = 0
num_Guess = 0
randint = 0

# Store values
randint = random.randint(1,100)

# Introduction
print("Welcome to the guessing game! You have up to 10 attempts to guess the number.", end='\n')

# Loop 10 times
for i in range(10):
    
    # Counter
    num_Guess += 1
    
    # Prompt user for input
    user_Guess = int(input(f"\nAttempt #{num_Guess}: Guess a number between 1 to 100: "))
    
    # Error trap
    if (user_Guess < 1 or user_Guess > 100):
        print("SyntaxError: Invalid syntax")
        break
    else:  
        # Check if random integer is equal, less or greater than the user integer
        if (user_Guess == randint):
            
            # Output if both are euqal to the random integer
            print(f"\n\tYou are correct the number was  {randint}")
            
            # Exit Loop
            break

        else:
            if (user_Guess < randint):
                
                # Output if user integer is less than the random integer
                print("\n\tYour guess was too low.", end='\n')
            
            else:
                # Output if user integer is greater than the random integer
                print("\n\tYour guess was too high.", end='\n')
# Check if random integer is not equal to user integer
if (user_Guess != randint):
        
    # Output if loop is terminated
    print(f"\n\tThe correct number was  {randint}")