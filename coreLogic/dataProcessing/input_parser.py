

"""
=========================================================================================
Input Reception

Asks the user for input and validates it.
    Validate Input: Ensure that the user input is not empty or meets specific   criteria
    Error Handling: Handle unexpected input accordingly

Returns:
    str: The validated user input

    This ensures the user doesn't enter a blank command and prompts them until valid input is provided. 

==========================================================================================
"""
def get_user_input():
    while True:
        user_input = input("Enter your command: ").strip()
        if user_input:
            return user_input
        else:
            print("Well, that can't be right...one more time.")





"""
===================================================================================
Input Normalization

Cleans and standardizes user input.

Args:
    user_input (str): The raw input from the user.

Returns:
    str: The normalized input, or None if input is valid

===================================================================================

"""

def normalize_input(user_input):
    user_input = ' '.join(user_input().strip().lower().split()) # Remove extra spaces
    return user_input if user_input else None






"""
====================================================================================
Command Parsing

Adding a command parser helps determine the intent behind the user's input.
====================================================================================
"""

def parse_command(normalized_input):
    if normalize_input.startswith("create digimon"):
        return "CREATE_DIGIMON", normalized_input[14:] # Extract Digimon Name
    elif normalized_input.startswith("search"):
        return "SEARCH", normalized_input[7:]
    elif normalized_input == "help":
        return "HELP", None
    else:
        return "UNKNOWN", None
    



"""
======================================================================
Error Handling

When a command is unknown or incomplete, guide the user toward valid inputs.
======================================================================
"""

def handle_invalid_command(command):
    print(f"'{command} is not recognized. Try 'help' for available commands.")