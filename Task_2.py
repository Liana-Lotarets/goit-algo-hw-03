# Import the module "random".
import random

# Define the function get_numbers_ticket().
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # Create the empty set for numbers.
    random_unique_numbers = set()
    # Check the conditions for the parameters min, max and quantity.
    if min >= 1 and max <= 1000 and min <= quantity <= max:
        # Add random elements to the set until their number will be equal to "quantity".
        while len(random_unique_numbers) < quantity:
            random_unique_numbers.add(random.randint(min, max))
        # Convert the set to a list.
        random_unique_numbers = list(random_unique_numbers)
        # Sort the list.
        random_unique_numbers.sort()
        # Return the sorted list of the random unique numbers.
        return random_unique_numbers
    else:
        # The conditions for the parameters are not satisfied. Therefore, return the empty list.
        print('Argument values are incorrect.')
        return []
#  The end of the function definition.

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers: ", lottery_numbers)