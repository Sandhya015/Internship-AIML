def grade(score):
    if not isinstance(score, int):
        raise TypeError("Score must be an integer.")
    
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score = 80
print(grade(score))  