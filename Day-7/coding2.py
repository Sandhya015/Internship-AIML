def get_valid_number():
    try:
        user_input =input("enter the number")
        number=int(user_input)
        return number

    except ValueError:
        return "Error: That's not a valid number"