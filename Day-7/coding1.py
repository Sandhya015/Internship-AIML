def divide_numbers(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:

        return "Error:Divison by Zero is not allowed"