def check_positive(number):
    try:
        if number<0:
            raise ValueError("Negative numbers are not allowed!")
        return number
    except ValueError as e:
        return str(e)