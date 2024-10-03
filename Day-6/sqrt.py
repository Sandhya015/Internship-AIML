import math

def math_operations(num:int) -> dict:
    if num < 1 or num>100:
        raise ValueError("input must be positive")

    result ={
        "square_root":math.sqrt(num),
        "sine_90_degrees":math.sin(math.radians(90)),
        "factorial":math.factorial(num)
    }

    return result