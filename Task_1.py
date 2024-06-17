# Import the module "datetime".
import datetime

# Define the function get_days_from_today().
def get_days_from_today(date: str) -> int:
    try:
        # Convert a date string in the format 'YYYY-MM-DD' to a datetime object.
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    # If the date format is incorrect, then an ValueError will occur.
    except ValueError:
        print('Date format must be YYYY-MM-DD.')
    else:
        # Get the number of days from the beginning of the Christian calendar to the given date.
        number_days_of_given_date = given_date.toordinal()
        # Get the current date.
        current_date = datetime.datetime.today()
        # Get the number of days from the beginning of the Christian calendar to the current date.
        number_days_of_current_date = current_date.toordinal()
        # Calculate the number of days from the given date to the current one.
        return number_days_of_current_date - number_days_of_given_date
# The end of the function definition.

print(get_days_from_today('2024-06-15'))