from datetime import datetime
from dateutil.relativedelta import relativedelta

# Ask the user to enter their date of birth
date_birth_str = input("Insert your birthday (days/months/years): ")

# Converts the string into a datetime object
try:
    date_birth = datetime.strptime(date_birth_str, "%d/%m/%Y")
except ValueError:
    print("Incorrect date format. Use the day/month/year format.")
    exit()

# Get the current date
today = datetime.now()

# Calculate the precise difference using relativedelta
# This automatically handles leap years and different month lengths
age = relativedelta(today, date_birth)

years = age.years
months = age.months
days = age.days

# Print the result
print(f"You are {years} years, {months} months, and {days} days old.")
