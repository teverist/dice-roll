import random


# Main functionality
def parse_input(input):
    if input.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input)
    elif input == "exit":
        SystemExit(1)
    else:
        print("Please enter a number from 1 - 6. ")
        num_dice_input


num_dice_input = input("How many dice would you like to roll? [1-6]. (Type exit to quit): ")
num_dice = parse_input(num_dice_input)



