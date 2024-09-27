def categorize_temperature(temp):
    if temp > 30:
        return "Hot"
    elif 20 <= temp <= 30:
        return "Warm"
    elif 10 <= temp <= 19:
        return "Cool"
    else:
        return "Cold"

temperature = 28
print(categorize_temperature(temperature))  