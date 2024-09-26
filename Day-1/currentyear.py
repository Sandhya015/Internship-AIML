def calculate_age(birth_year):
    current_year = 2023
    current_age = current_year - birth_year
    return current_age

try:
    birth_year = int(input("Enter your birth year: "))
    print("The current age is", calculate_age(birth_year))
except ValueError:
    print("Please enter a valid birth year.")