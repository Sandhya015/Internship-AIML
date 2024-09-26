def is_prime_or_even_odd(n):
    if n < 2:
        return "Even" if n % 2 == 0 else "Odd"
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Even" if n % 2 == 0 else "Odd"
    
    return True

print(is_prime_or_even_odd(3))  
print(is_prime_or_even_odd(4))  
print(is_prime_or_even_odd(9)) 