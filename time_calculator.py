from datetime import datetime

from datetime import datetime

# Ask the user to enter their date of birth
date_birth_str = input("Insert your birthday (giorno/mese/anno): ")

# Converts the string into a datetime object
try:
    date_birth = datetime.strptime(date_birth_str, "%d/%m/%Y")
except ValueError:
    print("Incorrect date format. Use the day/month/year format.")
    exit()

# Get the current date
today = datetime.now()

# Calculate the difference in years, months, and days
years = today.year - date_birth.year
months = today.month - date_birth.month
days = today.day - date_birth.day

# If the days are negative, it means that the current day hasn't been reached yet this month
if days < 0:
    months -= 1
    days += 30  # This is a simplification, since not all months have 30 days

# If the months are negative, it means that the current year hasn't reached the birth month yet
if months < 0:
    years -= 1
    months += 12

# Print the result
print(f"You are {years} years, {months} months, and {days} days old.")
