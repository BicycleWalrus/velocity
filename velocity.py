#!/usr/bin/env python3
"""TPatrick | Alta3 Research
   Virtual Pet Bird with Scientifically
   Accurate Air Speed Velocity Calculator"""

""" FRONT MATTER DICTIONARIES AND FUNCTIONS """

# Bird dictionary
bird = {"name": "", "type": "", "age": 0, "hunger": 0, "toys":
        ["Perch", "Hanging Bird Bath", "Activity Wall", "Jingle Ball", "Shredding Toy"]}

# Bird types data
bird_types = {"Budgerigar" : {"Body Mass (g)": 13, "Frequency (Hz)": 27, "Amplitude (cm)": 11, "Wingspan (cm)": 27},
        "European Swallow": {"Body Mass (g)": 20, "Frequency (Hz)": 18, "Amplitude (cm)": 18, "Wingspan (cm)": 30},
        "Downy Woodpecker": {"Body Mass (g)": 27, "Frequency (Hz)": 14, "Amplitude (cm)": 29, "Wingspan (cm)": 31},
        "European Starling": {"Body Mass (g)": 85, "Frequency (Hz)": 14, "Amplitude (cm)": 26, "Wingspan (cm)": 35}}

# Initial Virtual Bird Setup!
def init_bird():
    """ Initialize the Application with User Input Data """
    bird_type = ""
    bird_options = list(bird_types.keys())

    # Validate the input
    while bird_type not in bird_options:
        print("Here is a list of available Pet Birds: \n") # Print Bird Types
        for option in bird_options:
            print(option)
        bird_type = input("\nWhich bird would you like to give a home?: ") # Name from user

    print(f"You selected {bird_type}! Congratulations on this important decision!")
    bird["type"] = bird_type

    # Name our bird
    bird["name"] = input(f"What would you like to name your {bird_type}? ")
    print("You\'re now the proud owner of " + bird["name"] + ", the " + bird["type"] + "! ")

# Print Menu
def menu(menu_options):
    """Present Menu Options"""
    option_keys = list(menu_options.keys())

    print("\nWhat would you like to do?")
    print("\n==========================")
    for key in option_keys:
        print(key + ":\t" + menu_options[key]["text"])

# Play with toys
def play_bird():
    """ Play with our Virtual Pet """
    toy_options = bird['toys']
    print("*********************")
    print(f"Which toy would you like to use to play with {bird['name']}?")
    print("===============================\n")

    # Specific toy number to select from the Dictionary
    toy_num = -1
    while toy_num < 0 or toy_num > len(toy_options) - 1:
        for i in range(len(toy_options)):
            print(str(i) + ": " + toy_options[i])
        toy_num = int(input("\nInput the number of the toy you would like: "))

    # Get the selected toy option from our list
    chosen_toy = toy_options[toy_num]
    print(f"{bird['name']} had a great time playing with {chosen_toy}!")

# Feeding our Pet to decrease hunger
def feed_bird():
    """ Feed our Virtual Bird """
    # If negative, will set to 0
    new_hunger = bird["hunger"] - 20
    if new_hunger < 0:
        new_hunger = 0
    bird["hunger"] = new_hunger

    # Print results to the user
    print("*********************")
    print(f"You fed {bird['name']}! Decreasing hunger by 10!\n Current hunger: {bird['hunger']}")

# Quit the game
def quit_velocity():
    """Quit the Application"""
    print("*********************")
    print("Quiting Velocity")

# Bird Statistics
def print_stats():
    """Deliver Bird Statistics to user"""
    print("*********************")
    print(f"\n{bird['name']} the {bird['type']} is doing great!")
    print(f"{bird['name']} has: {str(len(bird['toys']))} toys available to play with!")
    for toy in bird['toys']:
        print(toy)
    print(f"\n{bird['name']} is currently at a hunger level of {bird['hunger']} out of 100.")
    print(f"{bird['name']} is {str(bird['age'])} days old!")

# Air Speed Velocity Calculator
def velocity_check():
    """ Calculate Air Speed Velocity """
    print("*********************")
    print("Feature coming soon!")

""" END FRONT MATTER - BEGIN MAIN APPLICATION """

# Main Game Loop
def velocity():
    """ Main Application """
    init_bird() # Choose Bird Type, and Name

    # Menu Options as a Dictionary
    menu_options = { "S": { "function": print_stats, "text": bird['name'] + "\'s vitals!"},
                     "F": { "function": feed_bird, "text": "Feed " + bird["name"]},
                     "P": { "function": play_bird, "text" : f"Playtime with {bird['name']}"},
                     "V": { "function": velocity_check, "text" : f"Check {bird['name']}'s Air Speed Velocity!"},
                     "Q": { "function": quit_velocity, "text": "Quit Velocity"}
                   }

    keep_playing = True

    while keep_playing:
        # Gamify Hunger, and Age - If Bird dies, quit Velocity
        bird["hunger"] += 10
        if bird["hunger"] >= 100:
            print("*********************")
            print(f"{bird['name']} has sadly perished.")
            print("*********************")
            print("\nIn a desperate attempt to seek out food,")
            print(f"{bird['name']} the {bird['type']} escaped from his")
            print("pen, only to be eaten by a white carnivorous rabbit")
            print("who can only be destroyed by the Holy Hand Grenade.")
            print(f"\nYou have failed {bird['name']}. It is entirely your fault he has died.")

            # Leave a subtle reminder to the user about what they've done
            with open('hey.txt', mode='w', encoding="utf8") as file_object:
                print(f"You killed {bird['name']}.", file=file_object)
            break
        else:
            menu_selection = ""
        bird["age"] += 1

        # Validate Input from User
        while menu_selection not in menu_options.keys():
            # Print\Input for Menu Options
            menu(menu_options)
            menu_selection = input("\nPlease Select a Menu Option: \n").upper()
        menu_options[menu_selection]["function"]()

        # Quit the game if user inputs "Q"
        if menu_selection == "Q":
            keep_playing = False
    print()
velocity()
