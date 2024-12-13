

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