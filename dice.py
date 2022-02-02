import random


def parse_input(input):
    if input.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input)
    elif input == "exit":
        SystemExit(1)
    else:
        print("Please enter a number from 1 - 6. ")
        num_dice_input


def roll_dice(num_die):
    roll_results = []
    for _ in range(num_die):
        roll = random.randint(1,6)
        roll_results.append(roll)

    return roll_results

DICE_ART = {

    1: (

        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",

    ),

    2: (

        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",

    ),

    3: (

        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",

    ),

    4: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    5: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

}

DIE_HEIGHT = len(DICE_ART[1])

DIE_WIDTH = len(DICE_ART[1][0])

DIE_FACE_SEPARATOR = " "


# Main functionality
num_dice_input = input("How many dice would you like to roll? [1-6]. (Type exit to quit): ")
num_dice = parse_input(num_dice_input)


