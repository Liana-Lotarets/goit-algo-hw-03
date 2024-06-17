# Import the module "re".
import re

# Define the function normalize_phone().
def normalize_phone(phone_number: str) -> str:
    # Create a list of all sequences of digits.
    matches = re.findall(r"\d+", phone_number)
    # Combine into a single sequence of digits.
    number = ''.join(matches)
    # Take the last ten digits and add the country code.
    return '+38' + number[-10:]
# The end of the function definition.

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers: ", sanitized_numbers)
