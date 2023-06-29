import random

def roll_dice():
    min_value = 1
    max_value = 6
    
    # Roll the dice and print the result
    dice_result = random.randint(min_value, max_value)
    print("You rolled a", dice_result)
    
    # Ask the user if they want to roll again
    roll_again = input("Do you want to roll the dice again? (yes/no): ")
    
    # Check if the user wants to roll again
    if roll_again.lower() == "yes" or roll_again.lower() == "y":
        roll_dice()  # Recursive call to roll_dice() function
    
# Start the game
print("Welcome to the Roll the Dice Game!")
roll_dice()